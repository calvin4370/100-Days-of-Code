import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

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

# Access Hoshimachi Suisei's Spotify page using her Spotify URI (Uniform Resource Indicator)
SUISEI_URI = 'spotify:artist:726WiFmWkohzodUxK3XjHX'

# Access her albums
results = sp.artist_albums(SUISEI_URI, album_type='album')
albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

print("Suisei's Albums: ")
for album in albums:
    print(album['name'])

# Access her top tracks
# Each track is a dict
results = sp.artist_top_tracks(SUISEI_URI, country='SG')
tracks = results['tracks']
print("\nSuisei's Top Tracks: ")
for track in tracks: # Each track is a dict
    track_name = track['name']
    print(track_name)