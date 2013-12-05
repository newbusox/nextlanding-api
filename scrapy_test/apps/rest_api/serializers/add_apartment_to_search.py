from rest_framework import serializers
from scrapy_test.apps.domain.apartment.models import AddApartmentToSearch


class AddApartmentToSearchSerializer(serializers.ModelSerializer):
  class Meta:
    model = AddApartmentToSearch
