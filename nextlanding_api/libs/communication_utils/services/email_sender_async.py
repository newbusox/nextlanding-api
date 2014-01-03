import logging
from nextlanding_api.libs.communication_utils.services import email_tasks

logger = logging.getLogger(__name__)


def send_email(from_address, from_name, to_address, subject, plain_text_body, associated_model, eta=None):
  associated_model_content_type_app = associated_model._meta.app_label
  associated_model_content_type_model = associated_model._meta.verbose_name
  associated_model_content_type_id = associated_model.pk

  email_tasks.send_email_task.apply_async(
    (
      from_address, from_name, to_address, subject, plain_text_body,
      associated_model_content_type_app, associated_model_content_type_model,
      associated_model_content_type_id,
    ),
    eta=eta
  )
