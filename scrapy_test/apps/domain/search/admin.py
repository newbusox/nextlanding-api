from django.contrib import admin
from scrapy_test.apps.domain.search.models import PotentialSearch, SearchEmailerSender

admin.site.register(PotentialSearch)
admin.site.register(SearchEmailerSender)
