from email.utils import parseaddr
import re
from urlparse import urlparse
from nextlanding_api.apps.marketing import constants

cl_url_regex = re.compile("(?P<url>https?://(?:\S+)craigslist(?:\S+))")


def provide_correspondence_data(correspondence):
  from_address = parseaddr(correspondence.from_address)[1]

  if 'craigslist' in from_address.lower():
    match = cl_url_regex.search(correspondence.incoming_text)

    if match:
      cl_url = match.groups()[0]
      correspondence.data[constants.ASSOCIATED_URL] = cl_url

      parsed_uri = urlparse(cl_url)
      location = parsed_uri.netloc.split('.')[0]
      correspondence.data[constants.GEOGRAPHIC_REGION] = location

  return correspondence
