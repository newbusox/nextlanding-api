from celery.task import task
from scrapy_test.aggregates.result.services import result_service
from scrapy_test.apps.domain.result.services import search_result_service


@task
def create_search_result_task(result_id):
  result = result_service.get_result(result_id)

  return search_result_service.create_search_result(result).id
