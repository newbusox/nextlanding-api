import reversion
from nextlanding_api.aggregates.listing.models import Listing, Amenity

reversion.register(Listing, follow=['amenities'])
reversion.register(Amenity)
