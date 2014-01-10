from celery import shared_task
from nextlanding_api.aggregates.listing.services import listing_service
from nextlanding_api.apps.web_scraper.services import web_scraper_service


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
  listing = listing_service.get_listing(listing_id)
  web_scraper_service.delete_listing_checker(listing)

@shared_task()
def crawl_individual_page_task(crawl_url):
  web_scraper_service.crawl_individual_page(crawl_url)
