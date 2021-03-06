import logging
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.utils import timezone
from nextlanding_api.aggregates.search import factories, constants
from nextlanding_api.aggregates.search.models import Search
from nextlanding_api.libs.communication_utils.services import email_sender_async
from nextlanding_api.libs.geo_utils.services import geo_location_service

logger = logging.getLogger(__name__)


def create_search(_geo_location_service=geo_location_service, **search_attrs):
  specified_location = search_attrs.get('specified_location', None)

  if not specified_location: raise TypeError('specified location is required')

  geocoded_address = _geo_location_service.get_geocoded_address(specified_location)

  search_attrs['address'] = geocoded_address.address1
  search_attrs['city'] = geocoded_address.city
  search_attrs['state'] = geocoded_address.state
  search_attrs['zip_code'] = geocoded_address.zip_code
  search_attrs['formatted_address'] = geocoded_address.formatted_address
  search_attrs['lat'] = geocoded_address.lat
  search_attrs['lng'] = geocoded_address.lng

  search = factories.construct_search(**search_attrs)

  save_or_update(search)

  return search


def save_or_update(search):
  search.save(internal=True)


def get_search(search_id):
  return Search.objects.get(pk=search_id)


def update_geo_boundary_points(search, geo_boundary_points):
  search.update_geo_boundary_points(geo_boundary_points)
  save_or_update(search)


def send_client_results_email(search_id, _email_service=email_sender_async):
  search = get_search(search_id)

  # send in 1 hour
  now = timezone.now()
  email_schedule_date = now + relativedelta(minutes=60)

  _email_service.send_email(
    settings.PUBLIC_EMAIL[1],
    settings.PUBLIC_EMAIL[0],
    search.email_address,
    constants.CLIENT_RESULTS_SUBJECT_TEMPLATE,
    constants.CLIENT_RESULTS_BODY_TEMPLATE.format(search_id),
    search,
    email_schedule_date
  )

def notify_search_purchase(search, _email_service=email_sender_async):
  _email_service.send_email(
    settings.SYSTEM_EMAIL[1],
    settings.SYSTEM_EMAIL[0],
    settings.ADMIN_EMAIL[1],
    "New Search Created",
    "Search: {0} was created".format(search.pk),
    search
  )

  _email_service.send_email(
    settings.PUBLIC_EMAIL[1],
    settings.PUBLIC_EMAIL[0],
    search.email_address,
    constants.BUYER_PURCHASE_SUBJECT_TEMPLATE,
    constants.BUYER_PURCHASE_BODY_TEMPLATE,
    search
  )

  return search
