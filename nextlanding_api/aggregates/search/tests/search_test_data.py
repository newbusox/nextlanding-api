import pytz

eastern_time_zone = pytz.timezone('US/Eastern')

# region search 1
search_1 = {
  'description': 'I want a great place to live',
  'email_address': 'test@test.com',
  'specified_location': 'Astoria NY',
  'geo_boundary_points': {"0":[[40.738152838822934,-74.0741103887558],[40.717338733312495,-74.05419766902924],[40.701463603604594,-74.08990323543549]]},
  'no_fee_preferred': True,
  'bedroom_max': 2,
  'bathroom_max': 1.5,
  'sqfeet_max': 850.50,
  'price_max': 2500.50,
  'amenities': [1, 2]
}
search_1_expected_lat = 40.7623925
search_1_expected_lng = -73.9301037

#endregion
