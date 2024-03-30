import requests
from django.http import JsonResponse
from requests import Response
from requests.exceptions import HTTPError, JSONDecodeError

from hotels_service.serializers.supplier import (
    SupplierAcmeResponseSerializer,
    SupplierPaperfliesResponseSerializer,
    SupplierPatagoniaResponseSerializer,
)


class SupplierClient:
    """Interface to get supplier data."""

    def __init__(self):
        self.domain = "https://5f2be0b4ffc88500167b85a0.mockapi.io/suppliers"

    def validate_response(
        self, response: Response, custom_error_msg: str
    ) -> JsonResponse:
        try:
            response.raise_for_status()
            return response.json()
        except (HTTPError, JSONDecodeError) as e:
            raise ValueError(f"{custom_error_msg}, msg: {e}") from e

    def get_acme_supplier_data(self) -> dict:
        response = requests.get(
            f"{self.domain}/acme",
            headers={
                "Accept": "application/json",
            },
        )
        response_data = self.validate_response(
            response,
            "Failed to get supplier data from acme.",
        )
        serializer = SupplierAcmeResponseSerializer(data=response_data, many=True)
        serializer.is_valid(raise_exception=True)

        return serializer.to_representation(serializer.validated_data)

    def get_patagonia_supplier_data(self) -> dict:
        response = requests.get(
            f"{self.domain}/patagonia",
            headers={
                "Accept": "application/json",
            },
        )
        response_data = self.validate_response(
            response,
            "Failed to get supplier data from patagonia.",
        )

        serializer = SupplierPatagoniaResponseSerializer(data=response_data, many=True)
        serializer.is_valid(raise_exception=True)

        return serializer.to_representation(serializer.validated_data)

    def get_paperflies_supplier_data(self) -> dict:
        response = requests.get(
            f"{self.domain}/paperflies",
            headers={
                "Accept": "application/json",
            },
        )
        response_data = self.validate_response(
            response,
            "Failed to get supplier data from paperflies.",
        )

        serializer = SupplierPaperfliesResponseSerializer(data=response_data, many=True)
        serializer.is_valid(raise_exception=True)

        return serializer.to_representation(serializer.validated_data)
