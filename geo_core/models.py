from django.contrib.gis.db import models

class Point(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.PointField(srid=4326)

class LineString(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.LineStringField(srid=4326)

class Polygon(models.Model):
    id = models.AutoField(primary_key=True)
    geom = models.PolygonField(srid=4326)