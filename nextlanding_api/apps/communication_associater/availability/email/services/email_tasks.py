from celery import shared_task
from nextlanding_api.aggregates.search.services import search_service
from nextlanding_api.apps.communication_associater.availability.email.services import email_service


@shared_task
def request_availability_about_apartments_task(search_id, search_specific_email_message_request):
  search = search_service.get_search(search_id)

  return email_service.request_availability_about_apartments(search, search_specific_email_message_request)
