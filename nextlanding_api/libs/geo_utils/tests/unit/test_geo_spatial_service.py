from django.contrib.gis.geos import Point, Polygon
import pytest
from nextlanding_api.libs.geo_utils.services.geo_spacial_service import point_resides_in_bounds


@pytest.mark.parametrize(("polygon", "point"), [
  (
    (
      (40.7560997756636, -73.99411618709564),
      (40.762341053140275, -73.95566403865814),
      (40.74595644996025, -73.97729337215424),
      (40.7560997756636, -73.99411618709564),
    ),
    (40.7546308, -73.972055)
  ),
])
def test_point_resides_in_bounds(polygon, point):
  assert point_resides_in_bounds(polygon, point)
