from django.dispatch import receiver
from scrapy_test.aggregates.apartment.services import apartment_tasks
from scrapy_test.aggregates.listing.signals import sanitized, deleted, died
from scrapy_test.aggregates.listing.models import Listing


@receiver(sanitized,sender = Listing)
def event_occurred_callback(sender, **kwargs):
  apartment_tasks.adopt_listing_task.delay(kwargs['instance'].id)

@receiver(deleted,sender = Listing)
@receiver(died,sender = Listing)
def listing_deleted_callback(sender, **kwargs):
  apartment_tasks.update_availability_task.delay(kwargs['instance'].id)
