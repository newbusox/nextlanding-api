from rest_framework import serializers
from scrapy_test.apps.domain.result.models import SearchResult


class SearchResultSerializer(serializers.ModelSerializer):
  class Meta:
    model = SearchResult
