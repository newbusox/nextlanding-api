from django.dispatch import receiver
from scrapy_test.aggregates.search.services import search_tasks
from scrapy_test.apps.domain.search.models import PotentialSearch
from scrapy_test.apps.domain.search.services import potential_search_tasks
from scrapy_test.apps.domain.search.signals import potential_search_completed


@receiver(potential_search_completed, sender=PotentialSearch)
def potential_search_completed_callback(sender, **kwargs):
  (
    search_tasks.create_search_task.s(**kwargs['instance'].search_attrs) |
    potential_search_tasks.associate_search_task.s(kwargs['instance'].id)
  ).delay()
