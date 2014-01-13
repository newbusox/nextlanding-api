import logging
from celery import shared_task
from celery.exceptions import Ignore
from nextlanding_api.aggregates.listing.services import listing_service
from nextlanding_api.apps.web_scraper.services import web_scraper_service
from nextlanding_api.libs.python_utils.errors.exceptions import log_ex_with_message

logger = logging.getLogger(__name__)


@shared_task()
def run_spiders_task():
  web_scraper_service.run_spiders()


@shared_task()
def run_checkers_task():
  web_scraper_service.run_checkers()


@shared_task()
def add_listing_checker_task(listing_id):
  listing = listing_service.get_listing(listing_id)

  return web_scraper_service.add_listing_checker(listing).pk


@shared_task()
def delete_listing_checker_task(listing_id):
  try:
    listing = listing_service.get_listing(listing_id)
    web_scraper_service.delete_listing_checker(listing)
  except Exception as e:
    logger.info(log_ex_with_message(u"Error deleting checker", e))
    raise Ignore()


@shared_task()
def crawl_individual_page_task(crawl_url):
  web_scraper_service.crawl_individual_page(crawl_url)
