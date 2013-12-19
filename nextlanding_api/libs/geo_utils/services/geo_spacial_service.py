from django.contrib.gis.geos import Point, Polygon, MultiPolygon


def point_resides_in_bounds(point, polygon):
  poly = Polygon(polygon)
  prep_poly = poly.prepared
  return prep_poly.contains(Point(point))


def point_resides_in_multi_bounds(point, *polygons):
  polygons = [Polygon(polygon) for polygon in polygons]
  multi = MultiPolygon(polygons)
  prep_multi = multi.prepared

  return prep_multi.contains(Point(point))
