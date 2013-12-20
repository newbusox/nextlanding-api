from django.contrib.gis.geos import Point, Polygon, MultiPolygon


def points_resides_in_bounds(points, *polygons):
  polygons = [Polygon(polygon) for polygon in polygons]
  multi = MultiPolygon(polygons)
  prep_multi = multi.prepared

  ret_val = [k for k, v in points.items() if prep_multi.contains(Point(v[0], v[1]))]

  return ret_val


def point_within_distance(point, distance, *polygons):
  return False
