from django.contrib.gis.geos import Point, Polygon


def point_resides_in_bounds(polygon, point):
  poly = Polygon(polygon)
  prep_poly = poly.prepared
  return prep_poly.contains(Point(point))
