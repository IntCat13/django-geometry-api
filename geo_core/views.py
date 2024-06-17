from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Point, LineString, Polygon
from .serializers import PointSerializer, LineStringSerializer, PolygonSerializer
from .services import join_lines, polygon_intersection

class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer

class LineStringViewSet(viewsets.ModelViewSet):
    queryset = LineString.objects.all()
    serializer_class = LineStringSerializer

class PolygonViewSet(viewsets.ModelViewSet):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer

@api_view(['POST'])
def join_lines_view(request):
    line_ids = request.data.get('lines', [])
    if not line_ids:
        return Response({'error': 'No line IDs provided'}, status=status.HTTP_400_BAD_REQUEST)

    result, error = join_lines(line_ids)
    if error:
        return Response({'error': error}, status=status.HTTP_404_NOT_FOUND)

    return Response({
        'id': result.id,
        'type': 'LineString',
        'coordinates': result.geom.coords
    }, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def polygon_intersection_view(request, id):
    point_ids = request.data.get('points', [])
    if not point_ids:
        return Response({'error': 'No point IDs provided'}, status=status.HTTP_400_BAD_REQUEST)

    intersecting_points, error = polygon_intersection(id, point_ids)
    if error:
        return Response({'error': error}, status=status.HTTP_404_NOT_FOUND)

    result = [{
        'id': point.id,
        'type': 'Point',
        'coordinates': point.geom.coords
    } for point in intersecting_points]

    return Response(result, status=status.HTTP_200_OK)
