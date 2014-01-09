from django.conf import settings
import stripe
from nextlanding_api.libs.payment_utils.exceptions import ChargeError, InvalidCardError
from nextlanding_api.libs.python_utils.errors.exceptions import re_throw_ex


def charge_payment(amount_in_dollars, token, description):
  stripe.api_key = settings.STRIPE_SECRET_KEY
  token_id = token['id']
  amount_in_cents = int(amount_in_dollars * 100)

  try:
    charge = stripe.Charge.create(
      amount=amount_in_cents,
      currency="usd",
      card=token_id,
      description=description
    )
  except stripe.CardError as e:
    throw_ex = re_throw_ex(ChargeError, "Error processing payment", e)

    if e.message:
      if "security code is incorrect" in e.message.lower():
        throw_ex = re_throw_ex(InvalidCardError, "Invalid card", e)

    raise throw_ex[0], throw_ex[1], throw_ex[2]

  return charge
