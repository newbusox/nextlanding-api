import logging

logger = logging.getLogger(__name__)


def get_availability_identifier_from_email(email):
  try:
    result_id = int(email.to.split('-')[1].split('@')[0])
  except:
    raise ValueError("Error getting id from this address: {0}".format(email.to))

  return result_id


def prepare_outgoing_email(result, search_specific_email_message_request, template_vars):
  addresss_parts  = template_vars['from_email_address'].split('@')
  new_address = "{0}-{1}@{2}".format(addresss_parts[0],result.pk,addresss_parts[1])
  template_vars['from_email_address'] = new_address
  return search_specific_email_message_request

