from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import *
from Product.models import Category
from django.contrib.auth.models import User
class CommentTest(APITestCase):

    def setUp(self)->None:
        self.user=User.objects.create_user(username='maksim',password='123456')
        self.profile=Profile.objects.create(user=self.user,full_name='maksimka')
        self.category=Category.objects.create(title='laptop')
        self.product=Product.objects.create(name='razer blade',category=self.category,
                                            desc='some text',price=50000,
                                            )

        self.url=reverse('product_detail',args=(self.product.id,))

    def test_comment_successful(self):
        self.client.login(username='maksim',password='123456')
        data={
            "text":'good laptop'
        }
        self.response=self.client.post(self.url,data)

    def test_comment_with_bad_words(self):
        self.client.login(username='maksim',password='123456')
        data={
            "text":'baf laptop!'
        }
        self.response = self.client.post(self.url, data)

class RateTest(APITestCase):

    def setUp(self)->None:
        self.user=User.objects.create_user(username='maksim',password='123456')
        self.profile=Profile.objects.create(user=self.user,full_name='maksimka')
        self.category=Category.objects.create(title='laptop')
        self.product=Product.objects.create(name='razer blade',category=self.category,
                                            desc='some text',price=50000,
                                            )

        self.url = reverse('score', args=(self.product.id,))

    def test_score_create(self):
        self.client.login(username='maksim', password='123456')
        data = {
            "score":4.1
        }
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code,201)