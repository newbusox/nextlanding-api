def get_coords_for_search(search):
  if search.geo_boundary_points:
    #use the first place they drew and if they didn't draw, take the geocoded search term
    first_geo_point = search.geo_boundary_points["0"][0]
    search_geo = (first_geo_point[0], first_geo_point[1])
  else:
    search_geo = (search.lat, search.lng)

  return search_geo


def get_location_for_search(search):
  coords_for_search = get_coords_for_search(search)

  return {"name": search.formatted_address, "lat": coords_for_search[0], "lng": coords_for_search[1]}
