import logging
from celery.exceptions import Ignore
from celery.task import task
from nextlanding_api.aggregates.apartment.services import apartment_service
from nextlanding_api.aggregates.result.services import result_service
from nextlanding_api.aggregates.search.services import search_service
from nextlanding_api.libs.communication_utils.models import Email
from nextlanding_api.libs.python_utils.errors.exceptions import log_ex_with_message

logger = logging.getLogger(__name__)

@task
def associate_incoming_email_with_result_task(email_id):
  email = Email.objects.get(pk=email_id)

  logger.debug("Received searchs params for email: {0}".format(email))

  try:
    ret_val = result_service.associate_incoming_email_with_result(email)
    logger.debug("Finished email assocation: {0}".format(email))
    return ret_val
  except Exception as e:
    logger.warn(log_ex_with_message("Error associating email", e))
    raise Ignore()

@task
def notify_results_unavailable_task(apartment_id, reason):
  apartment = apartment_service.get_apartment(apartment_id)

  result_service.notify_results_unavailable(apartment, reason)


@task
def create_result_task(apartment_id, search_id):
  apartment = apartment_service.get_apartment(apartment_id)
  search = search_service.get_search(search_id)

  return result_service.create_result(apartment, search).id
