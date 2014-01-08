from celery import shared_task
from nextlanding_api.aggregates.availability.services import availability_service
from nextlanding_api.aggregates.result.services import result_service
from nextlanding_api.apps.domain.result.services import search_result_service


@shared_task
def create_search_result_task(result_id):
  result = result_service.get_result(result_id)

  return search_result_service.create_search_result(result).id


@shared_task
def update_availability_response_task(result_id):
  result = result_service.get_result(result_id)

  search_result_service.update_availability_response(result)
