import pytest
from nextlanding_api.apps.marketing.enums import ProductEnum
from nextlanding_api.apps.marketing.models import MarketingEmailAccount
from nextlanding_api.apps.marketing.tests.email_test_data import email_2
from nextlanding_api.libs.communication_utils.models import Email


@pytest.mark.django_db_with_migrations
def test_correspondence_is_created_from_post(client, settings):
  #needed to print emails
  settings.DEBUG = True
  MarketingEmailAccount.objects.create(email_addresses='"Some Dude" <some_test_acct@markettest1.com>',
                                       product=ProductEnum.Search,
                                       ignore_keywords="Ignore me\nI'm to ignore"
  )

  response = client.post('/api/communication/email/', email_2)
  assert 2 == Email.objects.count()

