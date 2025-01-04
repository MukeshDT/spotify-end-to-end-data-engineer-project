import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

client_id = os.environ.get('client_id')
client_secret = os.environ.get('client_secret')

def lambda_handler(event, context):
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

    Playlist_link = "https://open.spotify.com/playlist/0eWPIR1Us5qZOjDwxgIoQX"
    Playlist_URI = Playlist_link.split("/")[-1]

    spotify_data = sp.playlist_items(Playlist_URI)

    client = boto3.client('s3')

    filename = "spotify_raw_" + str(datetime.now()) + ".json"

    client.put_object(
        Bucket='spotify-etl-project-mukesh',
        Key='raw_data/to-processed/' + filename,
        Body=json.dumps(spotify_data)
    )
