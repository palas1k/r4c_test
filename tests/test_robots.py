from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from robots.models import Robot


class RobotAPITests(APITestCase):

    def setUp(self):
        self.valid_model1 = Robot.objects.create(model='R2', version='1.0', created='2010-12-31T23:59:59')
        self.url = reverse('robot_create')

    def test_create_robot_valid(self):
        data = {
            "model": "R2",
            "version": "D2",
            "created": "2024-12-15 18:42:53"
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Robot.objects.count(), 2)
        self.assertEqual(Robot.objects.first().model, "R2")

    def test_create_robot_invalid_model(self):
        data = {
            "model": "InvalidModel",
            "version": "D2",
            "created": "2022-12-31 23:59:59"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_robot_missing_fields(self):
        data = {
            "model": "R2",
            "version": "D2"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_robot_invalid_date_format(self):
        """Test creating a robot with an invalid date format."""
        data = {
            "model": "R2",
            "version": "D2",
            "created": "invalid-date-format"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)