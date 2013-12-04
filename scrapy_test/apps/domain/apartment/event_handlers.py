from django.dispatch import receiver
from scrapy_test.aggregates.apartment.models import Apartment
from scrapy_test.aggregates.apartment.signals import created_from_listing, adopted_listing, became_unavailable
from scrapy_test.apps.domain.apartment.services import add_apartment_to_search_tasks


@receiver(created_from_listing, sender=Apartment)
def apartment_created_callback(sender, **kwargs):
  add_apartment_to_search_tasks.create_apartment_task.delay(kwargs['instance'].id)

@receiver(adopted_listing, sender=Apartment)
def apartment_adopted_callback(sender, **kwargs):
  add_apartment_to_search_tasks.update_apartment_task.delay(kwargs['instance'].id)

@receiver(became_unavailable, sender=Apartment)
def became_unavailable_callback(sender, **kwargs):
  add_apartment_to_search_tasks.update_apartment_task.delay(kwargs['instance'].id)
