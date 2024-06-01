import requests
import json

URL = 'http://localhost:8080/artists'

# Populate the database with artists 
def populate_artists():
    json_file = open('data/artists.json')
    artists = json.load(json_file)
    for artist in artists:
        response = requests.post(f'{URL}/create', data=json.dumps(artist), headers={'Content-Type': 'application/json'})
        print(response.json())

# Get all artists from the database
def get_artists():
    response = requests.get(URL)
    json_response = response.json()
    print(json.dumps(json_response, indent=4))

# 