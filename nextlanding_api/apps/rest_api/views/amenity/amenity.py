from rest_framework import viewsets
from nextlanding_api.aggregates.amenity.models import Amenity
from nextlanding_api.apps.rest_api.serializers.amenity.amenity import AmenitySerializer


class AmenityViewSet(viewsets.ReadOnlyModelViewSet):
  """
  API endpoint that allows potential searches to be retrieved or updated.
  """
  model = Amenity
  serializer_class = AmenitySerializer
  paginate_by = None
