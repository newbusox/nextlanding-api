import textwrap
from mock import MagicMock
from scrapy_test.apps.communication_associater.availability.email.services import email_body_result_identifier_service, email_to_address_result_identifier_service
from scrapy_test.libs.communication_utils.models import Email

def test_email_result_body_gets_availability_identifier():
  text = textwrap.dedent("""\
  Hey this is some dude

  hope all is well

  res-id: 123

  Goodbye""")

  email = MagicMock(text=text, spec=Email)

  identifier = email_body_result_identifier_service.get_availability_identifier_from_email(email)

  assert 123 == identifier

def test_email_result_to_address_gets_availability_identifier():
  email = MagicMock(to_address="test-123@fakesite.com", spec=Email)

  identifier = email_to_address_result_identifier_service.get_availability_identifier_from_email(email)

  assert 123 == identifier
