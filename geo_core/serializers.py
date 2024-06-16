from rest_framework import serializers
from django.contrib.gis.geos import Point as DPoint, LineString as DLineString, Polygon as DPolygon, LinearRing
from .models import Point, LineString, Polygon

class PointSerializer(serializers.ModelSerializer):
    coordinates = serializers.ListField(write_only=True)

    class Meta:
        model = Point
        fields = ('id', 'coordinates')

    def create(self, validated_data):
        coordinates = validated_data.pop('coordinates')
        point = DPoint(coordinates[0], coordinates[1], srid=4326)
        return Point.objects.create(geom=point)
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'type': 'Point',
            'coordinates': instance.geom.coords
        }

class LineStringSerializer(serializers.ModelSerializer):
    coordinates = serializers.ListField(write_only=True)

    class Meta:
        model = LineString
        fields = ('id', 'coordinates')

    def create(self, validated_data):
        coordinates = validated_data.pop('coordinates')
        linestring = DLineString(coordinates, srid=4326)
        return LineString.objects.create(geom=linestring)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'type': 'LineString',
            'coordinates': instance.geom.coords
        }

class PolygonSerializer(serializers.ModelSerializer):
    coordinates = serializers.ListField(write_only=True)

    class Meta:
        model = Polygon
        fields = ('id', 'coordinates')

    def create(self, validated_data):
        coordinates = validated_data.pop('coordinates')
        linear_ring = LinearRing(coordinates[0])
        polygon = DPolygon(linear_ring, srid=4326)
        return Polygon.objects.create(geom=polygon)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'type': 'Polygon',
            'coordinates': instance.geom.coords
        }
