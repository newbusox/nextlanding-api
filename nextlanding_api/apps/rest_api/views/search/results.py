import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from nextlanding_api.aggregates.search.services import search_service
from nextlanding_api.apps.domain.result.services import search_result_service
from nextlanding_api.apps.domain.search.services import search_location_service
from nextlanding_api.apps.rest_api.serializers.search.search_result import SearchResultSerializer

logger = logging.getLogger(__name__)

class SearchResultsView(APIView):
  """
  API endpoint for viewing results.
  """

  def get(self, request, *args, **kwargs):
    search_param = {}
    pk = kwargs['pk']

    response = None

    try:
      search = search_service.get_search(pk)
    except:
      logger.debug("Error getting search: {0}".format(pk))
      response = Response(status=status.HTTP_404_NOT_FOUND)
    else:
      search_param['address'] = search_location_service.get_location_for_search(search)

      if search.geo_boundary_points:
        search_param['geo_boundary_points'] = search.geo_boundary_points

      results = search_result_service.get_results_from_search(search)

      serializer = SearchResultSerializer(results)

      search_param["search_results"] = serializer.data

      response = Response(search_param)

    return response
