"""A video playlist class."""

from video_library import VideoLibrary
from video import Video  # Grab everything from video.py, inspired by video_player implementation


# playLists = []  # Holds all playlists that'll be created

class Playlist:
    """A class used to represent a Playlist. While unfinished, the working outs are still there to see."""

    def __init__(self, playlist_name):
        # self._video = Video()  # Inspired by video_player implementation
        # self.playlists = []  # Holds all playlists that'll be created
        self.name = playlist_name
        self.videos = []  # Holds all videos inside the playlist

    # def __repr__(self):  # Attempt to get returnable data
    #     return f'{self.name}'

    # def create_playlist(self, playlist_name):  # placed the functions incorrectly, oops
    #     """Create a unique playlist."""
    #     name = playlist_name.strip()  # Remove whitespace in string
    #     if name.lower() in playLists:  # Check if playlist of same name was already made
    #         print("Cannot create playlist: A playlist with the same name already exists")
    #     else:
    #         newPlaylist = Playlist(playlist_name)
    #         print("Successfully created new playlist:", name)

    # def add_to_playlist(self, playlist_name, video_id):
