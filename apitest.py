# API used https://zoo-animal-api.herokuapp.com

import requests
from pprint import pprint as pp

# Test of the zoo animals API
endpoint1 = 'https://zoo-animal-api.herokuapp.com/animals/rand'
response = requests.get(endpoint1)
data = response.json()
pp(data)
print(data['name'])

