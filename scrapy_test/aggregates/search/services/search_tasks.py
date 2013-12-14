from celery.task import task
from scrapy_test.aggregates.search.services import search_service


@task
def create_search_task(**search_attrs):
  return search_service.create_search(**search_attrs).id

@task
def notify_search_purchase_task(search_id):
  search = search_service.get_search(search_id)
  return search_service.notify_search_purchase(search)
