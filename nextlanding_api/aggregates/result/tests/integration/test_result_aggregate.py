from django.utils import timezone
import pytest
from nextlanding_api.aggregates.apartment.services import apartment_service
from nextlanding_api.aggregates.availability.models import Availability
from nextlanding_api.aggregates.listing.models import Listing
from nextlanding_api.aggregates.listing.services import listing_service
from nextlanding_api.aggregates.result.models import Result
from nextlanding_api.aggregates.result.services import result_service
from nextlanding_api.aggregates.result.tests import result_test_data
from nextlanding_api.aggregates.search.models import Search
from nextlanding_api.aggregates.search.services import search_service


@pytest.mark.django_db_with_migrations
def test_result_is_created_from_attrs():
  listing_id = listing_service.create_listing(**result_test_data.cl_listing_4033538277).id

  search_id = search_service.create_search(**result_test_data.search_1).id

  listing = Listing.objects.get(pk=listing_id)

  apartment = listing.apartment

  search = Search.objects.get(pk=search_id)

  result_id = result_service.create_result(apartment, search).id

  result = Result.objects.get(pk=result_id)

  assert 1 == Result.objects.count()


@pytest.mark.django_db_with_migrations
def test_result_notified_unavailable_updates_apartment_and_listings():
  listing_id = listing_service.create_listing(**result_test_data.cl_listing_4033538277).id

  search_id = search_service.create_search(**result_test_data.search_1).id

  listing = Listing.objects.get(pk=listing_id)

  apartment = listing.apartment

  search = Search.objects.get(pk=search_id)

  result_id = result_service.create_result(apartment, search).id

  result = Result.objects.get(pk=result_id)

  result.add_availability_response('This is a test', timezone.now(), Availability.objects.get_unavailable_type())

  result_service.save_or_update(result)

  apartment = apartment_service.get_apartment(apartment.pk)

  assert apartment.is_available == False

  listings = apartment.listings.values_list('is_deleted', flat=True)

  assert all(f == True for f in listings)
