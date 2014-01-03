from nextlanding_api.libs.common_domain.event_signal import EventSignal

created = EventSignal('created', __name__, 1, providing_args=['instance', 'attrs'])
initiated_availability_request = EventSignal(
  'initiated_availability_request', __name__, 1,
  providing_args=['instance', 'search_specific_email_message_request']
)
updated_geo_boundary_points = EventSignal(
  'updated_geo_boundary_points', __name__, 1,
  providing_args=['instance', 'geo_boundary_points']
)
sending_client_results_email = EventSignal('sending_client_results_email', __name__, 1,
  providing_args=['instance']
)
