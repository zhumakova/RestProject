from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import *

from django.contrib.auth.models import User

class RegisterTest(APITestCase):

    def setUp(self)->None:
        self.url=reverse('register')

    def test_register_ok(self):
        date={

                "username": "maksimka1234",
                "password": "123456",
                "check_password": "123456",
                "profile": {
                    "full_name": "maksimka",
                    "address":"troitskaya",
                    "wallet":50000,
                    "email":"a@j"
                }

        }
        self.response=self.client.post(self.url,date,format='json')
        self.assertEqual(self.response.status_code,201)