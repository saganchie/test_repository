import requests

body_route = {
    "cities": [
        3611,
        2747,
        1070,
        2934,
        120,
        270,
        1189,
        3611
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
        "shortestRoute": 1,
        "allowWinterRoads": 1,
        "allowFerries": 0,
        "withinCountry": 0,
        "allowTollRoads": 1,
        "excludeMkad": 1,
        "useBelarusRule": 0
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

# headers = {
#     "X-API-Secret":"2ed277e5cac34fe1be8c7762a599161d"
# }

response = requests.post("http://staging-4:4242/webapi/distancer/route",
                        json=body_route)

if response.status_code == 200:
    print("OK!")
#
# if response.json() == "тут должно быть ожидаемое тело ответа":
#     print("Ништяк!")
# else:
#     print("Кизяк!")

print(response.json())