import requests
from SECRET_STUFF import *
import base64, json

# https://developer.spotify.com/documentation/web-api
# läs under "Getting started" för att få client_id och client_Secret


def get_token():
    AUTH_URL = "https://accounts.spotify.com/api/token"

    # POST
    auth_response = requests.post(
        AUTH_URL,
        {
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        },
    )

    # convert the response to JSON
    auth_response_data = auth_response.json()

    # save the access token
    access_token = auth_response_data["access_token"]

    return access_token


token = get_token()
print(token)
