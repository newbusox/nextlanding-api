import datetime
from django.utils import timezone
from scrapy_test.apps.domain.apartment.models import AddApartmentToSearch
from scrapy_test.libs.geo_utils.services.geo_distance_service import km_distance


def save_or_update(add_apartment_model):
  add_apartment_model.save(internal=True)


def get_apartment(pk):
  return AddApartmentToSearch.objects.get(pk=pk)


def create_apartment(apartment_aggregate):
  ret_val = AddApartmentToSearch(
    apartment_aggregate_id=apartment_aggregate.pk,
    lat=apartment_aggregate.lat,
    lng=apartment_aggregate.lng,
    changed_date=apartment_aggregate.changed_date,
    broker_fee=apartment_aggregate.broker_fee,
    cats_ok=bool(apartment_aggregate.amenities.filter(amenity_type__name='Cats').count()),
    dogs_ok=bool(apartment_aggregate.amenities.filter(amenity_type__name='Dogs').count()),
    price=apartment_aggregate.price,
    bedroom_count=apartment_aggregate.bedroom_count,
    bathroom_count=apartment_aggregate.bathroom_count,
    sqfeet=apartment_aggregate.sqfeet,
    is_available=True
  )

  save_or_update(ret_val)

  return ret_val


def update_apartment(apartment_aggregate):
  apartment_search_model = get_apartment(apartment_aggregate.pk)

  apartment_search_model.changed_date = apartment_aggregate.changed_date
  apartment_search_model.is_available = apartment_aggregate.is_available

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

  search_geo = (search.lat, search.lng)

  #doing the filtering before all the prefetching is much faster.
  #however, we should actually be doing th distance filter in the db
  apartments_to_lookup = [
    a[0] for a in apartments if
    a[0] not in apartments_to_filter and km_distance(search_geo, (a[1], a[2])) <= distance
  ]

  apartments = AddApartmentToSearch.objects.filter(apartment_aggregate_id__in=apartments_to_lookup)

  return apartments
