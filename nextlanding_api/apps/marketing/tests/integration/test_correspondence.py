import pytest
from nextlanding_api.apps.marketing import constants
from nextlanding_api.apps.marketing.enums import DidNotRespondEnum, ProductEnum
from nextlanding_api.apps.marketing.models import Correspondence, MarketingEmailAccount
from nextlanding_api.apps.marketing.services import correspondence_service


@pytest.mark.django_db_with_migrations
def test_correspondence_duplicate_is_not_responded():
  MarketingEmailAccount.objects.create(email_addresses='"Some Dude" <some_test_acct@markettest1.com>',
                                       product=ProductEnum.Search
  )

  correspondence = Correspondence.objects.create(to='some_test_acct@markettest1.com', from_address='123asd2@test.com',
                                                 from_first_name='Dude',
                                                 from_last_name='Last Name', product=ProductEnum.Search, subject='test',
                                                 incoming_html='test',
                                                 incoming_text='test', outgoing_html='test', outgoing_text='test',
                                                 data={constants.GEOGRAPHIC_REGION: 'newyork'})

  correspondence.pk = 2
  correspondence.save()
  did_not_respond_reason = correspondence_service._validate_correspondence_response(correspondence)

  assert did_not_respond_reason == DidNotRespondEnum.AlreadyMessaged
