from scrapy.http import Request
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.item import Item, Field

# to run
# scrapy crawl azama -o myinfo.csv -t csv


class DmozSpider(BaseSpider):
  name = "azama"
  allowed_domains = ["azama.org"]
  start_urls = [
    "http://azama.org/looking-to-rent/",
  ]

  items = []
  pages = 3
  current_page = 1

  def parse(self, response):
    hxs = HtmlXPathSelector(response)
    sites = hxs.select("//div[@id='results']/table/tr")

    for site in sites:
      item = DmozItem()
      text__extract = site.select('td[2]/span[1]/text()').extract()
      item['company'] = text__extract[0] if text__extract else None
      item['email'] = site.select('td[2]/span[3]/a[1]/text()').extract()[0]
      self.items.append(item)

    self.current_page += 1
    if self.current_page <= self.pages:
      return Request('http://azama.org/looking-to-rent/?tab={0}'.format(self.current_page))


    return self.items


class DmozItem(Item):
  email = Field()
  company = Field()
