from celery import shared_task
from nextlanding_api.aggregates.search.services import search_service
from nextlanding_api.apps.communication_associater.availability.email.services import email_service
from nextlanding_api.apps.communication_associater.availability.email.email_objects import SearchSpecificEmailMessageRequest


@shared_task
def request_availability_about_apartments_task(search_id, search_specific_email_message_request):
  if not isinstance(search_specific_email_message_request, tuple):
    # celery will pass in a dict when it's async but in the case of CELERY_ALWAYS_EAGER (like testing) it will not be
    # serialized at all and will remain a namedtuple
    search_specific_email_message_request = SearchSpecificEmailMessageRequest(**search_specific_email_message_request)

  search = search_service.get_search(search_id)

  return email_service.request_availability_about_apartments(search, search_specific_email_message_request)
