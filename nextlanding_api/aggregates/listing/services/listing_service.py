from decimal import InvalidOperation
from django.db import DatabaseError
from nextlanding_api.aggregates.listing.domain.listing_builder import ListingBuilder
from nextlanding_api.aggregates.listing.exceptions import ListingPersistError
from nextlanding_api.aggregates.listing.models import Listing
from nextlanding_api.libs.datetime_utils.parsers import datetime_parser
from nextlanding_api.libs.python_utils.errors.exceptions import re_throw_ex


def get_listing(pk):
  return Listing.objects.get(pk=pk)


def get_listing_by_url(url):
  return Listing.objects.get(url=url)


def create_listing(**listing_attrs):
  builder = ListingBuilder(**listing_attrs)
  listing = builder.build_listing()
  try:
    save_or_update(listing)
  except (InvalidOperation, DatabaseError) as e:
    throw_ex = re_throw_ex(
      ListingPersistError, u"Error persisting listing: {0}".format(listing.url), e
    )
    raise throw_ex[0], throw_ex[1], throw_ex[2]

  return listing


def update_listing(**listing_attrs):
  url = listing_attrs['url']
  listing = get_listing_by_url(url)

  last_updated_date = listing_attrs.get('last_updated_date')

  if last_updated_date:
    listing.update_last_updated_date(datetime_parser.get_datetime(last_updated_date[0]))
    save_or_update(listing)

  return listing


def kill_listing(listing):
  listing.make_dead()

  save_or_update(listing)

  return listing


def save_or_update(listing):
  listing.save(internal=True)


def associate_listing_with_apartment(listing, apartment):
  listing.associate_with_apartment(apartment)
  save_or_update(listing)
  return listing


def notify_listings_unavailable(apartment):
  for listing in apartment.listings.all():
    listing.notify_unavailable()

    save_or_update(listing)
