from dynamic_scraper.spiders.django_spider import DjangoSpider
from scrapy.item import BaseItem


class IndividualItemSpider(DjangoSpider):
  def parse(self, response):
    url_elem = self.scraper.get_detail_page_url_elem()

    if 'item' not in response.meta:
      #the loader in the DJspider class expects a dict to populate
      response.meta['item'] = self.scraped_obj_item_class()

    item = self.parse_item(response)

    if isinstance(item, BaseItem):
      url_name = url_elem.scraped_obj_attr.name
      if item:
        item[url_name] = response.url
        cnt = self.scraped_obj_class.objects.filter(url=item[url_name]).count()
        # Mark item as DOUBLE item
        if cnt > 0:
          item[url_name] = 'DOUBLE' + item[url_name]
        yield item
    else:
      item.callback = self.parse
      yield item

  def spider_closed(self):
    #hack: we don't want to have our individual scraping change the scheduling of a normal spider
    pass
