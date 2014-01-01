import pytest
from nextlanding_api.apps.communication_associater.tests.email_test_data import email_2
from nextlanding_api.libs.communication_utils.models import Email


@pytest.mark.django_db_with_migrations
def test_email_is_created_from_post(client):
  response = client.post('/api/communication/email/', email_2)
  assert 1 == Email.objects.count()

