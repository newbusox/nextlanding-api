from django.dispatch import receiver
from scrapy_test.aggregates.search.models import Search
from scrapy_test.aggregates.search.signals import created

from scrapy_test.apps.domain.search.services import emailer_sender_tasks


@receiver(created, sender=Search)
def search_created_callback(sender, **kwargs):
  emailer_sender_tasks.create_search_emailer_sender_task.delay(kwargs['instance'].id)
