import logging

logger = logging.getLogger(__name__)


def get_availability_identifier_from_email(email):
  try:
    result_id = int(email.to_address.split('-')[1].split('@')[0])
  except:
    raise ValueError("Error getting id from this address: {0}".format(email.to_address))

  return result_id


def prepare_outgoing_email(result, search_specific_email_message_request, template_vars):
  template_vars['to_address'] = "{0}-{1}".format(['to_address'], result.pk)

