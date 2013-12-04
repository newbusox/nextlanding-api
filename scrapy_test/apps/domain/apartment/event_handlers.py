from django.dispatch import receiver
from scrapy_test.aggregates.apartment.models import Apartment
from scrapy_test.aggregates.apartment.signals import created_from_listing
from scrapy_test.apps.domain.apartment.services import add_apartment_to_search_tasks


@receiver(created_from_listing, sender=Apartment)
def search_created_callback(sender, **kwargs):
  add_apartment_to_search_tasks.create_apartment_task.delay(kwargs['instance'].id)
