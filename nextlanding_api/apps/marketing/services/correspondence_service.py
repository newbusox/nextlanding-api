from email.utils import parseaddr
import datetime
from dateutil.relativedelta import relativedelta
from django.db.models import Q

from django.template import Context, Template
from django.utils import timezone
import pytz

from nextlanding_api.libs.communication_utils.services import email_sender_async, email_service
from nextlanding_api.apps.marketing import constants
from nextlanding_api.apps.marketing.enums import DidNotRespondEnum
from nextlanding_api.apps.marketing.models import Correspondence, MarketingEmailAccount
from nextlanding_api.apps.marketing.services import source_correspondence_service
from nextlanding_api.libs.communication_utils.models import Email
from nextlanding_api.libs.communication_utils.signals import email_consumed_by_model
from nextlanding_api.libs.text_utils.parsers import text_parser


def save_or_update(correspondence):
  correspondence.save(internal=True)


def create_correspondence_from_email(email):
  ret_val = source_correspondence_service.construct_correspondence_from_email(email)

  from_name = parseaddr(ret_val.from_address)[0]

  if from_name:
    from_name_split = from_name.split(' ')
    ret_val.from_first_name = from_name_split.pop(0)

    try:
      #get the last part of a multiple-spaced name
      ret_val.from_last_name = from_name_split[-1]
    except IndexError:
      pass

    ret_val.from_name = from_name

  market_email_account = _get_marketing_email_account_from_email(ret_val.to)

  ret_val.product = market_email_account.product

  save_or_update(ret_val)

  email_consumed_by_model.send(Email, instance=email, associated_model=ret_val)

  return ret_val


def _get_marketing_email_account_from_email(email_to_address):
  to_address = parseaddr(email_to_address)[1]

  market_email_account = MarketingEmailAccount.objects.filter(email_addresses__icontains=to_address).get()

  return market_email_account


def send_response_if_applicable(correspondence):
  did_not_respond_reason = _validate_correspondence_response(correspondence)

  if did_not_respond_reason:
    correspondence.responded = False
    correspondence.did_not_respond_reason = did_not_respond_reason
  else:
    variables = {}
    variables['contact_name'] = correspondence.from_first_name

    market_email_account = _get_marketing_email_account_from_email(correspondence.to)

    to_address = parseaddr(correspondence.to)[1]

    market_email_address = next(
      account for account in market_email_account.email_addresses.splitlines() if to_address.lower() in account
    )

    from_name, from_address = parseaddr(market_email_address)

    # autoescape=False will prevent '&' from turning into '&amp;'
    # http://stackoverflow.com/questions/237235/how-to-disable-html-encoding-when-using-context-in-django
    context = Context(variables, autoescape=False)

    body_template = Template(constants.SEARCH_BODY_REPLY_TEMPLATE)
    body = body_template.render(context)

    correspondence.responded = True
    correspondence.outgoing_text = body
    correspondence.outgoing_html = email_service.convert_text_to_html(body)

    eastern_now = datetime.datetime.now(pytz.timezone('US/Eastern'))

    if eastern_now.time() < datetime.time(8, 00):
      # too early
      email_schedule_date = eastern_now.replace(hour=8, minute=5)
    elif eastern_now.time() > datetime.time(20, 00):
      # too later
      email_schedule_date = eastern_now.replace(hour=8, minute=5) + relativedelta(days=1)
    else:
      # in the right time frame but delay a bit
      email_schedule_date = eastern_now + relativedelta(minutes=5)

    # wait a day to send it
    email_schedule_date = email_schedule_date + relativedelta(days=1)

    email_sender_async.reply_to_email(
      correspondence.originating_email,
      body,
      correspondence,
      email_schedule_date,
      from_address=from_address,
      from_name=from_name,
    )

  save_or_update(correspondence)

  return correspondence


def _validate_correspondence_response(correspondence, _text_parser=text_parser):
  ret_val = None

  if not ret_val:
    market_email_account = _get_marketing_email_account_from_email(correspondence.to)

    if market_email_account.ignore_keywords:
      ignore_hash = {alias: alias for alias in market_email_account.ignore_keywords.splitlines()}

      ignore_results = _text_parser.get_canonical_name_from_keywords(correspondence.incoming_text, ignore_hash)

      if ignore_results:
        ret_val = DidNotRespondEnum.IgnoreRecipient

  if not ret_val:
      if not source_correspondence_service.is_valid_recipient(correspondence):
        ret_val = DidNotRespondEnum.IgnoreRecipient

  if not ret_val:
    try:
      if not len(correspondence.from_first_name) > 1 and len(correspondence.from_last_name) > 1:
        ret_val = DidNotRespondEnum.MissingInformation
    except TypeError:
      # either of the names or None
      ret_val = DidNotRespondEnum.MissingInformation

  if not ret_val:
    if not constants.GEOGRAPHIC_REGION in correspondence.data:
      ret_val = DidNotRespondEnum.MissingInformation

  if not ret_val:
    time_range = timezone.now() - relativedelta(months=3)
    existing_correspondence = (
      Correspondence
      .objects
      .filter(
        Q(from_first_name__iexact=correspondence.from_first_name, from_last_name__iexact=correspondence.from_last_name)
        |
        Q(from_last_name__iexact=correspondence.from_last_name, changed_date__gte=time_range)
      )
      .filter(data__contains={constants.GEOGRAPHIC_REGION: correspondence.data[constants.GEOGRAPHIC_REGION]})
      .exclude(id=correspondence.pk)
      .count()
    )

    if existing_correspondence:
      ret_val = DidNotRespondEnum.AlreadyMessaged

  return ret_val
