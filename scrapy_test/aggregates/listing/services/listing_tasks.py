import logging
from celery.task import task
from scrapy_test.aggregates.apartment.services import apartment_service
from scrapy_test.aggregates.listing.services import listing_service
from scrapy_test.libs.python_utils.errors.exceptions import log_ex_with_message

logger = logging.getLogger(__name__)


@task
def create_listing_task(**listing_attrs):
  try:
    return listing_service.create_listing(**listing_attrs).id
  except Exception as e:
    logger.WARN(log_ex_with_message("Error creating listing", e))


@task
def update_listing_task(**listing_attrs):
  return listing_service.update_listing(**listing_attrs).id


@task
def kill_listing_task(listing_id):
  listing = listing_service.get_listing(listing_id)
  return listing_service.kill_listing(listing).id


@task
def associate_listing_with_apartment_task(listing_id, apartment_id):
  listing = listing_service.get_listing(listing_id)
  apartment = apartment_service.get_apartment(apartment_id)
  return listing_service.associate_listing_with_apartment(listing, apartment).id


@task
def notify_listings_unavailable_task(apartment_id):
  apartment = apartment_service.get_apartment(apartment_id)
  return listing_service.notify_listings_unavailable(apartment)
