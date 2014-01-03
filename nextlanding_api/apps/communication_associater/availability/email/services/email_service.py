import logging
import datetime
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from nextlanding_api.apps.communication_associater.availability.email.services.availability_email_builder import \
  AvailabilityEmailBuilder
from nextlanding_api.apps.communication_associater.results.email import constants
from nextlanding_api.libs.communication_utils.services import email_sender_async
import pytz

logger = logging.getLogger(__name__)

availability_from_email_address_domain = settings.AVAILABILITY_FROM_EMAIL_ADDRESS_DOMAIN


def request_availability_about_apartments(search, search_specific_email_message_request,
                                          _email_sender=email_sender_async):
  #there is a circular dependency between result -> ... -> email_service.
  from nextlanding_api.aggregates.result.models import Result

  #only get results that have not gotten a response back yet. This is in case we re-email our contacts because we
  # haven't gotten enough responses. We don't want to re-contact those who've already responded.
  results_to_request_notification = (
    Result
    .objects
    .find_results_from_search(search)
    .filter(availability_last_response_date=None)
  )

  email_builder = AvailabilityEmailBuilder()

  for r in results_to_request_notification:
    try:
      message = email_builder.get_availability_email_message(r, search_specific_email_message_request)
    except ObjectDoesNotExist:
      logger.debug("No suitable contact info found: {0}".format(r))
    except:
      logger.exception("Error creating email message")
    else:
      try:
        _email_sender.send_email(
          message.from_address, message.from_name, message.to_address, message.subject, message.body, r
        )
      except:
        logger.exception("Error sending email message")


def send_client_results_email(search, _email_service=email_sender_async):
  search_id = search.pk

  # send in 1 hour
  eastern_now = datetime.datetime.now(pytz.timezone('US/Eastern'))
  email_schedule_date = eastern_now + relativedelta(minutes=60)

  _email_service.send_email(
    settings.PUBLIC_EMAIL[1],
    settings.PUBLIC_EMAIL[0],
    search.email_address,
    constants.CLIENT_RESULTS_SUBJECT_TEMPLATE,
    constants.CLIENT_RESULTS_BODY_TEMPLATE.format(search_id),
    search,
    email_schedule_date
  )
