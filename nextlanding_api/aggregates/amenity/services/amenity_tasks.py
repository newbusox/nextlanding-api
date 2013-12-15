from celery.task import task
from nextlanding_api.aggregates.apartment.services import apartment_service
from nextlanding_api.aggregates.listing.services import listing_service


@task
def associate_listing_with_apartment_task(listing_id):
  listing = listing_service.get_listing(listing_id)
  return apartment_service.associate_listing_with_apartment(listing).id
