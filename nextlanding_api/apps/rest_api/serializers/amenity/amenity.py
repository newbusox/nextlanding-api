from rest_framework import serializers
from nextlanding_api.aggregates.amenity.models import Amenity


class AmenitySerializer(serializers.ModelSerializer):
  class Meta:
    model = Amenity
