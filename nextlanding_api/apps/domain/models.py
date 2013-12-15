#pulling in other models so django/south picks them up as mentioned here:
#http://stackoverflow.com/a/6338719/173957
from nextlanding_api.apps.domain.search.models import *
from nextlanding_api.apps.domain.apartment.models import *
from nextlanding_api.apps.domain.result.models import *
