import requests
import json
from SECRET_STUFF import *

# Set up the necessary variables
client_id = CLIENT_ID
client_secret = CLIENT_SECRET

# Retrieve an access token using client credentials flow
token_url = "https://accounts.spotify.com/api/token"
method = "POST"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
data = {"grant_type": "client_credentials"}
auth = (client_id, client_secret)
response = requests.request(method, token_url, headers=headers, data=data, auth=auth)
access_token = json.loads(response.text)["access_token"]

# Use the access token to search for a track
query = "yellow submarine"
search_url = f"https://api.spotify.com/v1/search?q={query}&type=track"
headers = {"Authorization": f"Bearer {access_token}"}
response = requests.get(search_url, headers=headers)
track_id = json.loads(response.text)["tracks"]["items"][0]["id"]

# Use the access token and track ID to retrieve the track details
track_url = f"https://api.spotify.com/v1/tracks/{track_id}"
response = requests.get(track_url, headers=headers)
track_data = json.loads(response.text)

# Print the track details
print(f'Track name: {track_data["name"]}')
print(f'Artist name: {track_data["artists"][0]["name"]}')
print(f'Album name: {track_data["album"]["name"]}')
