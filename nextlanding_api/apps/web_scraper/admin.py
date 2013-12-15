from django.contrib import admin
from dynamic_scraper.admin import ScraperElemInline
from nextlanding_api.apps.web_scraper.models import ListingSourceScraperConfig, ListingCheckerConfig

admin.site.register(ListingSourceScraperConfig)
admin.site.register(ListingCheckerConfig)

#ensure the pk field is shown
ScraperElemInline.readonly_fields = ('pk',)
