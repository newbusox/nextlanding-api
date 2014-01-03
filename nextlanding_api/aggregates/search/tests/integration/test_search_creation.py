import pytest
from nextlanding_api.aggregates.search.models import Search
from nextlanding_api.aggregates.search.services import search_service
from nextlanding_api.aggregates.search.tests import search_test_data


@pytest.mark.django_db_with_migrations
def test_search_is_created_from_attrs(settings):
  #needed to print emails
  settings.DEBUG = True

  search_id = search_service.create_search(**search_test_data.search_1).id
  search = Search.objects.get(pk=search_id)
  assert 1 == Search.objects.count()
