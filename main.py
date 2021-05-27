from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "??"
CLIENT_SECRET = "??"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID, 
        client_secret=CLIENT_SECRET, 
        scope="playlist-modify-private", 
        redirect_uri="http://example.com",
        show_dialog=True,
        cache_path="token.txt",
        )
    )

user_id = sp.current_user()["id"]

date = input("Where would you like to travel? Type the date in this format: YY-MM-DD:\n")

year = date.split("-")[0]

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
soup = BeautifulSoup(response.text, "html.parser")

songs = soup.find_all(name="span", class_="chart-element__information__song")

song_list = [song.getText() for song in songs]


song_uris = []
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        print(uri)
        song_uris.append(uri)
    except IndexError:
        print(f"{song} does not exist in Spotify. Skipped.")

