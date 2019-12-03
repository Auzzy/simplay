import json
import os

import spotipy
import spotipy.util
from flask import redirect, request, url_for
from spotipy.oauth2 import SpotifyOAuth

from simplay.simplay import app

REDIRECT_URL = "https://1c9f59b10f9d4ae781e43f0130a11721.vfs.cloud9.us-east-1.amazonaws.com/auth"

def _get_access_token():
    pass

@app.route("/")
def home():
    auth_obj = SpotifyOAuth(os.environ.get("SPOTIPY_CLIENT_ID"), os.environ.get("SPOTIPY_CLIENT_SECRET"), REDIRECT_URL, scope="playlist-read-private")
    return redirect(auth_obj.get_authorize_url())

@app.route("/auth")
def complete_auth():
    auth_code = request.args.get("code")
    auth_obj = SpotifyOAuth(os.environ.get("SPOTIPY_CLIENT_ID"), os.environ.get("SPOTIPY_CLIENT_SECRET"), REDIRECT_URL, scope="playlist-read-private")
    token_info = auth_obj.get_access_token(auth_code)

    client = spotipy.Spotify(auth=token_info["access_token"])
    result = client.user_playlists("metalnut4")

    playlist_names = [playlist_item["name"] for playlist_item in result["items"]]
    return "<br />".join(playlist_names)

@app.route("/next")
def another():
    auth_obj = SpotifyOAuth(os.environ.get("SPOTIPY_CLIENT_ID"), os.environ.get("SPOTIPY_CLIENT_SECRET"), REDIRECT_URL, scope="playlist-read-private")
    token_info = auth_obj.get_cached_token()

    client = spotipy.Spotify(auth=token_info["access_token"])
    result = client.user_playlists("metalnut4")
    playlist_names = [playlist_item["name"] for playlist_item in result["items"]]
    return "<br />".join(playlist_names)