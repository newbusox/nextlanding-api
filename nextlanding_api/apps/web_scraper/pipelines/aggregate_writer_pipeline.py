import traceback
from scrapy import log
from scrapy.exceptions import DropItem
from nextlanding_api.aggregates.listing.services import listing_tasks
from nextlanding_api.apps.web_scraper.spiders.listing_spider import ListingSpider


class AggregateCommandPipeline(object):
  def process_item(self, item, spider):
    try:
      double = item['url'][0:6] == 'DOUBLE'
      if double:
        item['url'] = item['url'][6:]

      # if we get too many "if's" then we should do a "tell-don't-ask" pattern
      # but I don't think a spider should care about business logic
      # like if something should be updated vs created
      if isinstance(spider, ListingSpider):
        if double:
          listing_tasks.update_listing_task.delay(**item)
        else:
          listing_tasks.create_listing_task.delay(**dict(item, listing_source_id=spider.ref_object.listing_source.id))

      spider.action_successful = True
      spider.log("Item sent to application to be processed: {0}".format(item['url']), log.INFO)
    except:
      spider.log(traceback.format_exc(), log.ERROR)
      raise DropItem("Error sending item.")

    return item
