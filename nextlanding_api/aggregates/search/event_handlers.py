from django.dispatch import receiver
from nextlanding_api.aggregates.search.models import Search
from nextlanding_api.aggregates.search.services import search_tasks
from nextlanding_api.aggregates.search.signals import created, initiated_availability_request
from nextlanding_api.apps.domain.search.models import PotentialSearch
from nextlanding_api.apps.domain.search.services import potential_search_tasks
from nextlanding_api.apps.domain.search.signals import potential_search_completed


@receiver(potential_search_completed, sender=PotentialSearch)
def potential_search_completed_callback(sender, **kwargs):
  (
    search_tasks.create_search_task.s(**kwargs['instance'].search_attrs) |
    potential_search_tasks.associate_search_task.s(kwargs['instance'].id)
  ).delay()

@receiver(created, sender=Search)
def notify_search_purchase_task_callback(sender, **kwargs):
  search_tasks.notify_search_purchase_task.delay(kwargs['instance'].id)

@receiver(initiated_availability_request, sender=Search)
def requested_availability_callback(sender, **kwargs):
  search_tasks.send_client_results_email.delay(
    kwargs['instance'].id
  )
