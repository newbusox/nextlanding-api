import logging
from django.conf import settings

from scrapy_test.apps.communication_associater.availability.email.services import \
  email_body_result_identifier_service, email_to_address_result_identifier_service
from scrapy_test.apps.communication_associater.availability.email.services.availability_email_builder import \
  AvailabilityEmailBuilder
from scrapy_test.libs.communication_utils.services import email_service

logger = logging.getLogger(__name__)

availability_from_email_address_domain = settings.AVAILABILITY_FROM_EMAIL_ADDRESS_DOMAIN


def request_availability_about_apartments(search, search_specific_email_message_request, _email_service=email_service):
  #there is a circular dependency between result -> ... -> email_service.
  from scrapy_test.aggregates.result.models import Result

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
    except:
      logger.exception("Error creating email message")
    else:
      try:
        _email_service.send_email(
          message.from_address, message.from_name, message.to_address, message.subject, message.body, r
        )
      except:
        logger.exception("Error sending email message")
