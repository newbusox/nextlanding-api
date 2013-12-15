from nextlanding_api.aggregates.search.models import Search


def construct_search(**kwargs):
  search = Search._from_attrs(**kwargs)
  return search
