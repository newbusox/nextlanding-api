import logging
from celery.exceptions import Ignore
from celery import shared_task
from django.db import IntegrityError
from nextlanding_api.aggregates.apartment.services import apartment_service
from nextlanding_api.aggregates.listing.exceptions import ListingBuilderError, ListingPersistError
from nextlanding_api.aggregates.listing.services import listing_service
from nextlanding_api.libs.python_utils.errors.exceptions import log_ex_with_message

logger = logging.getLogger(__name__)


@shared_task
def create_listing_task(**listing_attrs):
  logger.debug("Received listing params for creating: {0}".format(listing_attrs['url']))
  try:
    ret_val = listing_service.create_listing(**listing_attrs).id
    logger.debug("Finished listing creation: {0}".format(listing_attrs['url']))
    return ret_val
  except (ListingBuilderError, ListingPersistError) as e:
    logger.warn(log_ex_with_message(u"Error creating listing", e))
    raise Ignore()
  except IntegrityError as e:
    logger.warn(log_ex_with_message(u"Listing already exists", e))
    raise Ignore()


@shared_task
def update_listing_task(**listing_attrs):
  logger.debug(u"Received listing params for update: {0}".format(listing_attrs['url']))
  try:
    ret_val = listing_service.update_listing(**listing_attrs).id
    logger.debug(u"Finished listing update: {0}".format(listing_attrs['url']))
    return ret_val
  except Exception as e:
    logger.warn(log_ex_with_message(u"Error updating listing", e))
    raise Ignore()


@shared_task
def kill_listing_task(listing_id):
  listing = listing_service.get_listing(listing_id)
  return listing_service.kill_listing(listing).id


@shared_task
def associate_listing_with_apartment_task(listing_id, apartment_id):
  listing = listing_service.get_listing(listing_id)
  apartment = apartment_service.get_apartment(apartment_id)
  return listing_service.associate_listing_with_apartment(listing, apartment).id


@shared_task
def notify_listings_unavailable_task(apartment_id):
  apartment = apartment_service.get_apartment(apartment_id)
  return listing_service.notify_listings_unavailable(apartment)
