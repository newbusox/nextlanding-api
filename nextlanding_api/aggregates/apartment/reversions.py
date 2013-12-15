import reversion
from nextlanding_api.aggregates.apartment.models import Apartment, Amenity

reversion.register(Apartment, follow=['amenities'])
reversion.register(Amenity)
