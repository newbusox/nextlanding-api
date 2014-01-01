from datetime import timedelta
from django.utils import timezone
from nextlanding_api.apps.marketing import constants
from nextlanding_api.apps.marketing.enums import ProductEnum, DidNotRespondEnum
from nextlanding_api.apps.marketing.models import Correspondence, MarketingEmailAccount
from email.utils import parseaddr
from nextlanding_api.apps.marketing.services import search_product_service
from nextlanding_api.libs.communication_utils.models import Email
from nextlanding_api.libs.communication_utils.signals import email_consumed_by_model


def save_or_update(correspondence):
  correspondence.save(internal=True)


def create_correspondence_from_email(email):
  ret_val = Correspondence(
    to=email.to,
    from_address=email.from_address,
    incoming_text=email.text,
    incoming_html=email.html
  )

  from_name = parseaddr(ret_val.from_address)[0]

  if from_name:
    from_name_split = from_name.split(' ')
    ret_val.from_first_name = from_name_split[0]

    try:
      ret_val.from_last_name = from_name_split[1]
    except IndexError:
      pass

    ret_val.from_name = from_name

  to_address = parseaddr(email.to)[1]

  to_domain = to_address.split('@')[1]

  market_email_account = MarketingEmailAccount.objects.filter(email_addresses__icontains=to_domain).get()

  ret_val.product = market_email_account.product

  if market_email_account.product == ProductEnum.Search:
    search_product_service.provide_correspondence_data(ret_val)

  save_or_update(ret_val)

  email_consumed_by_model.send(Email, instance=email, associated_model=ret_val)

  return ret_val


def send_response_if_applicable(correspondence):
  did_not_respond_reason = None

  return correspondence


def _validate_correspondence_response(correspondence):
  ret_val = None

  if not (correspondence.from_last_name or constants.GEOGRAPHIC_REGION in correspondence.data):
    ret_val = DidNotRespondEnum.MissingInformation
  else:
    time_range = timezone.now() - timedelta(months=9)
    existing_correspondence = (
      Correspondence
      .objects
      .filter(from_last_name=correspondence.from_last_name)
      .filter(changed_date__lt=time_range)
      .filter(data={constants.GEOGRAPHIC_REGION: correspondence.data[constants.GEOGRAPHIC_REGION]})
      .exclude(correspondence)
      .count()
    )

    if existing_correspondence:
      ret_val = DidNotRespondEnum.AlreadyMessaged

  if not ret_val:
    pass


  return ret_val
