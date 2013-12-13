import logging
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from scrapy_test.aggregates.apartment.services import apartment_service
from scrapy_test.aggregates.search.services import search_service
from scrapy_test.apps.domain.apartment.services import add_apartment_to_search_service
from scrapy_test.apps.domain.search.services import search_location_service
from scrapy_test.apps.rest_api.serializers.search.add_apartment_to_search import AddApartmentToSearchSerializer

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
      #json encoding will convert any decimal to a string - we might as well just make it be an int
      #https://github.com/tomchristie/django-rest-framework/issues/508
      search_param['days_back'] = 7
      search_param['distance'] = 2
      search_param['fees_allowed'] = not search.no_fee_preferred
      search_param['cats_required'] = bool(search.amenities.filter(amenity_type__name='Cats Allowed').count())
      search_param['dogs_required'] = bool(search.amenities.filter(amenity_type__name='Dogs Allowed').count())
      search_param['price_min'] = int(search.price_min or 0)
      search_param['price_max'] = int(search.price_max or 5000)
      search_param['bedroom_min'] = search.bedroom_min or 0
      search_param['bedroom_max'] = search.bedroom_max or 3
      search_param['bathroom_min'] = int(search.bathroom_min or 1)
      search_param['bathroom_max'] = int(search.bathroom_max or 3)
      search_param['description'] = search.description

      search_param['address'] = search_location_service.get_location_for_search(search)

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
