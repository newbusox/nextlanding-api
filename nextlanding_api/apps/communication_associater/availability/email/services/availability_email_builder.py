import logging
from django.conf import settings

from django.template import Context, Template

from nextlanding_api.apps.communication_associater.availability.email.email_objects import \
  SearchSpecificEmailMessageInstance
from nextlanding_api.apps.communication_associater.availability.email.services import email_result_identifier_service

logger = logging.getLogger(__name__)

availability_from_email_address_domain = settings.AVAILABILITY_FROM_EMAIL_ADDRESS_DOMAIN


class AvailabilityEmailBuilder(object):
  def __init__(self, result_identifier_service=email_result_identifier_service):
    self.result_identifier_service = result_identifier_service

  def _get_listing(self):
    #get the 'best' contact - the most recent contact w/ name + email
    listing = (
                self
                .result
                .apartment
                .listings
                .exclude(is_deleted=True)
                .exclude(contact_email_address=None)
                .order_by("-last_updated_date")
              )[:1].get()
    return listing


  def _get_address(self):
    address = self.result.apartment.address
    return address


  def get_availability_email_message(self, result, search_specific_email_message_request):
    variables = {}

    self.result = result
    self.search_specific_email_message_request = search_specific_email_message_request
    self.listing = self._get_listing()

    from_address = self._get_from_email_address()
    from_name = self._get_from_name()
    to_address = self._get_to_email_address()

    variables['address'] = self._get_address()
    variables['bedroom'] = self._get_bedroom_count()
    variables['price'] = self._get_price()

    variables['signature'] = self._get_signature()
    variables['from_name'] = from_name
    variables['from_email_address'] = from_address

    variables['contact_name'] = self._get_contact_name()
    variables['source'] = self._get_source_public_name()
    variables['to_address'] = to_address

    # autoescape=False will prevent '&' from turning into '&amp;'
    # http://stackoverflow.com/questions/237235/how-to-disable-html-encoding-when-using-context-in-django
    context = Context(variables, autoescape=False)

    #search_specific_email_message_request is immutable
    self.search_specific_email_message_request = (
      self.result_identifier_service
      .prepare_outgoing_email(result, search_specific_email_message_request, context)
    )

    #allow us to get versions of vars after putting through result identifier
    from_address = variables['from_email_address']

    subject_template = Template(self.search_specific_email_message_request.subject)
    subject = subject_template.render(context)

    body_template = Template(self.search_specific_email_message_request.body)
    body = body_template.render(context)

    return SearchSpecificEmailMessageInstance(from_address, from_name, subject, body, to_address)


  def _get_contact_name(self):
    contact_name = self.listing.contact_name
    if not contact_name:
      return None
    else:
      contact_name_parts = contact_name.strip().split()
      return contact_name.strip() if len(contact_name_parts) == 0 else contact_name_parts[0]


  def _get_source_public_name(self):
    return self.listing.listing_source.public_name


  def _get_bedroom_count(self):
    return self.result.apartment.bedroom_count


  def _get_price(self):
    return self.result.apartment.price


  def _get_signature(self):
    name = self.search_specific_email_message_request.from_name.split()[0]
    return name


  def _get_from_name(self):
    name = self.search_specific_email_message_request.from_name
    return name


  def _get_from_email_address(self):
    name = self.search_specific_email_message_request.from_name.replace(' ', '.')
    name = name + "@{0}".format(availability_from_email_address_domain)
    return name


  def _get_to_email_address(self):
    return self.listing.contact_email_address
