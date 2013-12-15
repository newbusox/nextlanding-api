from rest_framework import serializers
from nextlanding_api.apps.domain.apartment.models import AddApartmentToSearch


class AddApartmentToSearchSerializer(serializers.ModelSerializer):
  class Meta:
    model = AddApartmentToSearch
