from bs4 import BeautifulSoup
import requests

date = input("Where would you like to travel? Type the date in this format: YY-MM-DD:\n")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
soup = BeautifulSoup(response.text, "html.parser")

songs = soup.find_all(name="span", class_="chart-element__information__song")

song_list = [song.getText() for song in songs]
print(song_list)