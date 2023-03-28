import requests
from SECRET_STUFF import *
import base64

# https://developer.spotify.com/documentation/web-api
# läs under "Getting started" för att få client_id och client_Secret


def get_token():
    auth_string = CLIENT_ID + ":" + CLIENT_SECRET
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "httpps://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic" + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headerrs=headers, data=data)
    json_result = json.loads(result)
