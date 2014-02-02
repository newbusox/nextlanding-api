import logging

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseServerError
from rest_framework.views import APIView

from nextlanding_api.libs.communication_utils.exceptions import EmailParseError
from nextlanding_api.libs.communication_utils.models import Email
from nextlanding_api.libs.communication_utils.services import email_service


logger = logging.getLogger(__name__)


class CommunicationEmailView(APIView):
  """
  API endpoint for incoming emails.
  """

  def post(self, request, *args, **kwargs):
    if request.QUERY_PARAMS.get('token') != settings.EXTERNAL_API_TOKEN and not settings.DEBUG:
      return HttpResponseForbidden()

    else:
      email_data = request.DATA.dict()
      if not email_service.is_spam(**email_data):

        try:
          email = Email.construct_incoming_email(**email_data)
          email_service.create_incoming_mail(email)

        except (EmailParseError, IntegrityError, ValidationError, KeyError):
          logger.info('ignoring invalid email')
        except Exception:
          logger.exception('error accepting email')

          return HttpResponseServerError()
      else:
        logger.info('spam detected')

      return HttpResponse(status=200)
