# API used https://zoo-animal-api.herokuapp.com
import requests


# Function to get a random animal from the API. Returns dictionary of the card
def get():
    endpoint1 = 'https://zoo-animal-api.herokuapp.com/animals/rand'
    response = requests.get(endpoint1)
    data = response.json()
    return data


