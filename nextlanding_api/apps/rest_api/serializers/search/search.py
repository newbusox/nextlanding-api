from rest_framework import serializers
from nextlanding_api.aggregates.search.models import Search


class SearchSerializer(serializers.ModelSerializer):
  class Meta:
    model = Search
