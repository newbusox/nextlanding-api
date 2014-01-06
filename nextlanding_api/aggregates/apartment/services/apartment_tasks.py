from celery.task import task
from django.db import IntegrityError
from nextlanding_api.aggregates.apartment.services import apartment_service
from nextlanding_api.aggregates.listing.services import listing_service
import logging
from nextlanding_api.libs.python_utils.errors.exceptions import log_ex_with_message

logger = logging.getLogger(__name__)

@task
def adopt_listing_task(listing_id):
  listing = listing_service.get_listing(listing_id)
  try:
    apartment_id = apartment_service.adopt_listing(listing).id
    return apartment_id
  except IntegrityError as e:
    logger.info(log_ex_with_message("Integrity error adopting listing", e))
    raise adopt_listing_task.retry(exc=e)


@task
def update_availability_task(listing_id):
  listing = listing_service.get_listing(listing_id)
  apartment = listing.apartment
  apartment_service.update_availability(apartment)


@task
def handle_result_notification_task(apartment_id, availability_type_system_name):
  apartment = apartment_service.get_apartment(apartment_id)
  apartment_service.handle_result_notification(apartment, availability_type_system_name)

