from rest_framework import serializers


class HotelRequestSerializer(serializers.Serializer):
    hotels = serializers.ListField(
        child=serializers.CharField(), required=False, default=[]
    )
    destination = serializers.IntegerField(required=False, default=0)


class HotelsResponseSerializer(serializers.Serializer):
    class _LocationSerializer(serializers.Serializer):
        address = serializers.CharField()
        country = serializers.CharField()

    class _AmenitiesSerializer(serializers.Serializer):
        general = serializers.ListField(child=serializers.CharField())
        room = serializers.ListField(child=serializers.CharField())

    class _ImagesSerializer(serializers.Serializer):
        class _RoomsAndSiteSerializer(serializers.Serializer):
            link = serializers.CharField()
            description = serializers.CharField()

        rooms = serializers.ListField(child=_RoomsAndSiteSerializer())
        site = serializers.ListField(child=_RoomsAndSiteSerializer())
        amenities = serializers.ListField(child=_RoomsAndSiteSerializer())

    hotel_id = serializers.CharField()
    destination_id = serializers.IntegerField()
    hotel_name = serializers.CharField()
    location = _LocationSerializer()
    description = serializers.CharField()
    amenities = _AmenitiesSerializer()
    images = _ImagesSerializer()
    booking_conditions = serializers.ListField(child=serializers.CharField())
