import logging
import os

from scrapy_test.apps.communication_associater.availability.email.constants import EMAIL_AVAILABILITY_IDENTIFIER_RE, \
  EMAIL_AVAILABILITY_IDENTIFIER

logger = logging.getLogger(__name__)


def get_availability_identifier_from_email(email):
  match = EMAIL_AVAILABILITY_IDENTIFIER_RE.search(email.text)

  if not match:
    raise ValueError("email text did not contain availability identifier: {0}".format(email.text))

  return int(match.groups(0)[0])


def prepare_outgoing_email(result, search_specific_email_message_request, template_vars):
  res_id = EMAIL_AVAILABILITY_IDENTIFIER.format(result.pk)

  search_specific_email_message_request.body += "{0}{0}{1}".format(os.linesep, res_id)
