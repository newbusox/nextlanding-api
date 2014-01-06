import collections
import logging
from django.core.exceptions import ValidationError

from django.db import models, transaction
from jsonfield import JSONField
from localflavor.us.models import USStateField
import reversion
from nextlanding_api.aggregates.search.signals import created, initiated_availability_request, \
  updated_geo_boundary_points
from nextlanding_api.apps.communication_associater.availability.email.email_objects import SearchSpecificEmailMessageRequest

from nextlanding_api.libs.common_domain.aggregate_base import AggregateBase
from nextlanding_api.libs.common_domain.models import RevisionEvent
from nextlanding_api.libs.django_utils.models.utils import copy_django_model_attrs
from nextlanding_api.libs.django_utils.serialization.flexible_json_serializer import JSONSerializer

logger = logging.getLogger(__name__)


class Search(models.Model, AggregateBase):
  email_address = models.EmailField()

  description = models.TextField()

  specified_location = models.CharField(max_length=2048)

  # advanced usage and how to keep dicts ordered
  # upon deserializing https://github.com/bradjasper/django-jsonfield#advanced-usage
  geo_boundary_points = JSONField(load_kwargs={'object_pairs_hook': collections.OrderedDict}, blank=True, null=True)

  address = models.CharField(max_length=255, blank=True, null=True)
  city = models.CharField(max_length=255)
  state = USStateField()
  zip_code = models.CharField(max_length=10, blank=True, null=True)
  lat = models.FloatField()
  lng = models.FloatField()
  formatted_address = models.CharField(max_length=4096)

  no_fee_preferred = models.BooleanField()

  bedroom_min = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)
  bedroom_max = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)
  bathroom_min = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
  bathroom_max = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
  price_min = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
  price_max = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
  sqfeet_min = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
  sqfeet_max = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

  created_date = models.DateTimeField(auto_now_add=True)
  changed_date = models.DateTimeField(auto_now=True)

  def __init__(self, *args, **kwargs):
    super(Search, self).__init__(*args, **kwargs)
    self._amenity_list = []

  @classmethod
  def _from_attrs(cls, **kwargs):
    ret_val = cls()

    if not kwargs.get('description'): raise TypeError('description is required')
    if not kwargs.get('specified_location'): raise TypeError('specified_location is required')

    geo_boundary_points = kwargs.get('geo_boundary_points', None)
    if geo_boundary_points and any(len(geo_points) < 3 for k, geo_points in geo_boundary_points.items()):
      raise ValidationError('at least 3 points per geo_boundary_point are required')

    bedroom_max = kwargs.get('bedroom_max')
    if bedroom_max:
      if bedroom_max < kwargs.get('bedroom_min', None):
        raise ValidationError("bedroom_max must be greater than bedroom_min")

    bathroom_max = kwargs.get('bathroom_max')
    if bathroom_max:
      if bathroom_max < kwargs.get('bathroom_min', None):
        raise ValidationError("bathroom_max must be greater than bathroom_min")

    price_max = kwargs.get('price_max')
    if price_max:
      if price_max < kwargs.get('price_min', None):
        raise ValidationError("price_max must be greater than price_min")

    sqfeet_max = kwargs.get('sqfeet_max')
    if sqfeet_max:
      if sqfeet_max < kwargs.get('sqfeet_min', None):
        raise ValidationError("sqfeet_max must be greater than sqfeet_min")

    ret_val._raise_event(created, sender=Search, instance=ret_val, attrs=kwargs)

    return ret_val

  def _handle_created_event(self, **kwargs):
    amenities = kwargs['attrs'].pop('amenities', None)
    if amenities:
      self._amenity_list.extend(Amenity(amenity_type_id=a) for a in amenities)

    # django model constructor has pretty smart logic for mass assignment
    copy_django_model_attrs(self, **kwargs['attrs'])

    logger.info("{0} has been created".format(self))

  def request_availability_from_contacts(self, from_name, subject, body):
    if not body or not subject or not from_name:
      raise ValidationError("subject, body, and from_name are required")


    search_specific_email_message_request = SearchSpecificEmailMessageRequest(from_name, subject, body)

    self._raise_event(initiated_availability_request, sender=Search, instance=self,
                      search_specific_email_message_request=search_specific_email_message_request)

  def update_geo_boundary_points(self, geo_boundary_points):
    if geo_boundary_points and any(len(geo_points) < 3 for k, geo_points in geo_boundary_points.items()):
      raise ValidationError('at least 3 points per geo_boundary_point are required')

    self._raise_event(updated_geo_boundary_points, sender=Search, instance=self,
                      geo_boundary_points=geo_boundary_points)

  def _handle_updated_geo_boundary_points_event(self, **kwargs):
    self.geo_boundary_points = kwargs['geo_boundary_points']

  def _handle_initiated_availability_request_event(self, **kwargs):
    pass

  def save(self, internal=False, *args, **kwargs):
    if internal:
      with transaction.commit_on_success():
        with reversion.create_revision():
          super(Search, self).save(*args, **kwargs)

          for a in self._amenity_list:
            #add actually does a save internally, hitting the db
            self.amenities.add(a)

          serializer = JSONSerializer()

          for event in self._uncommitted_events:
            #we don't need to store the instance because it's not really part of the parameters
            #and django-reversion will keep a snapshop
            kwargs_to_save = {k: v for k, v in event.kwargs.items() if k != 'instance'}
            data = serializer.serialize(kwargs_to_save)

            reversion.add_meta(RevisionEvent, name=event.event_fq_name, version=event.version, data=data)

      self.send_events()
    else:
      from nextlanding_api.aggregates.search.services import search_service

      search_service.save_or_update(self)

  def __unicode__(self):
    return 'Search #' + str(self.pk) + ': ' + self.formatted_address


class Amenity(models.Model):
  search = models.ForeignKey(Search, related_name='amenities')
  amenity_type = models.ForeignKey('amenity.Amenity', related_name='search_instance')

  class Meta:
    unique_together = ("search", "amenity_type")
