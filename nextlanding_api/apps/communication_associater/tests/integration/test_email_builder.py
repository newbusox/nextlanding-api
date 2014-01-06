from mock import patch
import pytest
from nextlanding_api.aggregates.listing.models import Listing
from nextlanding_api.aggregates.listing.services import listing_service
from nextlanding_api.aggregates.result.models import Result
from nextlanding_api.aggregates.result.services import result_service
from nextlanding_api.aggregates.search.models import Search
from nextlanding_api.aggregates.search.services import search_service
from nextlanding_api.apps.communication_associater.availability.email.constants import EMAIL_AVAILABILITY_IDENTIFIER_RE
from nextlanding_api.apps.communication_associater.availability.email.email_objects import SearchSpecificEmailMessageRequest

from nextlanding_api.apps.communication_associater.availability.email.services.availability_email_builder import \
  AvailabilityEmailBuilder
from nextlanding_api.apps.communication_associater.tests import email_test_data


@pytest.mark.django_db_with_migrations
def test_email_with_body_result_created_correctly(settings):
  #needed to print emails
  settings.DEBUG = True

  #patch decorator cannot be used with mock
  with patch('nextlanding_api.apps.communication_associater.availability.email.services.availability_email_builder'
             '.availability_from_email_address_domain', 'mytest.com'):
    listing_id = listing_service.create_listing(**email_test_data.cl_listing_4033538277).id

    search_id = search_service.create_search(**email_test_data.search_1).id

    listing = Listing.objects.get(pk=listing_id)

    apartment = listing.apartment

    search = Search.objects.get(pk=search_id)

    result_id = result_service.create_result(apartment, search).id

    result = Result.objects.get(pk=result_id)

    email_builder = AvailabilityEmailBuilder()
    search_specific_email_message_request = SearchSpecificEmailMessageRequest("Jim", "Hey this is a test subject",
                                                                              "Hey this is a test body")

    email_message = email_builder.get_availability_email_message(result, search_specific_email_message_request)

  assert EMAIL_AVAILABILITY_IDENTIFIER_RE.search(email_message.body)

@pytest.mark.django_db_with_migrations
def test_email_with_from_result_created_correctly(settings):
  #needed to print emails
  settings.DEBUG = True

  with patch('nextlanding_api.apps.communication_associater.availability.email.services.availability_email_builder'
             '.availability_from_email_address_domain', 'mytest.com'):
    listing_dict = dict(email_test_data.cl_listing_4033538277, **{'contact_email_address': [u'test@somesite.com']})

    listing_id = listing_service.create_listing(**listing_dict).id

    search_id = search_service.create_search(**email_test_data.search_1).id

    listing = Listing.objects.get(pk=listing_id)

    apartment = listing.apartment

    search = Search.objects.get(pk=search_id)

    result_id = result_service.create_result(apartment, search).id

    result = Result.objects.get(pk=result_id)

    email_builder = AvailabilityEmailBuilder()
    search_specific_email_message_request = SearchSpecificEmailMessageRequest("Jim", "Hey this is a test subject",
                                                                              "Hey this is a test body")

    email_message = email_builder.get_availability_email_message(result, search_specific_email_message_request)

  assert "Jim-{0}@mytest.com".format(result_id) == email_message.from_address
