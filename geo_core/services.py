from django.contrib.gis.geos import LineString as DLineString, Polygon as DPolygon, Point as DPoint
from .models import Point, LineString, Polygon

def join_lines(line_ids):
    lines = LineString.objects.filter(id__in=line_ids).order_by('id')
    if not lines.exists():
        return None, 'No lines found with provided IDs'

    coordinates = []
    for line in lines:
        coordinates.extend(line.geom.coords)

    seen = set()
    unique_coordinates = []
    for coord in coordinates:
        if coord not in seen:
            unique_coordinates.append(coord)
            seen.add(coord)

    joined_linestring = DLineString(unique_coordinates, srid=4326)
    result = LineString.objects.create(geom=joined_linestring)
    return result, None

def polygon_intersection(polygon_id, point_ids):
    try:
        polygon = Polygon.objects.get(id=polygon_id)
    except Polygon.DoesNotExist:
        return None, 'Polygon not found'

    points = Point.objects.filter(id__in=point_ids)
    if not points.exists():
        return None, 'No points found with provided IDs'

    intersecting_points = []
    for point in points:
        if polygon.geom.intersects(point.geom):
            intersecting_points.append(point)
    
    return intersecting_points, None
