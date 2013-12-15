from nextlanding_api.aggregates.apartment.enums import ApartmentUnavailableReasonEnum
from nextlanding_api.aggregates.availability.models import Availability
from nextlanding_api.aggregates.availability.services import availability_service
from nextlanding_api.aggregates.result import factories
from nextlanding_api.aggregates.result.models import Result
from nextlanding_api.apps.communication_associater.availability.email.services import email_result_identifier_service
from nextlanding_api.libs.communication_utils.models import Email
from nextlanding_api.libs.communication_utils.services import email_service
from nextlanding_api.libs.communication_utils.signals import email_consumed_by_model


def create_result(apartment, search):
  result = factories.construct_result(apartment, search)

  save_or_update(result)

  return result


def get_result(pk):
  return Result.objects.get(pk=pk)


def save_or_update(result):
  result.save(internal=True)


def associate_incoming_email_with_result(email,
                                         _email_service=email_service,
                                         _email_result_identifier_service=email_result_identifier_service,
                                         _availability_service=availability_service):
  result_id = _email_result_identifier_service.get_availability_identifier_from_email(email)

  result = get_result(result_id)

  contents = _email_service.get_reply_contents(email)

  availability_type = _availability_service.get_availability_from_str(contents)

  result.add_availability_response(contents, email.sent_date, availability_type)

  save_or_update(result)

  email_consumed_by_model.send(Email, instance=email, associated_model=result)


def notify_results_unavailable(apartment, reason):
  #find all results that are NOT `notified unavailable` because they've already been notified as unavailable. We
  # should set these to `other user found it to be unavailable`
  if reason == ApartmentUnavailableReasonEnum.NotifiedUnavailable:

    #we are going to exclude the `unavailable` type
    unavailable_type = Availability.objects.get_unavailable_type()

    different_user_notified_unavailable_type = Availability.objects.get_different_user_notified_unavailable_type()

    results = Result.objects.find_results_to_be_notified_of_availability(apartment, unavailable_type)
    for r in results:
      r.change_availability(different_user_notified_unavailable_type)
      save_or_update(r)

  elif reason == ApartmentUnavailableReasonEnum.AllListingsDeleted:
    all_listings_deleted_type = Availability.objects.get_all_listings_deleted_type()
    results = Result.objects.find_results_to_be_notified_of_availability(apartment)

    for r in results:
      r.change_availability(all_listings_deleted_type)
      save_or_update(r)
