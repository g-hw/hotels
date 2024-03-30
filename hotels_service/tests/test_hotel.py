from unittest.mock import Mock, patch

from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.test import APITestCase


class TestHotel(APITestCase):
    @patch("hotels_service.core.supplier.requests.get")
    def test_get_hotels__success_with_destination(self, mock_response):
        mock_res = Mock()
        mock_res.json = Mock(return_value=[])
        mock_response.return_value = mock_res

        response = self.client.post(
            reverse("get-hotels"), format="json", data={"destination": 5432}
        )

        self.assertEqual(response.status_code, HTTP_200_OK)

    @patch("hotels_service.core.supplier.requests.get")
    def test_get_hotels__success_with_hotels(self, mock_response):
        mock_res = Mock()
        mock_res.json = Mock(return_value=[])
        mock_response.return_value = mock_res

        response = self.client.post(
            reverse("get-hotels"), format="json", data={"hotels": ["a"]}
        )

        self.assertEqual(response.status_code, HTTP_200_OK)

    @patch("hotels_service.core.supplier.requests.get")
    def test_get_hotels__invalid_request(self, mock_response):
        mock_res = Mock()
        mock_res.json = Mock(return_value=[])
        mock_response.return_value = mock_res

        response = self.client.post(
            reverse("get-hotels"), format="json", data={"destination": [5432]}
        )

        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
