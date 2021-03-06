from django.contrib import admin
from nextlanding_api.aggregates.listing.models import Listing, Amenity


class AmenityInline(admin.StackedInline):
  model = Amenity
  max_num = 0


class ListingAdmin(admin.ModelAdmin):
  inlines = [
    AmenityInline,
  ]


admin.site.register(Listing, ListingAdmin)
