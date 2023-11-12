from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetUp(APITestCase):
    def setUp(self):
        self.product_list = reverse('product-list')
        self.auth_token = reverse('auth-token')
        return super().setUp()

    def tearDown(self):
        return super().tearDown()