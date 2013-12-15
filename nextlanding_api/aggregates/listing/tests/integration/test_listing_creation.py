import pytest
from nextlanding_api.aggregates.listing.models import Listing
from nextlanding_api.aggregates.listing.services import listing_service
from nextlanding_api.aggregates.listing.tests import listing_test_data

@pytest.mark.django_db_with_migrations
def test_listing_is_created_from_attrs():
  listing_id = listing_service.create_listing(**listing_test_data.cl_listing_4033538277).id
  listing = Listing.objects.get(pk=listing_id)
  assert 1 == Listing.objects.count()
