from urlparse import urlparse
from nextlanding_api.aggregates.listing_source.models import ListingSource
from nextlanding_api.apps.web_scraper.spiders.individual_item_spider import IndividualItemSpider
from nextlanding_api.apps.web_scraper.spiders.listing_spider import ListingSpider
from nextlanding_api.libs.text_utils.search import fuzzy_search


class IndividualListingSpider(IndividualItemSpider, ListingSpider):
  name = 'individual_listing_spider'

  def __init__(self, *args, **kwargs):
    #hack process based utils expects id to be a primary key, but we're passing in a url
    #if we just passed in url, processbased utils would not forward it onto the crawler process

    url = kwargs['id']

    #get the root domain - but this is pretty naive. consider
    #https://github.com/john-kurkowski/tldextract
    netloc_split = urlparse(url).netloc.split(".")
    if 'www' in netloc_split:
      domain = netloc_split[1]
    else:
      domain = netloc_split[0]

    listing_sources = ListingSource.objects.filter(url__icontains=domain).all()

    if not listing_sources and len(netloc_split) >= 3:
      # this is a temp fix to get the next generic source in line
      domain = netloc_split[1]
      listing_sources = ListingSource.objects.filter(url__icontains=domain).all()

    if not listing_sources:
      raise Exception(u"url: {0} is not valid".format(url))
    source_dict = {k.url: k for k in listing_sources}

    closest_url = fuzzy_search.get_closest_word(url, source_dict.keys())

    config = source_dict[closest_url].scraper_config

    self.scraper = config.scraper
    self.scrape_url = url
    self.ref_object = config

    super(IndividualListingSpider, self).__init__(*args, **kwargs)

  def _set_start_urls(self, scrape_url):
    self.start_urls.append(scrape_url)
