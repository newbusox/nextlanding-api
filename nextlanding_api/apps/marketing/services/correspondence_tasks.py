from email.utils import parseaddr
import logging
from celery.exceptions import Ignore
from celery.task import task
from nextlanding_api.aggregates.apartment.services import apartment_service
from nextlanding_api.aggregates.result.services import result_service
from nextlanding_api.aggregates.search.services import search_service
from nextlanding_api.apps.marketing.models import MarketingEmailAccount
from nextlanding_api.apps.marketing.services import correspondence_service
from nextlanding_api.libs.communication_utils.models import Email
from nextlanding_api.libs.python_utils.errors.exceptions import log_ex_with_message

logger = logging.getLogger(__name__)


@task
def associate_incoming_email_with_correspondence_task(email_id):
  email = Email.objects.get(pk=email_id)

  to_address = parseaddr(email.to)[1]

  to_domain = to_address.split('@')[1]

  if MarketingEmailAccount.objects.filter(email_addresses__icontains=to_domain):

    logger.debug(u"Received correspondence params for email: {0}".format(email))

    try:
      ret_val = correspondence_service.create_correspondence_from_email(email)
      correspondence_service.send_response_if_applicable(ret_val)
      logger.debug(u"Finished creating correspondence: {0}".format(email))
      return ret_val
    except Exception as e:
      logger.warn(log_ex_with_message(u"Error creating correspondence", e))
      raise Ignore()
  else:
    logger.debug(u"Correspondence was not associated with email: {0}".format(email))
