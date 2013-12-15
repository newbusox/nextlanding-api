from rest_framework import serializers
from nextlanding_api.apps.domain.result.models import SearchResult


class SearchResultSerializer(serializers.ModelSerializer):
  class Meta:
    model = SearchResult
