from rest_framework import serializers
from scrapy_test.apps.domain.search.models import PotentialSearch

class PotentialSearchSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = PotentialSearch