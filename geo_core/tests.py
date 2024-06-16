from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Point, LineString, Polygon

class GeoAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.point_data_1 = {
            "type": "Point",
            "coordinates": [10, 15]
        }
        self.linestring_data_1 = {
            "type": "LineString",
            "coordinates": [[10, 20], [30, 40]]
        }
        self.polygon_data = {
            "type": "Polygon",
            "coordinates": [[[12.4924, 41.8902], [12.4925, 41.8903], [12.4926, 41.8904], [12.4924, 41.8902]]]
        }

    def test_create_and_get_point(self):
        # Create point
        response = self.client.post(reverse('point-list'), self.point_data_1, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        point_id = response.data['id']

        # Get point
        response = self.client.get(reverse('point-detail', args=[point_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(list(response.data['coordinates']), self.point_data_1['coordinates'])

    def test_create_and_get_linestring(self):
        # Create linestring
        response = self.client.post(reverse('linestring-list'), self.linestring_data_1, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        linestring_id = response.data['id']

        # Get linestring
        response = self.client.get(reverse('linestring-detail', args=[linestring_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual([list(coord) for coord in response.data['coordinates']], self.linestring_data_1['coordinates'])

    def test_create_and_get_polygon(self):
        # Create polygon
        response = self.client.post(reverse('polygon-list'), self.polygon_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        polygon_id = response.data['id']

        # Get polygon
        response = self.client.get(reverse('polygon-detail', args=[polygon_id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual([[list(coord) for coord in ring] for ring in response.data['coordinates']], self.polygon_data['coordinates'])