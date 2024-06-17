from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Point, LineString, Polygon
from .serializers import PointSerializer, LineStringSerializer, PolygonSerializer
from .services import join_lines, polygon_intersection
from drf_yasg.utils import swagger_auto_schema
from .swagger_schemas import point_create_schema, linestring_create_schema, polygon_create_schema, join_lines_schema, polygon_intersection_schema

class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer

    @swagger_auto_schema(**point_create_schema)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class LineStringViewSet(viewsets.ModelViewSet):
    queryset = LineString.objects.all()
    serializer_class = LineStringSerializer

    @swagger_auto_schema(**linestring_create_schema)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class PolygonViewSet(viewsets.ModelViewSet):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer

    @swagger_auto_schema(**polygon_create_schema)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


@swagger_auto_schema(**join_lines_schema)
@api_view(['POST'])
def join_lines_view(request):
    line_ids = request.data.get('lines', [])
    result, error = join_lines(line_ids)
    if error:
        return Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)
    return Response(LineStringSerializer(result).data, status=status.HTTP_201_CREATED)


@swagger_auto_schema(**polygon_intersection_schema)
@api_view(['POST'])
def polygon_intersection_view(request, id):
    point_ids = request.data.get('points', [])
    result, error = polygon_intersection(id, point_ids)
    if error:
        return Response({'error': error}, status=status.HTTP_400_BAD_REQUEST)
    return Response(PointSerializer(result, many=True).data)
