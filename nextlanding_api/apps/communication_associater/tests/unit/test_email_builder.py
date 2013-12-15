from mock import MagicMock
import pytest
from nextlanding_api.aggregates.listing.models import Listing
from nextlanding_api.apps.communication_associater.availability.email.services.availability_email_builder import \
  AvailabilityEmailBuilder


@pytest.mark.parametrize(("input_contact_name", "expected_contact_name"), [
  (None, None),
  ("Markus Crassus", "Markus"),
])
def test_email_service_creates_contact_name(input_contact_name, expected_contact_name):
  mock_listing = MagicMock(spec=Listing)
  mock_listing.contact_name = input_contact_name
  builder = AvailabilityEmailBuilder()
  builder.listing = mock_listing
  assert expected_contact_name == builder._get_contact_name()
