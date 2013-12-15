import pytest
from nextlanding_api.aggregates.apartment.models import Amenity as ApartmentAmenity
from nextlanding_api.aggregates.listing.models import Listing
from nextlanding_api.aggregates.listing.services import listing_service
from nextlanding_api.aggregates.result.services import result_service
from nextlanding_api.aggregates.result.tests import result_test_data
from nextlanding_api.aggregates.search.services import search_service


@pytest.mark.django_db_with_migrations
def test_result_creates_correct_compliance_score():
  listing = listing_service.create_listing(**result_test_data.cl_listing_4033538277)
  listing = Listing.objects.get(pk=listing.id)

  apartment = listing.apartment

  apartment.amenities.add(ApartmentAmenity(amenity_type_id=1, is_available=True),
                          ApartmentAmenity(amenity_type_id=2, is_available=True),
                          ApartmentAmenity(amenity_type_id=3, is_available=False))

  search = search_service.create_search(**result_test_data.search_1)

  result = result_service.create_result(apartment, search)

  assert result.compliance_score == 60
