import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestCrawler(APITestCase):
    def test_can_get_result(self):
        url = reverse('crawler')
        data = {
          # Não pode ser repetido, caso seja ele retornara o resultado só 1 vez
          "urls": ["https://marcobarao.github.io/", "https://twitter.com/marcobrunobr"],
          "word": "Marco"
        }
        qt_urls = len(data["urls"])
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), qt_urls)