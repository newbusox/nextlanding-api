from celery.task import task
from nextlanding_api.aggregates.search.services import search_service
from nextlanding_api.apps.domain.search.services import potential_search_service


@task
def associate_search_task(search_id, potential_search_id):
  search = search_service.get_search(search_id)
  potential_search = potential_search_service.get_potential_search(potential_search_id)

  return potential_search_service.associate_search(search, potential_search).id
