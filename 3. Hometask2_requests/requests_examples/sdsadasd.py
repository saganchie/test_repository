import json
import requests

body_route = {
    "cities": [
        {
            "city_id": 3611
        },
        {
            "city_id": 120
        }
    ],
    "delays": {
        "0": 0,
        "1": 5,
        "2": 10,
        "3": 15,
        "4": 30,
        "5": 60,
        "6": 90,
        "7": 60,
        "8": 120
    },
    "speeds": {
        "0": 40,
        "1": 40,
        "2": 60,
        "3": 60,
        "4": 70,
        "5": 80,
        "6": 30,
        "10": 20
    },
    "options": {
        "shortest_route": 0,
        "allow_winter_roads": 0,
        "allow_ferries": 0,
        "within_country": 0,
        "allow_toll_roads": 1,
        "exclude_mkad": 1,
        "use_belarus_rule": 0
    },
    "excluded_cities": [

    ],
    "excluded_regions": [

    ],
    "excluded_countries": [

    ],
    "loading_points": [

    ],
    "unloading_points": [

    ],
    "departure_date_utc": "2021-02-08T06:00:00Z",
    "work_day": {
        "work_day_start_time": "09:00:00",
        "working_hours": 8,
        "daily_mileage": 500
    }
}

response = requests.post("http://prod.distancer-api.service.spb.atiprod:4242/webapi/distancer/v2/city_route",
                         json=body_route)

print(json.dumps(response.json(), indent=4))
