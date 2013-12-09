from rest_framework import serializers
from scrapy_test.aggregates.result.models import Result


class SearchResultSerializer(serializers.ModelSerializer):
  class Meta:
    model = Result
