from rest_framework import serializers

from hotels_service.core.constants import GENERAL_AMENITIES, ROOM_AMENITIES
from hotels_service.core.helpers import compare_list


class SupplierAcmeResponseSerializer(serializers.Serializer):
    Id = serializers.CharField()
    DestinationId = serializers.IntegerField()
    Name = serializers.CharField()
    Latitude = serializers.CharField(allow_null=True, allow_blank=True)
    Longitude = serializers.CharField(allow_null=True, allow_blank=True)
    Address = serializers.CharField()
    City = serializers.CharField()
    Country = serializers.CharField()
    PostalCode = serializers.CharField()
    Description = serializers.CharField()
    Facilities = serializers.ListField(child=serializers.CharField())

    def to_representation(self, instance):
        data = super().to_representation(instance)

        return {
            "hotel_id": data["Id"],
            "destination_id": data["DestinationId"],
            "name": data["Name"],
            "location": {
                "lat": float(data["Latitude"]) if data["Latitude"] else None,
                "lng": float(data["Longitude"]) if data["Longitude"] else None,
                "address": f"{data['Address']}, {data['PostalCode']}",
                "city": data["City"],
                "country": data["Country"],
            },
            "description": data["Description"],
            "amenities": {
                "room": compare_list(data.get("Facilities", []), ROOM_AMENITIES),
                "general": compare_list(data.get("Facilities", []), GENERAL_AMENITIES),
            },
        }


class SupplierPatagoniaResponseSerializer(serializers.Serializer):
    class _ImagesDetailSerializer(serializers.Serializer):
        class _RoomsAmenitiesSerializer(serializers.Serializer):
            url = serializers.CharField()
            description = serializers.CharField()

        rooms = serializers.ListField(child=_RoomsAmenitiesSerializer())
        amenities = serializers.ListField(child=_RoomsAmenitiesSerializer())

    id = serializers.CharField()
    destination = serializers.IntegerField()
    name = serializers.CharField()
    lat = serializers.FloatField()
    lng = serializers.FloatField()
    address = serializers.CharField(allow_null=True)
    info = serializers.CharField(allow_null=True)
    amenities = serializers.ListField(child=serializers.CharField(), allow_null=True)
    images = _ImagesDetailSerializer()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {
            "hotel_id": data["id"],
            "destination_id": data["destination"],
            "name": data["name"],
            "location": {
                "lat": data["lat"],
                "lng": data["lng"],
                "address": data["address"],
            },
            "description": data["info"],
            "amenities": {
                "room": compare_list(data.get("amenities", []), ROOM_AMENITIES),
                "general": compare_list(data.get("amenities", []), GENERAL_AMENITIES),
            },
            "images": {
                "rooms": [
                    {"link": d["url"], "description": d["description"]}
                    for d in data["images"]["rooms"]
                ],
                "amenities": [
                    {"link": d["url"], "description": d["description"]}
                    for d in data["images"]["amenities"]
                ],
            },
        }


class SupplierPaperfliesResponseSerializer(serializers.Serializer):
    class _LocationSerializer(serializers.Serializer):
        address = serializers.CharField()
        country = serializers.CharField()

    class _AmenitiesSerializer(serializers.Serializer):
        general = serializers.ListField(child=serializers.CharField())
        room = serializers.ListField(child=serializers.CharField())

    class _ImagesSerializer(serializers.Serializer):
        class _RoomsAndSiteSerializer(serializers.Serializer):
            link = serializers.CharField()
            caption = serializers.CharField()

        rooms = serializers.ListField(child=_RoomsAndSiteSerializer())
        site = serializers.ListField(child=_RoomsAndSiteSerializer())

    hotel_id = serializers.CharField()
    destination_id = serializers.IntegerField()
    hotel_name = serializers.CharField()
    location = _LocationSerializer()
    details = serializers.CharField()
    amenities = _AmenitiesSerializer()
    images = _ImagesSerializer()
    booking_conditions = serializers.ListField(child=serializers.CharField())

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["description"] = data.pop("details")
        data["images"]["rooms"] = [
            {"link": d.pop("link"), "description": d.pop("caption")}
            for d in data["images"]["rooms"]
        ]
        data["images"]["site"] = [
            {"link": d.pop("link"), "description": d.pop("caption")}
            for d in data["images"]["site"]
        ]
        return data
