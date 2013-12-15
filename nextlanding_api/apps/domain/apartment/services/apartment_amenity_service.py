def get_amenities_dict(apartment):
  return {x.amenity_type.name: {"is_available": x.is_available} for x in apartment.amenities.all()}
