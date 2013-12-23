import logging

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

from nextlanding_api.aggregates.search.models import Search
from nextlanding_api.apps.rest_api.serializers.search.search import SearchSerializer
from nextlanding_api.aggregates.search.services import search_service


logger = logging.getLogger(__name__)


class SearchViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows potential searches to be retrieved or updated.
  """
  model = Search
  serializer_class = SearchSerializer

  def update_geo(self, request, *args, **kwargs):
    search_param = {}
    pk = kwargs['pk']

    response = None

    try:
      search = search_service.get_search(pk)
    except:
      logger.debug("Error getting search: {0}".format(pk))
      response = Response(status=status.HTTP_404_NOT_FOUND)
    else:
      search_service.update_geo_boundary_points(search,request.DATA['geo_boundary_points'])
      response = Response()

    return response
