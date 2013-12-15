from django.dispatch import receiver
from nextlanding_api.aggregates.listing.models import Listing
from nextlanding_api.aggregates.listing.signals import created, deleted
from nextlanding_api.apps.web_scraper.services import web_scraper_tasks


@receiver(created, sender=Listing)
def listing_sanitized_create_checker_callback(sender, **kwargs):
  web_scraper_tasks.add_listing_checker_task.delay(kwargs['instance'].id)


@receiver(deleted, sender=Listing)
def listing_remove_checker_callback(sender, **kwargs):
  web_scraper_tasks.delete_listing_checker_task.delay(kwargs['instance'].id)
