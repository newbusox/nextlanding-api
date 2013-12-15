import reversion
from nextlanding_api.aggregates.availability.models import Availability

reversion.register(Availability)
