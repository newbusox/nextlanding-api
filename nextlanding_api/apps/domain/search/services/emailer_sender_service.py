from django.db import transaction
from nextlanding_api.aggregates.search.services import search_service
from nextlanding_api.apps.domain.constants import EMAILER_SENDER_SUBJECT_TEMPLATE, EMAILER_SENDER_BODY_TEMPLATE
from nextlanding_api.apps.domain.search.models import SearchEmailerSender


def save_or_update(emailer_sender):
  emailer_sender.save(internal=True)


def get_search_emailer_sender(search_aggregate_id):
  return SearchEmailerSender.objects.get(search_aggregate_id=search_aggregate_id)


def create_search_emailer_sender(search):
  emailer_sender_model = SearchEmailerSender(
    search_aggregate_id=search.pk,
    specified_location=search.specified_location,
    description=search.description,
    subject=EMAILER_SENDER_SUBJECT_TEMPLATE,
    body=EMAILER_SENDER_BODY_TEMPLATE,
  )

  save_or_update(emailer_sender_model)

  return emailer_sender_model


def send_search_email(emailer_sender_model, from_name, subject, body):
  emailer_sender_model.from_name = from_name
  emailer_sender_model.subject = subject
  emailer_sender_model.body = body

  with transaction.commit_on_success():
    search = search_service.get_search(emailer_sender_model.search_aggregate_id)

    search.request_availability_from_contacts(from_name, subject, body)

    search_service.save_or_update(search)
    save_or_update(emailer_sender_model)

  return emailer_sender_model

def send_client_results_email(search):
  with transaction.commit_on_success():
    search.send_client_results_email()
    search_service.save_or_update(search)
