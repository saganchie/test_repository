import pprint
import requests

# Про передачу параметров
respons = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# print(respons.json()['userId'])

# print("\n------- status/headers/encoding ---------")
#
# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
#
# print("\n----------------- text ------------------")
# print(r.text)
# print("\n----------------- json ------------------")
#
# print(r.json())
#
# print("\n---------------- headers ----------------")

for key, value in respons.headers.items():
    print(key, ' => ', value)
