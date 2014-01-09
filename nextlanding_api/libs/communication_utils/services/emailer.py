from email.utils import parseaddr
import logging
import os
from smtplib import SMTPException
import sendgrid
from django.conf import settings
from sendgrid.exceptions import SGServiceException
from nextlanding_api.libs.communication_utils.exceptions import InvalidOutboundEmailError
from nextlanding_api.libs.python_utils.errors.exceptions import re_throw_ex

emailer = sendgrid.Sendgrid(settings.SENDGRID_USERNAME, settings.SENDGRID_PASSWORD, secure=True)

secondary_emailer = sendgrid.Sendgrid(settings.GMAIL_USERNAME, settings.GMAIL_PASSWORD, secure=True)
secondary_emailer.smtp.HOSTPORT = ('smtp.gmail.com', 587)

logger = logging.getLogger(__name__)


def send_email(from_address, from_name, to_address, subject, text, html, headers=None):
  to_domain = parseaddr(to_address)[1].split('@')[1]

  msg = sendgrid.Message((from_address, from_name), subject, text, html)
  msg.add_to(to_address)

  if headers:
    for k, v in headers.items():
      msg.add_header(k, v)

  if settings.DEBUG:
    logger.debug(u"{sep}******{sep}{0}{sep}{1}{sep}******".format(msg.subject, msg.text, sep=os.linesep))
  else:
    try:
      if to_domain in settings.SECONDARY_EMAIL_DOMAINS:
        secondary_emailer.smtp.send(msg)
      else:
        emailer.smtp.send(msg)
    except SGServiceException as e:
      throw_ex = re_throw_ex(SMTPException, "Error sending email", e)

      if e.message:
        if "find the recipient domain" in e.message.lower():
          throw_ex = re_throw_ex(InvalidOutboundEmailError, "Invalid email", e)

      raise throw_ex[0], throw_ex[1], throw_ex[2]
