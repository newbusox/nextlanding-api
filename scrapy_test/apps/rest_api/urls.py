from rest_framework import routers
from django.conf.urls import patterns, include, url
from scrapy_test.apps.rest_api.views.communication.email import CommunicationEmailView
from scrapy_test.apps.rest_api.views.search.add_apartments import AddApartmentsConfigView, AddApartmentsView

from scrapy_test.apps.rest_api.views.amenity.amenity import AmenityViewSet
from scrapy_test.apps.rest_api.views.search.emailer_sender import EmailerSenderView
from scrapy_test.apps.rest_api.views.search.potential_search import PotentialSearchViewSet

# our consumer, in this case, restangular, doesn't conventionally append a '/' suffix, so it's just easier to disable
# the expectation on this side.
from scrapy_test.apps.rest_api.views.search.results import SearchResultsView

router = routers.DefaultRouter(trailing_slash=False)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
router.register('potential_search', PotentialSearchViewSet)
router.register('amenity', AmenityViewSet)


# region search views
potential_search_init = PotentialSearchViewSet.as_view({
  'get': 'resume_init',
  'post': 'create_init',
  'put': 'update_init',
})

potential_search_complete = PotentialSearchViewSet.as_view({
  'post': 'complete_init',
})

add_apartments= AddApartmentsView.as_view()
add_apartments_config = AddApartmentsConfigView.as_view()

search_results= SearchResultsView.as_view()
# endregion

# region communication views
communication_email = CommunicationEmailView.as_view()
# endregion

urlpatterns = patterns(
  '',
  url(r'^', include(router.urls)),
  url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework')),
  url(r'^search/potential_search_init$', potential_search_init, name="potential_search_init"),
  url(r'^search/potential_search_complete$', potential_search_complete, name="potential_search_complete"),
  url(r'^search/(?P<pk>[0-9]+)/emailer_sender$', EmailerSenderView.as_view(), name="emailer-sender"),
  url(r'^search/(?P<pk>[0-9]+)/apartments$', add_apartments, name="add-apartments"),
  url(r'^search/(?P<pk>[0-9]+)/add_apartments_config$', add_apartments_config, name="add-apartments-config"),
  url(r'^search/(?P<pk>[0-9]+)/results$', search_results, name="search-results"),
  url(r'^communication/email/$', communication_email, name="communication-email"),
)
