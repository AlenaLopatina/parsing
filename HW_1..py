import requests
import json

URL = 'https://api.github.com/'
name = 'AlenaLopatina'
node = f'users/{name}/repos'
response = requests.get(url=URL + node)
response = response.json()

with open('response.json', 'w') as file:
    json.dump(response, file)

for el in response:
    print(el['name'])