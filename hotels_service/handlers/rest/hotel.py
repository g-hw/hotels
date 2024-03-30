from drf_yasg import openapi  # type: ignore
from drf_yasg.utils import swagger_auto_schema  # type: ignore
from rest_framework.decorators import api_view
from rest_framework.response import Response

from hotels_service.handlers.api.hotel import get_hotel_data_from_suppliers
from hotels_service.serializers.hotel import (
    HotelRequestSerializer,
    HotelsResponseSerializer,
)


@swagger_auto_schema(
    methods=["post"],
    responses={200: openapi.Response("Response format", HotelsResponseSerializer)},
)
@api_view(["POST"])
def get_hotels(request) -> Response:
    """Query hotels data with destination and hotel filtering."""

    serializer = HotelRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    request_body = serializer.validated_data
    hotel_data = get_hotel_data_from_suppliers(
        request_body["hotels"], request_body["destination"]
    )
    return Response(hotel_data)
