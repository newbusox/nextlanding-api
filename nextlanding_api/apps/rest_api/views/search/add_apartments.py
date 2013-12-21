import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from nextlanding_api.aggregates.apartment.services import apartment_service
from nextlanding_api.aggregates.search.services import search_service
from nextlanding_api.apps.domain.apartment.services import add_apartment_to_search_service
from nextlanding_api.apps.domain.search.services import search_location_service
from nextlanding_api.apps.rest_api.serializers.search.add_apartment_to_search import AddApartmentToSearchSerializer

logger = logging.getLogger(__name__)


class AddApartmentsConfigView(APIView):
  """
  API endpoint for getting add apartment parameters.
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
      search_param.update(add_apartment_to_search_service.get_search_default_params(search))

      search_param['description'] = search.description
      search_param['address'] = search_location_service.get_location_for_search(search)

      if search.geo_boundary_points:
        search_param['geo_boundary_points'] = search.geo_boundary_points

      response = Response(search_param)

    return response


class AddApartmentsView(APIView):
  """
  API endpoint for adding apartments to search.
  """

  def get(self, request, *args, **kwargs):
    pk = kwargs['pk']

    response = None

    try:
      search = search_service.get_search(pk)
    except:
      logger.debug("Error getting search: {0}".format(pk))
      response = Response(status=status.HTTP_404_NOT_FOUND)
    else:
      apartments = add_apartment_to_search_service.get_apartments_for_search(search, **request.QUERY_PARAMS.dict())
      serializer = AddApartmentToSearchSerializer(apartments)
      response = Response(serializer.data)

    return response

  def post(self, request, *args, **kwargs):
    pk = kwargs['pk']
    search = search_service.get_search(pk)

    apartment_id = request.DATA['apartment_aggregate_id']

    apartment = apartment_service.get_apartment(apartment_id)

    add_apartment_to_search_service.add_apartment_to_search(search, apartment)

    return Response(status=status.HTTP_201_CREATED)
