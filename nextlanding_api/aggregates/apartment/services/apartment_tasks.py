from celery import shared_task
from django.db import IntegrityError
from nextlanding_api.aggregates.apartment.services import apartment_service
from nextlanding_api.aggregates.listing.services import listing_service
import logging
from nextlanding_api.libs.python_utils.errors.exceptions import log_ex_with_message

logger = logging.getLogger(__name__)

@shared_task(bind=True)
def adopt_listing_task(self, listing_id):
  listing = listing_service.get_listing(listing_id)
  try:
    apartment_id = apartment_service.adopt_listing(listing).id
    return apartment_id
  except IntegrityError as e:
    logger.info(log_ex_with_message(u"Integrity error adopting listing", e))
    raise self.retry(exc=e)


@shared_task
def update_availability_task(listing_id):
  listing = listing_service.get_listing(listing_id)
  apartment = listing.apartment

  if apartment:
    apartment_service.update_availability(apartment)
  else:
    # This could happen if a listing was created, then marked as deleted, before the aparment was actually created
    logger.debug(u"Apartment didn't exist: {0}".format(listing))


@shared_task
def handle_result_notification_task(apartment_id, availability_type_system_name):
  apartment = apartment_service.get_apartment(apartment_id)
  apartment_service.handle_result_notification(apartment, availability_type_system_name)

