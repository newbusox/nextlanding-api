from django.dispatch import receiver
from scrapy_test.aggregates.result.models import Result
from scrapy_test.aggregates.result.signals import created_from_apartment_and_search
from scrapy_test.apps.domain.result.services import search_result_tasks


@receiver(created_from_apartment_and_search, sender=Result)
def created_from_apartment_and_search_callback(sender, **kwargs):
  search_result_tasks.create_search_result_task(kwargs['instance'].id)
