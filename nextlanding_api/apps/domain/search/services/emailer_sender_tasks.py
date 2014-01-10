from celery import shared_task
from nextlanding_api.aggregates.search.services import search_service
from nextlanding_api.apps.domain.search.services import emailer_sender_service


@shared_task
def create_search_emailer_sender_task(search_id):
  search = search_service.get_search(search_id)

  return emailer_sender_service.create_search_emailer_sender(search).id
