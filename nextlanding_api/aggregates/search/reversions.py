import reversion
from nextlanding_api.aggregates.search.models import Search, Amenity

reversion.register(Search, follow=['amenities'])
reversion.register(Amenity)
