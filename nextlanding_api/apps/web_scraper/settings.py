import os
import sys


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

sys.path.append(PROJECT_ROOT)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nextlanding_api.settings.dev") #Changed in DDS v.0.3

BOT_NAME = 'nextlanding_api'

SPIDER_MODULES = [
  'dynamic_scraper.spiders',
  'nextlanding_api.apps.web_scraper.spiders',
  'nextlanding_api.apps.web_scraper.checkers',
]
USER_AGENT = '%s/%s' % (BOT_NAME, '1.0')

ITEM_PIPELINES = [
  'nextlanding_api.apps.web_scraper.pipelines.validation_pipeline.ValidationPipeline',
  'nextlanding_api.apps.web_scraper.pipelines.aggregate_writer_pipeline.AggregateCommandPipeline',
]

EXTENSIONS = {
  'nextlanding_api.apps.web_scraper.scrapy.extensions.StopOnDuplicateItem': 500,
  'nextlanding_api.apps.web_scraper.scrapy.extensions.StatsReporter': 500,
}

DOWNLOADER_MIDDLEWARES = {
  'nextlanding_api.apps.web_scraper.scrapy.middlewares.ProxyMiddleware': 755,
  'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': None,
}

# https://scrapy.readthedocs.org/en/latest/topics/settings.html#randomize-download-delay
DOWNLOAD_DELAY = 0.73
