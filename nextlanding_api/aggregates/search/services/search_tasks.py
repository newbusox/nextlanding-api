from celery import shared_task
from nextlanding_api.aggregates.search.services import search_service


@shared_task
def create_search_task(**search_attrs):
  return search_service.create_search(**search_attrs).id

@shared_task
def notify_search_purchase_task(search_id):
  search = search_service.get_search(search_id)
  return search_service.notify_search_purchase(search)

@shared_task
def send_client_results_email(search_id):
  return search_service.send_client_results_email(search_id)
