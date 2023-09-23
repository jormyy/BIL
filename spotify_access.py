from requests import get, post, put
import base64
import json
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth


load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

SCOPES = "user-modify-playback-state"


def get_token():
    auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token


def get_auth_header(token):
    return {"Authorization": f"Bearer {token}"}


def search_song(token, song_query):
    url = f"https://api.spotify.com/v1/search?q={song_query}&type=track"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]["items"]
    # song_uri = sorted(json_result, key=lambda x: x["popularity"], reverse=True)[0]["uri"]
    song_uri = json_result[0]["uri"]
    return song_uri
    

# Set up authentication
def authenticate():
    
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                client_secret=CLIENT_SECRET,
                                                redirect_uri="http://localhost:5000/callback",
                                                scope="user-modify-playback-state"))
    return sp
