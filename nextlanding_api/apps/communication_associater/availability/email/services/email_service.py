import logging
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from nextlanding_api.apps.communication_associater.availability.email.services.availability_email_builder import \
  AvailabilityEmailBuilder
from nextlanding_api.libs.communication_utils.services import email_service, email_sender_async

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
