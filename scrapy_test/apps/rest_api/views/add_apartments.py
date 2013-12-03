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
    ret_val['price_min'] = search.price_min
    ret_val['price_max'] = search.price_max
    ret_val['bedroom_min'] = search.bedroom_min
    ret_val['bedroom_max'] = search.bedroom_max
    ret_val['bathroom_min'] = search.bathroom_min
    ret_val['bathroom_max'] = search.bathroom_max

    return Response(ret_val)
