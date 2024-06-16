from django.contrib.gis.geos import LineString as DLineString
from .models import LineString

def join_lines(line_ids):
    lines = LineString.objects.filter(id__in=line_ids)
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