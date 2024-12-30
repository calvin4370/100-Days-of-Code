from bs4 import BeautifulSoup as BS
import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Ask user to input date for Billboard 100
# date = input('Which date do you want to travel to? (YYYY-MM-DD): ')
date = '2024-12-25'

# Get a response from url
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0'}
url = 'https://www.billboard.com/charts/hot-100/' + date
response = requests.get(url=url, headers=headers)

# Make the soup
soup = BS(response.text, 'lxml')
song_name_h3 = soup.select('li ul li h3') # select all h3 within a li ul li h3 chain
song_artist_spans = soup.select('div ul li ul li span') # select all spans within a li ul li span chain with class="..."

# Make a list of the Billboard Top 100 songs at the specified date
song_names = [song.getText().strip() for song in song_name_h3]
song_artists = [song.getText().strip() for song in song_artist_spans[::7]]
songs = [(name, artist) for name, artist in zip(song_names, song_artists)]

# Spotify
# Get secret tokens from gitignored json file
with open('tokens.json') as file:
    tokens = json.load(file)
CLIENT_ID = tokens['client_id']
CLIENT_SECRET = tokens['client_secret']
REDIRECT_URI = tokens['spotify_redirect_url']

# Setup Spotipy
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope='playlist-modify-private'))

# Get list of Spotify Song URIs for each song in Top 100 Billboard
song_uris = []
year = date.split("-")[0]
for name, artist in songs:
    result = sp.search(q=f"track:{name} year:{year}", # artist: {artist} restricts the search too much, very hard to find
                       type="track",
                       limit=1)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{name} doesn't exist in Spotify. Skipped.")

print(f"Collected Spotify track URI's for {len(song_uris)} tracks")

# Create a private playlist in my Spotify account
playlist = sp.user_playlist_create(sp.me()["id"], name=f'{date} Billboard Top 100', public=False, collaborative=False, description='100 Days of Code Day 46: Create a Spotify Time MAchine playlist')

print('Created playlist')

# Add the songs in
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(f'Added {len(song_uris)} tracks to playlist')
