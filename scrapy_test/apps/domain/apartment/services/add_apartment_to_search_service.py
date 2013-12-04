from django.utils import timezone
from scrapy_test.apps.domain.apartment.models import AddApartmentToSearch


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
