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
            "coordinates": [[10.0000, 20.0000], [30.0000, 40.0000]]
        }
        self.linestring_data_2 = {
            "type": "LineString",
            "coordinates": [[40.0000, 40.0000], [45.0000, 50.0000]]
        }
        self.polygon_data = {
            "type": "Polygon",
            "coordinates": [[[10, 40], [20, 40], [20, 30], [10, 30], [10, 40]]]
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

    def test_join_lines(self):
        # Create linestrings
        response = self.client.post(reverse('linestring-list'), self.linestring_data_1, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        linestring_id_1 = response.data['id']

        response = self.client.post(reverse('linestring-list'), self.linestring_data_2, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        linestring_id_2 = response.data['id']

        # Join lines
        join_data = {
            "lines": [linestring_id_1, linestring_id_2]
        }
        response = self.client.post(reverse('join_lines'), join_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        expected_joined_coordinates = [[10.0000, 20.0000], [30.0000, 40.0000], [40.0000, 40.0000], [45.0000, 50.0000]]
        self.assertEqual([list(coord) for coord in response.data['coordinates']], expected_joined_coordinates)