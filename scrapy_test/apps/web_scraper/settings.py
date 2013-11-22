import os
import sys


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

sys.path.append(PROJECT_ROOT)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scrapy_test.settings.dev") #Changed in DDS v.0.3

BOT_NAME = 'scrapy_test'

SPIDER_MODULES = [
  'dynamic_scraper.spiders',
  'scrapy_test.apps.web_scraper.spiders',
  'scrapy_test.apps.web_scraper.checkers',
]
USER_AGENT = '%s/%s' % (BOT_NAME, '1.0')

ITEM_PIPELINES = [

]

EXTENSIONS = {
}

DOWNLOADER_MIDDLEWARES = {
}

# https://scrapy.readthedocs.org/en/latest/topics/settings.html#randomize-download-delay
DOWNLOAD_DELAY = 0.73
