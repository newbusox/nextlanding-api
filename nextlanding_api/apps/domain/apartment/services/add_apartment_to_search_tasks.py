from celery import shared_task
from celery.exceptions import Ignore
from django.core.exceptions import ObjectDoesNotExist
from nextlanding_api.aggregates.apartment.services import apartment_service
from nextlanding_api.aggregates.listing.services import listing_service
from nextlanding_api.aggregates.search.services import search_service
from nextlanding_api.apps.domain.apartment.services import add_apartment_to_search_service
import logging
from nextlanding_api.libs.python_utils.errors.exceptions import log_ex_with_message

logger = logging.getLogger(__name__)


@shared_task
def update_apartment_from_listing_task(listing_id):
  listing = listing_service.get_listing(listing_id)

  return add_apartment_to_search_service.update_apartment_from_listing(listing).id


@shared_task
def disable_apartment_task(apartment_id):
  apartment = apartment_service.get_apartment(apartment_id)

  try:
    return add_apartment_to_search_service.disable_apartment(apartment).id
  except ObjectDoesNotExist as e:
    logger.warn(log_ex_with_message(u"Apartment to add doesn't exist: {0}".format(apartment_id), e))
    raise Ignore()


@shared_task
def add_apartment_to_search_task(search_id, apartment_id):
  search = search_service.get_search(search_id)
  apartment = apartment_service.get_apartment(apartment_id)
  add_apartment_to_search_service.add_apartment_to_search(search, apartment)
