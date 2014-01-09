import logging
from smtplib import SMTPException
from celery.exceptions import Ignore
from celery.task import task
from django.contrib.contenttypes.models import ContentType
from nextlanding_api.libs.communication_utils.exceptions import InvalidOutboundEmailError
from nextlanding_api.libs.communication_utils.services import email_service
from nextlanding_api.libs.python_utils.errors.exceptions import log_ex_with_message

logger = logging.getLogger(__name__)


@task
def send_email_task(from_address, from_name, to_address, subject, plain_text_body,
                    associated_model_content_type_app, associated_model_content_type_model, associated_model_id):
  associated_model_type = ContentType.objects.get(
    app_label=associated_model_content_type_app, model=associated_model_content_type_model
  )

  associated_model = associated_model_type.get_object_for_this_type(pk=associated_model_id)

  try:
    email_service.send_email(from_address, from_name, to_address, subject, plain_text_body, associated_model)
  except InvalidOutboundEmailError:
    raise Ignore()
  except SMTPException as e:
    logger.warn(log_ex_with_message("SMTP Error sending email", e))
    raise send_email_task.retry(exc=e)


@task
def reply_to_email_task(email_id, plain_text_body, associated_model_content_type_app,
                        associated_model_content_type_model,
                        associated_model_id, **kwargs):

  associated_model_type = ContentType.objects.get(
    app_label=associated_model_content_type_app, model=associated_model_content_type_model
  )

  email = email_service.get_email(email_id)

  associated_model = associated_model_type.get_object_for_this_type(pk=associated_model_id)

  try:
    email_service.reply_to_email(email, plain_text_body, associated_model, **kwargs)
  except InvalidOutboundEmailError:
    raise Ignore()
  except SMTPException as e:
    logger.warn(log_ex_with_message("SMTP Error replying to email", e))
    raise reply_to_email_task.retry(exc=e)
