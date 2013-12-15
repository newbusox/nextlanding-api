#pulling in other models so django/south picks them up as mentioned here:
#http://stackoverflow.com/a/6338719/173957
from nextlanding_api.apps.domain.search.admin import *
from nextlanding_api.apps.domain.apartment.admin import *
from nextlanding_api.apps.domain.result.admin import *
