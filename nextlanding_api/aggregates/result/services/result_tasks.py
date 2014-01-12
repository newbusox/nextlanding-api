from email.utils import parseaddr
import logging
from celery.exceptions import Ignore
from celery import shared_task
from django.conf import settings
from django.db import IntegrityError
from nextlanding_api.aggregates.apartment.services import apartment_service
from nextlanding_api.aggregates.result.services import result_service
from nextlanding_api.aggregates.search.services import search_service
from nextlanding_api.libs.communication_utils.models import Email
from nextlanding_api.libs.python_utils.errors.exceptions import log_ex_with_message

logger = logging.getLogger(__name__)
availability_from_email_address_domain = settings.AVAILABILITY_FROM_EMAIL_ADDRESS_DOMAIN


@shared_task
def associate_incoming_email_with_result_task(email_id):
  email = Email.objects.get(pk=email_id)

  from_domain = email.from_address.split('@')[1]

  if from_domain in settings.BODY_RESULT_IDENTIFIER_DOMAINS:
    # in cases where we use a proxy, the 'to' address will not point to the correct availability_from_email_address_domain
    to_address = parseaddr(email.to)[1]
  else:
    to_address = parseaddr(email.envelope['to'][0])[1]

  to_domain = to_address.split('@')[1]

  if to_domain.lower() == availability_from_email_address_domain:

    logger.debug(u"Received searchs params for email: {0}".format(email))

    try:
      ret_val = result_service.associate_incoming_email_with_result(email)
      logger.debug(u"Finished email assocation: {0}".format(email))
      return ret_val
    except Exception as e:
      logger.warn(log_ex_with_message(u"Error associating email", e))
      raise Ignore()
  else:
    logger.debug(u"Result was not associated with email: {0}".format(email))


@shared_task
def notify_results_unavailable_task(apartment_id, reason):
  apartment = apartment_service.get_apartment(apartment_id)

  result_service.notify_results_unavailable(apartment, reason)


@shared_task
def create_result_task(apartment_id, search_id):
  apartment = apartment_service.get_apartment(apartment_id)
  search = search_service.get_search(search_id)

  try:
    return result_service.create_result(apartment, search).id
  except IntegrityError as e:
    logger.info(log_ex_with_message(u"Integrity error creating result", e))
    raise Ignore()


@shared_task
def create_results_task(search_id):
  search = search_service.get_search(search_id)

  result_service.create_results(search)
