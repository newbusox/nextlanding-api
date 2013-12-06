import datetime
from django.db import IntegrityError
from django.utils import timezone
from scrapy_test.apps.domain.apartment.models import AddApartmentToSearch
from scrapy_test.libs.geo_utils.services.geo_distance_service import km_distance
import logging

logger = logging.getLogger(__name__)


def save_or_update(add_apartment_model):
  add_apartment_model.save(internal=True)


def get_search_add_apartment_from_aggregate(apartment_aggregate_id):
  return AddApartmentToSearch.objects.get(apartment_aggregate_id=apartment_aggregate_id)


def _update_with_newest_listing(apartment_search_model, listing):
  apartment_search_model.description = listing.description
  apartment_search_model.contact_name = listing.contact_name
  apartment_search_model.contact_phone_number = listing.contact_phone_number
  apartment_search_model.contact_email_address = listing.contact_email_address

  apartment_search_model.listing_urls.append(listing.url)


def _create_search_apartment_from_aggregate(apartment_aggregate):
  ret_val = AddApartmentToSearch(
    apartment_aggregate_id=apartment_aggregate.pk,
    address=apartment_aggregate.address,
    lat=apartment_aggregate.lat,
    lng=apartment_aggregate.lng,
    changed_date=apartment_aggregate.changed_date,
    broker_fee=apartment_aggregate.broker_fee,
    cats_ok=bool(apartment_aggregate.amenities.filter(amenity_type__name='Cats Allowed').count()),
    dogs_ok=bool(apartment_aggregate.amenities.filter(amenity_type__name='Dogs Allowed').count()),
    price=apartment_aggregate.price,
    bedroom_count=apartment_aggregate.bedroom_count,
    bathroom_count=apartment_aggregate.bathroom_count,
    sqfeet=apartment_aggregate.sqfeet,
  )
  return ret_val


def update_apartment_from_listing(listing_aggregate):
  apartment_aggregate = listing_aggregate.apartment

  try:
    ret_val = get_search_add_apartment_from_aggregate(apartment_aggregate.pk)
  except:
    ret_val = _create_search_apartment_from_aggregate(apartment_aggregate)

  ret_val.changed_date = apartment_aggregate.changed_date
  ret_val.is_available = apartment_aggregate.is_available

  ret_val.amenities = {
    x.amenity_type.name: {"is_available": x.is_available} for x in apartment_aggregate.amenities.all()
  }

  _update_with_newest_listing(ret_val, listing_aggregate)

  try:
    save_or_update(ret_val)
  except IntegrityError:
    # There is a potential case where two listings are associated w/ an apartment at the same time. In this case,
    # they'll both try to update the apartment. For now, whoever is first will win. That is probably good enough

    logger.info(
      "{0} tried to create a search_add_apartment model for {1} but it already existed"
      .format(listing_aggregate, apartment_aggregate)
    )

  return ret_val


def disable_apartment(apartment_aggregate):
  apartment_search_model = get_search_add_apartment_from_aggregate(apartment_aggregate.pk)

  apartment_search_model.listing_urls = []

  save_or_update(apartment_search_model)

  return apartment_search_model


def get_apartments_for_search(search, **kwargs):
  """
  json encoding will convert any decimal to a string - we might as well just make it be an int
  https://github.com/tomchristie/django-rest-framework/issues/508
  """

  days_back = int(kwargs['days_back'])
  distance = int(kwargs['distance'])
  fees_allowed = bool(kwargs['fees_allowed'].lower() == 'true')
  cats_required = bool(kwargs['cats_required'].lower() == 'true')
  dogs_required = bool(kwargs['dogs_required'].lower() == 'true')
  price_min = int(kwargs['price_min'])
  price_max = int(kwargs['price_max'])
  bedroom_min = int(kwargs['bedroom_min'])
  bedroom_max = int(kwargs['bedroom_max'])
  bathroom_min = int(kwargs['bathroom_min'])
  bathroom_max = int(kwargs['bathroom_max'])

  apartments = (

    AddApartmentToSearch
    .objects
    .filter(is_available=True)
    .filter(changed_date__gte=timezone.now() - datetime.timedelta(days=days_back))
    .filter(price__range=(price_min, price_max))
    .filter(bedroom_count__range=(bedroom_min, bedroom_max))
    .filter(bathroom_count__range=(bathroom_min, bathroom_max))
    .values_list('id', 'lat', 'lng')
  )

  if not fees_allowed:
    apartments = apartments.exclude(broker_fee=True)

  if cats_required:
    apartments = apartments.filter(cats_ok=True)

  if dogs_required:
    apartments = apartments.filter(dogs_ok=True)

  #don't show apartments already tied to search
  results = search.results.all()

  #doing __contains__ in a queryset is super slow
  apartments_to_filter = [r.apartment_id for r in results]

  if search.geo_boundary_points:
    #use the first place they drew and if they didn't draw, take the geocoded search term
    first_geo_point = search.geo_boundary_points["0"][0]
    search_geo = (first_geo_point[0], first_geo_point[1])
  else:
    search_geo = (search.lat, search.lng)

  #doing the filtering before all the prefetching is much faster.
  #however, we should actually be doing th distance filter in the db
  apartments_to_lookup = [
    a[0] for a in apartments if
    a[0] not in apartments_to_filter and km_distance(search_geo, (a[1], a[2])) <= distance
  ]

  apartments = AddApartmentToSearch.objects.filter(apartment_aggregate_id__in=apartments_to_lookup)

  return apartments
