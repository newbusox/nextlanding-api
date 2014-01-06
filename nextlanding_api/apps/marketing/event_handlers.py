from django.dispatch import receiver
from nextlanding_api.apps.marketing.services import correspondence_tasks
from nextlanding_api.libs.communication_utils.models import Email
from nextlanding_api.libs.communication_utils.signals import email_received


@receiver(email_received, sender=Email)
def email_received_occurred_callback(sender, **kwargs):
  correspondence_tasks.associate_incoming_email_with_correspondence_task.delay(kwargs['instance'].id)
