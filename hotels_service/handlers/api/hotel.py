from collections import defaultdict

from hotels_service.core import helpers
from hotels_service.core.supplier import SupplierClient


def get_hotel_data_from_suppliers(hotel_ids: list[str], destination_id: int) -> list:
    supplier_client = SupplierClient()

    acme_data = supplier_client.get_acme_supplier_data()
    patagonia_data = supplier_client.get_patagonia_supplier_data()
    paperflies_data = supplier_client.get_paperflies_supplier_data()

    if len(hotel_ids) > 0:
        grouped_data = group_suppliers_data_by_hotel_id(
            hotel_ids, acme_data, patagonia_data, paperflies_data
        )
    else:
        grouped_data = group_suppliers_data_by_destination_id(
            destination_id, acme_data, patagonia_data, paperflies_data
        )

    cleaned_hotel_data = []
    for _, data in grouped_data.items():
        cleaned_hotel_data.append(clean_hotel_data(data))

    return cleaned_hotel_data


def group_suppliers_data_by_hotel_id(hotel_ids: list[str], *supplier_data) -> dict:
    grouped_data = defaultdict(list)
    hotels_list = [hotel for hotels_list in supplier_data for hotel in hotels_list]

    for hotel in hotels_list:
        if hotel["hotel_id"] in hotel_ids:
            grouped_data[hotel["hotel_id"]].append(hotel)

    return grouped_data


def group_suppliers_data_by_destination_id(destination_id: int, *supplier_data) -> dict:
    grouped_data = defaultdict(list)
    hotels_list = [hotel for hotels_list in supplier_data for hotel in hotels_list]

    for hotel in hotels_list:
        if (hotel["destination_id"]) == (destination_id):
            grouped_data[hotel["destination_id"]].append(hotel)

    return grouped_data


def clean_hotel_data(hotel_list: list) -> dict:
    return {
        "hotel_id": hotel_list[0]["hotel_id"],
        "destination_id": hotel_list[0]["destination_id"],
        "location": {
            "lat": helpers.get_first_value(
                [hotel.get("location", {}).get("lat", "") for hotel in hotel_list]
            ),
            "lng": helpers.get_first_value(
                [hotel.get("location", {}).get("lng", "") for hotel in hotel_list]
            ),
            "address": helpers.get_longest_length(
                [hotel.get("location", {}).get("address", "") for hotel in hotel_list]
            ),
            "city": helpers.get_first_value(
                [hotel.get("location", {}).get("city", "") for hotel in hotel_list]
            ),
            "country": helpers.get_longest_length(
                [hotel.get("location", {}).get("country", "") for hotel in hotel_list]
            ),
        },
        "description": helpers.get_longest_length(
            [hotel.get("description", "") for hotel in hotel_list]
        ),
        "amenities": {
            "general": list(
                {
                    amenity.strip().lower().replace(" ", "")
                    for hotel in hotel_list
                    for amenity in hotel["amenities"]["general"]
                }
            ),
            "room": list(
                {
                    amenity.strip().lower().replace(" ", "")
                    for hotel in hotel_list
                    for amenity in hotel["amenities"]["room"]
                }
            ),
        },
        "images": {
            "rooms": helpers.remove_duplicates_in_list(
                [
                    rooms
                    for hotel in hotel_list
                    for rooms in hotel.get("images", {}).get("rooms", {})
                ]
            ),
            "site": helpers.remove_duplicates_in_list(
                [
                    site
                    for hotel in hotel_list
                    for site in hotel.get("images", {}).get("site", {})
                ]
            ),
            "amenities": helpers.remove_duplicates_in_list(
                [
                    amenities
                    for hotel in hotel_list
                    for amenities in hotel.get("images", {}).get("amenities", {})
                ]
            ),
        },
        "booking_conditions": list(
            {
                condition
                for hotel in hotel_list
                for condition in hotel.get("booking_conditions", [])
            }
        ),
    }
