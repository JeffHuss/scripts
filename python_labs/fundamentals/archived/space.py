import requests
import json

response = requests.get('http://api.open-notify.org/astros.json').json()
formatted_json = json.dumps(response, indent=4)
# print(formatted_json)

for person in response['people']:
    print(person)

print(formatted_json)