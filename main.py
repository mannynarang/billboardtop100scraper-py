from bs4 import BeautifulSoup
import requests
from spotify import SpotifyPlaylist

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}").text
soup = BeautifulSoup(response, "html.parser")

artists = soup.select(selector="span.c-label.a-no-trucate")

artist_list = []
song_list = []
for a in artists:
    artist_list.append(a.getText().strip())

songs = soup.select(selector="li h3.c-title")

for song in songs:
    song_list.append(song.getText().strip())

results = zip(song_list, artist_list)

#
# hello = SpotifyPlaylist("yeeehaw")
# hello.create_playlist()

playlist = SpotifyPlaylist(f"{date} - billboard top 100")

for song, artist in results:
    result = (playlist.search_song(f"{song} - {artist}"))
    if result is not None:
        playlist.add_song_to_playlist(playlist.playlist_id,result)
