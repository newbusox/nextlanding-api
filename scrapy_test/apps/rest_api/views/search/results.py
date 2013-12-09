from rest_framework.response import Response
from rest_framework.views import APIView
from scrapy_test.aggregates.search.services import search_service
from scrapy_test.apps.domain.result.services import search_result_service
from scrapy_test.apps.domain.search.services import search_location_service
from scrapy_test.apps.rest_api.serializers.search.search_result import SearchResultSerializer


class SearchResultsView(APIView):
  """
  API endpoint for viewing results.
  """

  def get(self, request, *args, **kwargs):
    ret_val = {}
    pk = kwargs['pk']

    search = search_service.get_search(pk)

    ret_val['address'] = search_location_service.get_location_for_search(search)

    ret_val['geo_boundary_points'] = search.geo_boundary_points

    results = search_result_service.get_results_from_search(search)

    serializer = SearchResultSerializer(results)

    ret_val["search_results"] = serializer.data

    return Response(ret_val)
