from scrapy_test.apps.domain.constants import EMAILER_SENDER_SUBJECT_TEMPLATE, EMAILER_SENDER_BODY_TEMPLATE
from scrapy_test.apps.domain.search.models import SearchEmailerSender


def save_or_update(emailer_sender):
  emailer_sender.save(internal=True)


def get_search_emailer_sender(pk):
  return SearchEmailerSender.objects.get(pk=pk)


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
