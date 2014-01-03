from django.dispatch import receiver
from nextlanding_api.aggregates.search.models import Search
from nextlanding_api.aggregates.search.signals import initiated_availability_request, sending_client_results_email
from nextlanding_api.apps.communication_associater.availability.email.services import email_tasks


@receiver(initiated_availability_request, sender=Search)
def requested_availability_callback(sender, **kwargs):
  email_tasks.request_availability_about_apartments_task.delay(
    kwargs['instance'].id, kwargs['search_specific_email_message_request']
  )

@receiver(sending_client_results_email, sender=Search)
def sending_client_results_email_callback(sender, **kwargs):
  email_tasks.send_client_results_email.delay(
    kwargs['instance']
  )
