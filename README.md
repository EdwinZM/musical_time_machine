# musical_time_machine

Created with Python, 
Musical Time Machine is a program 
that asks for a specific year
and using web scraping with Beautiful Soup
it searches the top 100 Hits of that year
on Billboard.com.

After getting the top 100 hits of the year chosen,
Musical Time Machine uses the Spotify API to create a playlist
and add those songs to it.

# How to use

run `python3 main.py` and write a specific year

# Modules used

-bs4 Beautiful Soup
-requests
-spotipy
-spotipy.ouath2