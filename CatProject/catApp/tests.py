from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .serializers import CatSerializer

class post_cat_test(APITestCase):
    def setUp(self):
        self.cat_url = reverse('cat_list')
        self.cat_data = {
            "name": "Test Cat",
            "price": 1000.00,
            "breed": "Test Breed",
            "discription": "Test Discription",
        }
        return super().setUp()

    def test_can_create_cat(self):
        response = self.client.post(self.cat_url, self.cat_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class get_cat_list(APITestCase):
    def setUp(self):
        self.cat_url = reverse('cat_list')
        return super().setUp()

    def test_can_get_cat(self):
        response = self.client.get(self.cat_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class get_cat_detail(APITestCase):
    def setUp(self):
        self.cat_data = {
            "name": "Test Cat",
            "price": 1000.00,
            "breed": "Test Breed",
            "discription": "Test Discription",
        }
        self.response = self.client.post(reverse('cat_list'), self.cat_data)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.cat_url = reverse('cat_detail', kwargs={'pk': 1})
        return super().setUp()

    def test_can_get_cat(self):
        response = self.client.get(self.cat_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class put_cat_test(APITestCase):
    def setUp(self):
        self.cat_data = {
            "name": "Test Cat",
            "price": 1000.00,
            "breed": "Test Breed",
            "discription": "Test Discription",
        }
        self.response = self.client.post(reverse('cat_list'), self.cat_data)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.cat_url = reverse('cat_detail', kwargs={'pk': 1})
        return super().setUp()

    def test_can_put_cat(self):
        self.cat_data = {
            "name": "Test Cat2",
            "price": 1000.00,
            "breed": "Test Breed2",
            "discription": "Test Discription2",
        }
        response = self.client.put(self.cat_url, self.cat_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class delete_cat(APITestCase):
    def setUp(self):
        self.cat_data = {
            "name": "Test Cat",
            "price": 1000.00,
            "breed": "Test Breed",
            "discription": "Test Discription",
        }
        self.response = self.client.post(reverse('cat_list'), self.cat_data)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.cat_url = reverse('cat_detail', kwargs={'pk': 1})
        return super().setUp()

    def test_can_delete_cat(self):
        response = self.client.delete(self.cat_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)