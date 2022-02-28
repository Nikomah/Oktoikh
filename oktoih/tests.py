
from django.test import TestCase
from django.urls import reverse


class VoicesTestCase(TestCase):
    def test_get(self):
        url = reverse('voices', args=[3])
        print(url)
        response = self.client.get(url)
        print(response.status_code)
