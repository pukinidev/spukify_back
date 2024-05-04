import json
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

client_credential_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credential_manager)


"""
Retrieve Artist Information
Parameters:
    - uri: str -> Spotify URI of the artist
"""

def get_artists() -> list:
    artists = []
    for i in range(0, 400, 50):
        results = sp.search(q='year:2024', type='artist', limit=50, offset=i)
        for artist in results['artists']['items']:
            artists.append(artist)
    return artists

def get_artist_albums(artist_uri: str) -> list:
    albums = []
    for i in range(0, 100, 50):
        results = sp.artist_albums(artist_uri, album_type='album', limit=50, offset=i)
        for album in results['items']:
            albums.append(album)
    return albums


get_artist_albums('spotify:artist:06HL4z0CvFAxyc27GXpf02')