import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config

class SpotifyPlaylist:
    def __init__(self, playlist_name):
        self.spotify = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=config.SPOTIPY_CLIENT_ID,
                client_secret=config.SPOTIPY_CLIENT_SECRET,
                redirect_uri='http://localhost',
                username=config.USERNAME,
                scope='playlist-read-collaborative, '
                      'playlist-modify-public'))
        self.playlist_name = playlist_name
        self.playlist_id = self.create_playlist(playlist_name)

    # create playlist
    def create_playlist(self, playlist_name):
        success = self.spotify.user_playlist_create(user=config.USERNAME, name=playlist_name)
        playlistid = (success['uri']).split(":")
        return playlistid[2]

    # getting song from spotify
    def search_song(self, search_string):

        try:
            # results = self.spotify.search(q="Sisqo,Thong Song", type="track", limit=1)
            results = self.spotify.search(q=search_string, type="track", limit=1)


            print(results['tracks']['items'][0]['uri'])

        except IndexError:
            return None

        return results['tracks']['items'][0]['uri']


    # add item to playlist
    def add_song_to_playlist(self,playlist_id,song):
        self.spotify.playlist_add_items(playlist_id=playlist_id,items=[song])



