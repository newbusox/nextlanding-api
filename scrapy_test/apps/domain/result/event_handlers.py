from django.dispatch import receiver
from scrapy_test.aggregates.result.models import Result
from scrapy_test.aggregates.result.signals import created_from_apartment_and_search, availability_contact_responded
from scrapy_test.apps.domain.result.services import search_result_tasks


@receiver(created_from_apartment_and_search, sender=Result)
def created_from_apartment_and_search_callback(sender, **kwargs):
  search_result_tasks.create_search_result_task.delay(kwargs['instance'].id)


@receiver(availability_contact_responded, sender=Result)
def availability_contact_responded_callback(sender, **kwargs):
  search_result_tasks.update_availability_response_task.delay(kwargs['instance'].id)
