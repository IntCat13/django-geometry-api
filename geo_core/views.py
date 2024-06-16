from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Point, LineString, Polygon
from .serializers import PointSerializer, LineStringSerializer, PolygonSerializer

class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer

class LineStringViewSet(viewsets.ModelViewSet):
    queryset = LineString.objects.all()
    serializer_class = LineStringSerializer

class PolygonViewSet(viewsets.ModelViewSet):
    queryset = Polygon.objects.all()
    serializer_class = PolygonSerializer