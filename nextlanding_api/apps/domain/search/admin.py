from django.contrib import admin
from nextlanding_api.apps.domain.search.models import PotentialSearch, SearchEmailerSender

admin.site.register(PotentialSearch)
admin.site.register(SearchEmailerSender)
