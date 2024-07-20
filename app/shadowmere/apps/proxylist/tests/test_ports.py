import json

from django.urls import reverse
from rest_framework.test import APITestCase


class PortsEndpointTests(APITestCase):
    fixtures = ["proxies.json"]

    def test_ports(self):
        response = self.client.get(reverse("ports-list"))
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)
        self.assertEqual(result, [{"port": 807}, {"port": 2375}, {"port": 8091}])
