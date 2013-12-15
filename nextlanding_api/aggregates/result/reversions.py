import reversion
from nextlanding_api.aggregates.result.models import Result

reversion.register(Result)
