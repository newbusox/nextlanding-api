from django.dispatch import receiver
from nextlanding_api.aggregates.search.models import Search
from nextlanding_api.aggregates.search.signals import created

from nextlanding_api.apps.domain.search.services import emailer_sender_tasks


@receiver(created, sender=Search)
def search_created_callback(sender, **kwargs):
  emailer_sender_tasks.create_search_emailer_sender_task.delay(kwargs['instance'].id)
