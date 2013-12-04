from scrapy_test.apps.domain.apartment.models import AddApartmentToSearch
from scrapy_test.apps.domain.search.models import SearchEmailerSender


def save_or_update(add_apartment_model):
  add_apartment_model.save(internal=True)


def get_apartment(pk):
  return SearchEmailerSender.objects.get(pk=pk)

def create_apartment(apartment_aggregate):
  ret_val = AddApartmentToSearch()

  save_or_update(ret_val)

  return ret_val
