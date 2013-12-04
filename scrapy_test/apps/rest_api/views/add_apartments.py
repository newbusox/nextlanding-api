from rest_framework.response import Response
from rest_framework.views import APIView
from scrapy_test.aggregates.search.services import search_service


class AddApartmentsConfigView(APIView):
  """
  API endpoint for getting add apartment parameters.
  """

  def get(self, request, *args, **kwargs):
    ret_val = {}
    pk = kwargs['pk']

    search = search_service.get_search(pk)

    ret_val['days_back'] = 7
    ret_val['distance'] = 2
    ret_val['fees_allowed'] = not search.no_fee_preferred
    ret_val['cats_required'] = bool(search.amenities.filter(amenity_type__name='Cats').count())
    ret_val['dogs_required'] = bool(search.amenities.filter(amenity_type__name='Dogs').count())
    ret_val['price_min'] = search.price_min or 0
    ret_val['price_max'] = search.price_max or 5000
    ret_val['bedroom_min'] = search.bedroom_min or 0
    ret_val['bedroom_max'] = search.bedroom_max or 3
    ret_val['bathroom_min'] = search.bathroom_min or 1
    ret_val['bathroom_max'] = search.bathroom_max or 3

    return Response(ret_val)


class AddApartmentsView(APIView):
  """
  API endpoint for getting add apartment parameters.
  """

  def get(self, request, *args, **kwargs):
    days_back = request.QUERY_PARAMS['days_back']
    distance = request.QUERY_PARAMS['distance']
    fees_allowed = request.QUERY_PARAMS['fees_allowed']
    cats_required = request.QUERY_PARAMS['cats_required']
    dogs_required = request.QUERY_PARAMS['dogs_required']
    price_min = request.QUERY_PARAMS['price_min']
    price_max = request.QUERY_PARAMS['price_max']
    bedroom_min = request.QUERY_PARAMS['bedroom_min']
    bedroom_max = request.QUERY_PARAMS['bedroom_max']
    bathroom_min = request.QUERY_PARAMS['bathroom_min']
    bathroom_min = request.QUERY_PARAMS['bathroom_max']

    return Response()
