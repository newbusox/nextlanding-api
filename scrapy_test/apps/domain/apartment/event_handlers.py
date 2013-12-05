from django.dispatch import receiver
from scrapy_test.aggregates.apartment.models import Apartment
from scrapy_test.aggregates.apartment.signals import became_unavailable
from scrapy_test.aggregates.listing.models import Listing
from scrapy_test.aggregates.listing.signals import associated_with_apartment
from scrapy_test.apps.domain.apartment.services import add_apartment_to_search_tasks


@receiver(associated_with_apartment, sender=Listing)
def apartment_associated_callback(sender, **kwargs):
  """
  the reason we're targeting the `associated_with_apartment` event is because it will be the first point in time
  where an apartment is fully created and fully linked with any listings. The `created` event for an apartment might
  be too early and will have a apartment.listings.count() of 0.
  """
  add_apartment_to_search_tasks.update_apartment_from_listing_task.delay(kwargs['instance'].id)

@receiver(became_unavailable, sender=Apartment)
def became_unavailable_callback(sender, **kwargs):
  add_apartment_to_search_tasks.disable_apartment_task.delay(kwargs['instance'].id)
