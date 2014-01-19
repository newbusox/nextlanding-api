from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.response import Response
from nextlanding_api.apps.domain.constants import POTENTIAL_SEARCH_SESSION_ID
from nextlanding_api.apps.domain.search.models import PotentialSearch
from nextlanding_api.apps.domain.search.services import potential_search_service
from nextlanding_api.apps.rest_api.serializers.search.potential_search import PotentialSearchSerializer
from nextlanding_api.libs.payment_utils.exceptions import ChargeError, InvalidCardError


class PotentialSearchViewSet(viewsets.ReadOnlyModelViewSet):
  """
  API endpoint that allows potential searches to be retrieved or updated.
  """
  model = PotentialSearch
  serializer_class = PotentialSearchSerializer

  def resume_init(self, request, *args, **kwargs):
    potential_search_id = request.session.get(POTENTIAL_SEARCH_SESSION_ID)

    if potential_search_id:
      potential_search = potential_search_service.get_potential_search(potential_search_id)

      serializer = PotentialSearchSerializer(instance=potential_search)

      ret_val = Response(serializer.data)
    else:
      ret_val = Response()

    return ret_val

  def update_init(self, request, *args, **kwargs):
    potential_search_id = request.session.get(POTENTIAL_SEARCH_SESSION_ID)

    if not potential_search_id: raise Http404

    try:
      potential_search = potential_search_service.get_potential_search(potential_search_id)
    except:
      raise Http404

    data = potential_search_service.get_search_attrs(request.DATA['search_attrs'])

    potential_search.search_attrs = data
    potential_search_service.save_or_update(potential_search)

    serializer = PotentialSearchSerializer(instance=potential_search)

    return Response(serializer.data)


  def create_init(self, request, *args, **kwargs):
    data = potential_search_service.get_search_attrs(request.DATA['search_attrs'])

    potential_search = PotentialSearch(search_attrs=data)

    potential_search_service.save_or_update(potential_search)

    serializer = PotentialSearchSerializer(instance=potential_search)

    request.session[POTENTIAL_SEARCH_SESSION_ID] = potential_search.id

    return Response(serializer.data, status=status.HTTP_201_CREATED)


  def complete_init(self, request, *args, **kwargs):
    potential_search_id = request.session.get(POTENTIAL_SEARCH_SESSION_ID)
    token = request.DATA['token']

    if not potential_search_id: raise Http404

    try:
      potential_search = potential_search_service.get_potential_search(potential_search_id)
    except:
      raise Http404

    #this will call save internally
    try:
      potential_search_service.complete_potential_search(potential_search, token)
    except (ChargeError, InvalidCardError) as e:
      ret_val = Response("Invalid payment.", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
      serializer = PotentialSearchSerializer(instance=potential_search)

      ret_val = Response(serializer.data)

    return ret_val
