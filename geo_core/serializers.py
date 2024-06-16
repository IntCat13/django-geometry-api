from rest_framework import serializers
from django.contrib.gis.geos import Point as DPoint
from .models import Point

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