from celery import shared_task
from nextlanding_api.aggregates.apartment.services import apartment_service
from nextlanding_api.aggregates.listing.services import listing_service


@shared_task
def associate_listing_with_apartment_task(listing_id):
  listing = listing_service.get_listing(listing_id)
  return apartment_service.associate_listing_with_apartment(listing).id
