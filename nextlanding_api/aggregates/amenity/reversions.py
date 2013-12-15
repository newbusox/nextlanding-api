import reversion
from nextlanding_api.aggregates.amenity.models import Amenity

reversion.register(Amenity)
