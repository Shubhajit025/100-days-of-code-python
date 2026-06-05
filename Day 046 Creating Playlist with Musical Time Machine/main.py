import requests
from bs4 import BeautifulSoup
import ytmusicapi
from ytmusicapi import YTMusic

ask_date = input("Which year do you want to travel to? Type the date in this format - YYYY-MM-DD: ")

URL = f"https://appbrewery.github.io/bakeboard-hot-100/{ask_date}"


response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
song_name = soup.find_all(name="h3", class_="chart-entry__title")
songs = []

for song in song_name:
    my_song = song.getText()
    songs.append(my_song)
print(songs)

yt = YTMusic("browser.json")
playlists = yt.get_library_playlists()
# print(f"Found {len(playlists)} playlists in your library.")
NotMe = yt.create_playlist(
            title="NotMe",
            description="Made with love by NotMe, for me only.",
            privacy_status="PUBLIC"
        )

for song in songs:
    result = yt.search(song, filter="songs")
    if result:
        video_id = result[0]["videoId"]
        yt.add_playlist_items(NotMe, [video_id])
        print(f"Added: {song}")
    else:
        print(f"Not found: {song}")
