from scrapy_test.apps.domain.apartment.models import AddApartmentToSearch
from scrapy_test.apps.domain.search.models import SearchEmailerSender


def save_or_update(add_apartment_model):
  add_apartment_model.save(internal=True)


def get_apartment(pk):
  return SearchEmailerSender.objects.get(pk=pk)


def create_apartment(apartment_aggregate):
  ret_val = AddApartmentToSearch(
    lat=apartment_aggregate.lat,
    lng=apartment_aggregate.lng,
    changed_date=apartment_aggregate.changed_date,
    broker_fee=apartment_aggregate.broker_fee,
    cats_required=bool(apartment_aggregate.amenities.filter(amenity_type__name='Cats').count()),
    dogs_required=bool(apartment_aggregate.amenities.filter(amenity_type__name='Dogs').count()),
    price=apartment_aggregate.price,
    bedroom_count=apartment_aggregate.bedroom_count,
    bathroom_count=apartment_aggregate.bathroom_count,
    sqfeet=apartment_aggregate.sqfeet
  )

  save_or_update(ret_val)

  return ret_val
