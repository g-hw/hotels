from unittest.mock import Mock, patch

from rest_framework.test import APITestCase

from hotels_service.core.supplier import SupplierClient


class TestHotel(APITestCase):
    @patch("hotels_service.core.supplier.requests.get")
    def test_get_acme_supplier_data__success(self, mock_response):
        mock_res = Mock()
        mock_res.json = Mock(
            return_value=[
                {
                    "Id": "iJhz",
                    "DestinationId": 5432,
                    "Name": "Beach Villas Singapore",
                    "Latitude": 1.264751,
                    "Longitude": 103.824006,
                    "Address": " 8 Sentosa Gateway, Beach Villas ",
                    "City": "Singapore",
                    "Country": "SG",
                    "PostalCode": "098269",
                    "Description": "  This 5 star hotel is located on the coastline of Singapore.",
                    "Facilities": [
                        "Pool",
                        "BusinessCenter",
                        "WiFi ",
                        "DryCleaning",
                        " Breakfast",
                    ],
                }
            ]
        )
        mock_response.return_value = mock_res

        response = SupplierClient().get_acme_supplier_data()
        self.assertEqual(
            response,
            [
                {
                    "hotel_id": "iJhz",
                    "destination_id": 5432,
                    "name": "Beach Villas Singapore",
                    "location": {
                        "lat": 1.264751,
                        "lng": 103.824006,
                        "address": "8 Sentosa Gateway, Beach Villas, 098269",
                        "city": "Singapore",
                        "country": "SG",
                    },
                    "description": "This 5 star hotel is located on the coastline of Singapore.",
                    "amenities": {
                        "room": [],
                        "general": [
                            "Pool",
                            "BusinessCenter",
                            "WiFi",
                            "DryCleaning",
                            "Breakfast",
                        ],
                    },
                }
            ],
        )

    @patch("hotels_service.core.supplier.requests.get")
    def test_get_patagonia_supplier_data__success(self, mock_response):
        mock_res = Mock()
        mock_res.json = Mock(
            return_value=[
                {
                    "id": "iJhz",
                    "destination": 5432,
                    "name": "Beach Villas Singapore",
                    "lat": 1.264751,
                    "lng": 103.824006,
                    "address": "8 Sentosa Gateway, Beach Villas, 098269",
                    "info": "Located at the western tip of Resorts World Sentosa, guests at the Beach Villas are guaranteed privacy while they enjoy spectacular views of glittering waters. Guests will find themselves in paradise with this series of exquisite tropical sanctuaries, making it the perfect setting for an idyllic retreat. Within each villa, guests will discover living areas and bedrooms that open out to mini gardens, private timber sundecks and verandahs elegantly framing either lush greenery or an expanse of sea. Guests are assured of a superior slumber with goose feather pillows and luxe mattresses paired with 400 thread count Egyptian cotton bed linen, tastefully paired with a full complement of luxurious in-room amenities and bathrooms boasting rain showers and free-standing tubs coupled with an exclusive array of ESPA amenities and toiletries. Guests also get to enjoy complimentary day access to the facilities at Asia’s flagship spa – the world-renowned ESPA.",
                    "amenities": [
                        "Aircon",
                        "Tv",
                        "Coffee machine",
                        "Kettle",
                        "Hair dryer",
                        "Iron",
                        "Tub",
                    ],
                    "images": {
                        "rooms": [
                            {
                                "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/2.jpg",
                                "description": "Double room",
                            },
                            {
                                "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/4.jpg",
                                "description": "Bathroom",
                            },
                        ],
                        "amenities": [
                            {
                                "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/0.jpg",
                                "description": "RWS",
                            },
                            {
                                "url": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/6.jpg",
                                "description": "Sentosa Gateway",
                            },
                        ],
                    },
                },
            ]
        )
        mock_response.return_value = mock_res

        response = SupplierClient().get_patagonia_supplier_data()
        self.assertEqual(
            response,
            [
                {
                    "hotel_id": "iJhz",
                    "destination_id": 5432,
                    "name": "Beach Villas Singapore",
                    "location": {
                        "lat": 1.264751,
                        "lng": 103.824006,
                        "address": "8 Sentosa Gateway, Beach Villas, 098269",
                    },
                    "description": "Located at the western tip of Resorts World Sentosa, guests at the Beach Villas are guaranteed privacy while they enjoy spectacular views of glittering waters. Guests will find themselves in paradise with this series of exquisite tropical sanctuaries, making it the perfect setting for an idyllic retreat. Within each villa, guests will discover living areas and bedrooms that open out to mini gardens, private timber sundecks and verandahs elegantly framing either lush greenery or an expanse of sea. Guests are assured of a superior slumber with goose feather pillows and luxe mattresses paired with 400 thread count Egyptian cotton bed linen, tastefully paired with a full complement of luxurious in-room amenities and bathrooms boasting rain showers and free-standing tubs coupled with an exclusive array of ESPA amenities and toiletries. Guests also get to enjoy complimentary day access to the facilities at Asia’s flagship spa – the world-renowned ESPA.",
                    "amenities": {
                        "room": [
                            "Aircon",
                            "Tv",
                            "Coffee machine",
                            "Kettle",
                            "Hair dryer",
                            "Iron",
                            "Tub",
                        ],
                        "general": [],
                    },
                    "images": {
                        "rooms": [
                            {
                                "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/2.jpg",
                                "description": "Double room",
                            },
                            {
                                "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/4.jpg",
                                "description": "Bathroom",
                            },
                        ],
                        "amenities": [
                            {
                                "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/0.jpg",
                                "description": "RWS",
                            },
                            {
                                "link": "https://d2ey9sqrvkqdfs.cloudfront.net/0qZF/6.jpg",
                                "description": "Sentosa Gateway",
                            },
                        ],
                    },
                }
            ],
        )

    @patch("hotels_service.core.supplier.requests.get")
    def test_get_paperflies_supplier_data__success(self, mock_response):
        mock_res = Mock()
        mock_res.json = Mock(
            return_value=[
                {
                    "hotel_id": "SjyX",
                    "destination_id": 5432,
                    "hotel_name": "InterContinental",
                    "location": {
                        "address": "1 Nanson Rd, Singapore 238909",
                        "country": "Singapore",
                    },
                    "details": "InterContinental Singapore Robertson Quay is luxury's preferred address offering stylishly cosmopolitan riverside living for discerning travelers to Singapore. Prominently situated along the Singapore River, the 225-room inspiring luxury hotel is easily accessible to the Marina Bay Financial District, Central Business District, Orchard Road and Singapore Changi International Airport, all located a short drive away. The hotel features the latest in Club InterContinental design and service experience, and five dining options including Publico, an Italian landmark dining and entertainment destination by the waterfront.",
                    "amenities": {
                        "general": [
                            "outdoor pool",
                            "business center",
                            "childcare",
                            "parking",
                            "bar",
                            "dry cleaning",
                            "wifi",
                            "breakfast",
                            "concierge",
                        ],
                        "room": ["aircon", "minibar", "tv", "bathtub", "hair dryer"],
                    },
                    "images": {
                        "rooms": [
                            {
                                "link": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i93_m.jpg",
                                "caption": "Double room",
                            },
                            {
                                "link": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i94_m.jpg",
                                "caption": "Bathroom",
                            },
                        ],
                        "site": [
                            {
                                "link": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i1_m.jpg",
                                "caption": "Restaurant",
                            },
                            {
                                "link": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i2_m.jpg",
                                "caption": "Hotel Exterior",
                            },
                            {
                                "link": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i5_m.jpg",
                                "caption": "Entrance",
                            },
                            {
                                "link": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i24_m.jpg",
                                "caption": "Bar",
                            },
                        ],
                    },
                    "booking_conditions": [],
                },
            ]
        )
        mock_response.return_value = mock_res

        response = SupplierClient().get_paperflies_supplier_data()
        self.assertEqual(
            response,
            [
                {
                    "hotel_id": "SjyX",
                    "destination_id": 5432,
                    "hotel_name": "InterContinental",
                    "location": {
                        "address": "1 Nanson Rd, Singapore 238909",
                        "country": "Singapore",
                    },
                    "amenities": {
                        "general": [
                            "outdoor pool",
                            "business center",
                            "childcare",
                            "parking",
                            "bar",
                            "dry cleaning",
                            "wifi",
                            "breakfast",
                            "concierge",
                        ],
                        "room": ["aircon", "minibar", "tv", "bathtub", "hair dryer"],
                    },
                    "images": {
                        "rooms": [
                            {
                                "link": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i93_m.jpg",
                                "description": "Double room",
                            },
                            {
                                "link": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i94_m.jpg",
                                "description": "Bathroom",
                            },
                        ],
                        "site": [
                            {
                                "link": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i1_m.jpg",
                                "description": "Restaurant",
                            },
                            {
                                "link": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i2_m.jpg",
                                "description": "Hotel Exterior",
                            },
                            {
                                "link": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i5_m.jpg",
                                "description": "Entrance",
                            },
                            {
                                "link": "https://d2ey9sqrvkqdfs.cloudfront.net/Sjym/i24_m.jpg",
                                "description": "Bar",
                            },
                        ],
                    },
                    "booking_conditions": [],
                    "description": "InterContinental Singapore Robertson Quay is luxury's preferred address offering stylishly cosmopolitan riverside living for discerning travelers to Singapore. Prominently situated along the Singapore River, the 225-room inspiring luxury hotel is easily accessible to the Marina Bay Financial District, Central Business District, Orchard Road and Singapore Changi International Airport, all located a short drive away. The hotel features the latest in Club InterContinental design and service experience, and five dining options including Publico, an Italian landmark dining and entertainment destination by the waterfront.",
                }
            ],
        )
