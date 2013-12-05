from django.db import models, transaction
from jsonfield import JSONField
from localflavor.us.models import PhoneNumberField
from scrapy_test.libs.django_utils.fields.list_field import ListField


class AddApartmentToSearch(models.Model):
  #this represents the model to be used for adding apts to a search

  #do not use foreign keys for aggregates
  apartment_aggregate_id = models.IntegerField()

  #can this apt be searched and used to be added to a search?
  is_available = models.BooleanField()

  lat = models.FloatField()
  lng = models.FloatField()
  changed_date = models.DateTimeField()
  broker_fee = models.BooleanField()
  cats_ok = models.BooleanField()
  dogs_ok = models.BooleanField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  bedroom_count = models.PositiveSmallIntegerField(max_length=2, blank=True, null=True)
  bathroom_count = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
  sqfeet = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)

  listing_urls = ListField()

  description = models.TextField()
  contact_name = models.CharField(max_length=255, blank=True, null=True)
  contact_phone_number = PhoneNumberField(blank=True, null=True)
  contact_email_address = models.EmailField(blank=True, null=True)

  amenities = JSONField(blank=True, null=True)

  class Meta:
    app_label = 'domain'

  def save(self, internal=False, *args, **kwargs):
    if internal:
      with transaction.commit_on_success():
        super(AddApartmentToSearch, self).save(*args, **kwargs)
    else:
      from scrapy_test.apps.domain.apartment.services import add_apartment_to_search_service

      add_apartment_to_search_service.save_or_update(self)

  def __unicode__(self):
    return 'AddApartmentToSearch #' + str(self.pk)
