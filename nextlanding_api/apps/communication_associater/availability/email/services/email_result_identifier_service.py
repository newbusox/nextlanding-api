from django.conf import settings
from nextlanding_api.apps.communication_associater.availability.email.services import \
  email_body_result_identifier_service, email_from_address_result_identifier_service


def get_availability_identifier_from_email(email):
  return _get_email_result_identifier_impl(email.to).get_availability_identifier_from_email(email)


def _get_email_result_identifier_impl(to_address):
  from_domain = to_address.split('@')[1]
  if from_domain in settings.BODY_RESULT_IDENTIFIER_DOMAINS:
    ret_val = email_body_result_identifier_service
  else:
    ret_val = email_from_address_result_identifier_service

  return ret_val


def prepare_outgoing_email(result, search_specific_email_message_request, template_vars):
  return (
    _get_email_result_identifier_impl(template_vars['to_address'])
    .prepare_outgoing_email(result, search_specific_email_message_request, template_vars)
  )
