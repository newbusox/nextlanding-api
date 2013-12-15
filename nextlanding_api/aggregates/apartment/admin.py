from django.contrib import admin
from nextlanding_api.aggregates.apartment.models import Apartment, Amenity
from nextlanding_api.aggregates.listing.models import Listing


class ListingInline(admin.TabularInline):
  model = Listing
  max_num = 0


class AmenityInline(admin.StackedInline):
  model = Amenity
  max_num = 0


class ApartmentAdmin(admin.ModelAdmin):
  inlines = [
    ListingInline,
    AmenityInline,
  ]


admin.site.register(Apartment, ApartmentAdmin)
