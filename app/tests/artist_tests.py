import requests
import json

def get_artist():
    url = 'http://localhost:8080/artists/' 
    response = requests.get(url)
    return response.json()

get_artist()

    
