from rest_framework import serializers
from nextlanding_api.apps.domain.search.models import PotentialSearch


class PotentialSearchSerializer(serializers.ModelSerializer):
  class Meta:
    model = PotentialSearch
    fields = ('id', 'search_attrs', 'purchased')
