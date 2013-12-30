from django.dispatch import receiver
from nextlanding_api.aggregates.apartment.models import Apartment
from nextlanding_api.aggregates.apartment.signals import became_unavailable
from nextlanding_api.aggregates.result.services import result_tasks
from nextlanding_api.aggregates.search.models import Search
from nextlanding_api.aggregates.search.signals import created
from nextlanding_api.apps.domain.search.signals import apartment_added_to_search
from nextlanding_api.libs.communication_utils.models import Email
from nextlanding_api.libs.communication_utils.signals import email_received


@receiver(email_received, sender=Email)
def email_received_occurred_callback(sender, **kwargs):
  #for now, we assume every email coming into the system is for the purposes of availability
  #if we ever add more reasons for incoming email, we'll need to address this.
  result_tasks.associate_incoming_email_with_result_task.delay(kwargs['instance'].id)


@receiver(became_unavailable, sender=Apartment)
def became_unavailable_callback(sender, **kwargs):
  reason = kwargs.pop('reason')
  result_tasks.notify_results_unavailable_task.delay(kwargs['instance'].id, reason)


@receiver(apartment_added_to_search, sender=Search)
def apartment_added_to_search(sender, **kwargs):
  result_tasks.create_result_task.delay(kwargs['apartment'].id, kwargs['instance'].id)

@receiver(created, sender=Search)
def search_created(sender, **kwargs):
  result_tasks.create_results_task.delay(kwargs['instance'].id)
