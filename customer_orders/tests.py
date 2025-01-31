from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Customers, Order




class CustomerOrderTests(TestCase):
    def setUp(self):
     self.client = APIClient()
     self.customer = Customers.objects.create(name="Shannel Rikk", code="JD123")

    def test_create_customer(self):
        url = reverse('customer-list-create')
        data = {'name': 'Wanga Rodd', 'code': 'JD456'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 20)




