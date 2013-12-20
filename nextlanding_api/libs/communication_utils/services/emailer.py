import logging
from smtplib import SMTPException
import sendgrid
from django.conf import settings
from sendgrid.exceptions import SGServiceException
from nextlanding_api.libs.python_utils.errors.exceptions import re_throw_ex

emailer = sendgrid.Sendgrid(settings.SENDGRID_USERNAME, settings.SENDGRID_PASSWORD, secure=True)

secondary_emailer = sendgrid.Sendgrid(settings.GMAIL_USERNAME, settings.GMAIL_PASSWORD, secure=True)
secondary_emailer.smtp.HOSTPORT = ('smtp.gmail.com', 587)

logger = logging.getLogger(__name__)


def send_email(from_address, from_name, to_address, subject, text, html):
  to_domain = to_address.split('@')[1]

  msg = sendgrid.Message((from_address, from_name), subject, text, html)
  msg.add_to(to_address)

  if settings.DEBUG:
    logger.info(msg)
  else:
    try:
      if to_domain in settings.SECONDARY_EMAIL_DOMAINS:
        secondary_emailer.smtp.send(msg)
      else:
        emailer.smtp.send(msg)
    except SGServiceException as e:
      throw_ex = re_throw_ex(SMTPException, "Error sending email", e)
      raise throw_ex[0], throw_ex[1], throw_ex[2]
