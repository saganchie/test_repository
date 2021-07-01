import requests
import hashlib
import json
import pytest

body_route_base = {
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
    "excludedCities": [

    ],
    "excludedRegions": [

    ],
    "excludedCountries": [

    ],
    "loadingPoints": [

    ],
    "unloadingPoints": [

    ],
    "departureDateUtc": "2021-02-08T06:00:00Z",
    "workDay": {
        "workDayStartTime": "09:00:00",
        "workingHours": 8,
        "dailyMileage": 500
    }
}

body_route_cities = {"cities": [
    {
        "city_id": 3611
    },
    {
        "city_id": 120
    }
]}

body_route_options = {"options": {
    "shortest_route": True,
    "allow_winter_roads": False,
    "allow_ferries": False,
    "within_country": False,
    "allow_toll_roads": True,
    "exclude_mkad": True,
    "use_belarus_rule": True
}}


def create_obj_body(cities, options):
    new_body = {}
    new_body.update(body_route_base)
    new_body.update(cities)
    new_body.update(options)

    return new_body


class DistancerPew:
    def __init__(self, url):
        self.url = url

    def send_request(self, cities, options):
        # request_body = {
        #     'body_route_cities': cities,
        #     'body_route_base': base,
        #     'body_route_options': options
        # }
        request_body1 = create_obj_body(cities, options)
        response = requests.post(self.url, json=request_body1)
        return response.json()


def test_distance_route():
    pew = DistancerPew("http://prod.distancer-api.service.spb.atiprod:4242/webapi/distancer/v2/city_route")
    resp = pew.send_request(body_route_cities, body_route_options)

    #    return resp
    #    print(resp)

    with open('etalon_trace_data.json', 'w') as f:
        json.dump(resp, f)

# test_distance_route()
