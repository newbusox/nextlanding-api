from email.parser import HeaderParser
from email.utils import parseaddr
import re
from urlparse import urlparse
from nextlanding_api.apps.marketing import constants
from nextlanding_api.apps.marketing.models import Correspondence

cl_url_regex = re.compile("(?P<url>https?://(?:\S+)craigslist(?:\S+))")


def construct_correspondence_from_email(email):
  correspondence = Correspondence(
    subject=email.subject,
    to=email.to,
    from_address=email.from_address,
    incoming_text=email.text,
    incoming_html=email.html
  )

  from_address = parseaddr(correspondence.from_address)[1]

  if 'craigslist' in from_address.lower():
    match = cl_url_regex.search(correspondence.incoming_text)

    if match:
      cl_url = match.groups()[0]
      correspondence.data[constants.ASSOCIATED_URL] = cl_url

      parsed_uri = urlparse(cl_url)
      location = parsed_uri.netloc.split('.')[0]
      correspondence.data[constants.GEOGRAPHIC_REGION] = location

    #craigslist is forwarding the true email to the Delivered-To header
    parser = HeaderParser()
    headers = parser.parsestr(email.headers)
    correspondence.to = headers['Delivered-To']

  return correspondence
