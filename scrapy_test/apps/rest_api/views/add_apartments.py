from rest_framework.response import Response
from rest_framework.views import APIView
from scrapy_test.aggregates.search.services import search_service
from scrapy_test.apps.domain.apartment.services import add_apartment_to_search_service


class AddApartmentsConfigView(APIView):
  """
  API endpoint for getting add apartment parameters.
  """

  def get(self, request, *args, **kwargs):
    ret_val = {}
    pk = kwargs['pk']

    search = search_service.get_search(pk)

    #json encoding will convert any decimal to a string - we might as well just make it be an int
    #https://github.com/tomchristie/django-rest-framework/issues/508
    ret_val['days_back'] = 7
    ret_val['distance'] = 2
    ret_val['fees_allowed'] = not search.no_fee_preferred
    ret_val['cats_required'] = bool(search.amenities.filter(amenity_type__name='Cats').count())
    ret_val['dogs_required'] = bool(search.amenities.filter(amenity_type__name='Dogs').count())
    ret_val['price_min'] = int(search.price_min or 0)
    ret_val['price_max'] = int(search.price_max or 5000)
    ret_val['bedroom_min'] = search.bedroom_min or 0
    ret_val['bedroom_max'] = search.bedroom_max or 3
    ret_val['bathroom_min'] = int(search.bathroom_min or 1)
    ret_val['bathroom_max'] = int(search.bathroom_max or 3)

    return Response(ret_val)


class AddApartmentsView(APIView):
  """
  API endpoint for getting add apartment parameters.
  """

  def get(self, request, *args, **kwargs):
    ret_val = {}
    pk = kwargs['pk']
    search = search_service.get_search(pk)

    apartments = add_apartment_to_search_service.get_apartments_for_search(search, **request.QUERY_PARAMS.dict())

    return Response()
