"""A video player class."""

import random

from video_library import VideoLibrary
from video_playlist import Playlist


class VideoPlayer:
    """A class used to represent a Video Player."""

    # Worth getting some global variables here if they'll be used in other functions later down the line
    # Turns out I could've stuck all this in init, so everything's been moved there now

    # isPlaying = False  # Global variable to track if there's a video playing on the player
    # isPaused = False  # Global variable to track if the video player has been paused
    # currentVideo = None  # Global variable for current video, because local scope was causing headaches

    def __init__(self):
        self._video_library = VideoLibrary()
        self.isPlaying = False  # Global variable to track if there's a video playing on the player
        self.isPaused = False  # Global variable to track if the video player has been paused
        self.currentVideo = None  # Global variable for current video, because local scope was causing headaches
        self.playLists = []  # Holds all playlist objects that'll be created
        self.playListNames = []  # Holds all playlist names that had been created, to aid name conflict checks

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        all_videos = self._video_library.get_all_videos()  # Fetch all the videos, based off above function
        all_videos.sort(key=lambda x: x.title)  # Use key with lambda to dictate sort to only go through video title
        print("Here's a list of all available videos:")

        for video in all_videos:  # Loop through txt file, reading each video line by line
            tagString = str(video.tags)  # Convert to string to allow stripping of brackets
            # tagStrip.strip("()") # Old code - this didn't make a difference with this line placement
            print(video.title, "(", video.video_id, ")", "[", tagString.strip("()"), "]")

        # print("show_all_videos needs implementation")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """

        vidPlay = self._video_library.get_video(video_id)  # Start playing the chosen video

        try:  # Check if the video exists
            vidPlay.video_id
        except AttributeError:  # If video doesn't exist, don't bother with the rest of the code
            print("Cannot play video: Video does not exist")
        else:  # Continue as normal if the video exists
            # print("Current ID:", vidPlay.video_id) # Debug
            # currentVideo = vidPlay  # Old code with local currentVideo variable. Caused too much headaches to work
            if self.isPlaying:  # Don't this message on first run of function
                print("Stopping video:", self.currentVideo.title)  # Stop the previous video if any
                self.isPaused = False
            print("Playing video:", vidPlay.title)
            self.isPlaying = True
            self.currentVideo = vidPlay  # Store the video currently playing in a variable

        # print("play_video needs implementation")

    def stop_video(self):
        """Stops the current video."""
        if self.isPlaying is True:
            print("Stopping video:", self.currentVideo.title)
            self.isPlaying = False
            self.isPaused = False
        else:
            print("Cannot stop video: No video is currently playing")

        # print("stop_video needs implementation")

    def play_random_video(self):
        """Plays a random video from the video library."""
        getVideo = self._video_library.get_all_videos()  # Grab all videos
        num_videos = len(self._video_library.get_all_videos())  # Borrowed code to check if videos.txt is empty

        if num_videos == 0:  # Should trigger if there were no videos found in the txt file
            print("There are no videos available to play")  # Will need retrofit to fit flagged videos if I get there
        else:
            if self.isPlaying is True:
                print("Stopping video:", self.currentVideo.title)
                self.isPaused = False
            pickVideo = random.choice(getVideo)  # Get Python to pick a random video in the list (must import random)
            print("Playing video:", pickVideo.title)  # Print the video title of what Python picked at random
            self.isPlaying = True  # Borrowed code lines from play_video
            self.currentVideo = pickVideo  # Probably is a way to further streamline this

        # Old code structure below, things were out of order - checking video availability should've come first
        # if VideoPlayer.isPlaying is True:
        #     print("Stopping video:", VideoPlayer.currentVideo.title)
        #     VideoPlayer.isPaused = False
        # # else: # Old code - wasn't needed in the end
        # getVideo = self._video_library.get_all_videos()  # Grab all videos
        # num_videos = len(self._video_library.get_all_videos())  # Borrowed code to check if videos.txt is empty
        #
        # if num_videos == 0:  # Should trigger if there were no videos found in the txt file
        #     print("There are no videos available to play") # Will need retrofit to fit flagged videos if I get there
        # else:
        #     pickVideo = random.choice(getVideo)  # Get Python to pick a random video in the list
        #     print("Playing video:", pickVideo.title)  # Print the video title of what Python picked at random
        #     VideoPlayer.isPlaying = True  # Borrowed code lines from play_video
        #     VideoPlayer.currentVideo = pickVideo  # Probably is a way to further streamline this

        # print("play_random_video needs implementation")

    def pause_video(self):
        """Pauses the current video."""
        if self.isPlaying is True:  # Borrowed structure from stop_video
            if self.isPaused is True:
                print("Video already paused:", self.currentVideo.title)
            else:
                print("Pausing video:", self.currentVideo.title)
                self.isPaused = True
        else:
            print("Cannot pause video: No video is currently playing")
        # print("pause_video needs implementation")

    def continue_video(self):
        """Resumes playing the current video."""

        if self.isPlaying is True:  # Borrowed structure from pause_video
            if self.isPaused is True:
                print("Continuing video:", self.currentVideo.title)
                self.isPaused = False
            else:
                print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")

        # print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""

        tagString = str(self.currentVideo.tags)  # Convert to string to allow stripping of brackets

        if self.isPlaying is False:
            print("No video is currently playing")
        elif self.isPaused is True:
            print("Currently playing:", self.currentVideo.title, "(", self.currentVideo.video_id, ")",
                  "[", tagString.strip("()"), "]", "- PAUSED")
        else:
            print("Currently playing:", self.currentVideo.title, "(", self.currentVideo.video_id, ")",
                  "[", tagString.strip("()"), "]")

        # print("show_playing needs implementation")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        name = playlist_name.strip()  # Remove whitespace in string
        lowerList = self.playListNames  # temporary list containing lowercase playlist names

        for i in range(len(lowerList)):  # lower case everything in list, probably not good at scaling though
            lowerList[i] = lowerList[i].lower()

        # print("user input for comparison", name.lower())  # debug
        # print("List of playlist names:", lowerList)  # debug

        if name.lower() in lowerList:  # Check if playlist of same name was already made
            print("Cannot create playlist: A playlist with the same name already exists")
        elif name.lower() not in lowerList:
            # print("No conflict detected") # debug
            newPlaylist = Playlist(name.lower())  # new playlist object with user input name
            self.playLists.append(newPlaylist)  # add new playlist to the list of made playlists
            self.playListNames.append(playlist_name) # add just the name to this list for verification later
            print("Successfully created new playlist:", name)

        # print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        getVid = self._video_library.get_video(video_id)  # Start playing the chosen video

        if playlist_name not in self.playListNames:
            print("Cannot add video to ", playlist_name, ": Playlist does not exist")
        else:
            try:  # Check if the video exists
                getVid.video_id
            except AttributeError:  # If video doesn't exist, don't bother with the rest of the code
                print("Cannot add video to" , playlist_name, ": Video does not exist")
            # else: # Check if video already exists in playlist
                # if video_id in

        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        newTerm = ""  # new temp variable to hold cleaned search term
        found = False

        for cha in search_term:
            if cha.isalnum():  # Take user input and only put alphanumeric into temporary variable
                newTerm += cha

        all_videos = self._video_library.get_all_videos()  # Fetch all the videos, based off above function
        all_videos.sort(key=lambda x: x.title)  # Use key with lambda to dictate sort to only go through video title

        # if newTerm.strip() not in all_videos:  # No results found branch attempt
            # print("No search results for", search_term)
        # else:
        # result = [x for x in all_videos if newTerm.strip() in x]  # Attempt at list comprehension

        for video in all_videos:  # A not so elegant solution for finding results, using same for loop as below
            if newTerm.strip() in video.title.lower():
                found = True

        if found is False:
            print("No search results for", search_term)
        else:
            print("Here are results for", search_term+":")
            number = 1
            idHolder = []  # Hold the IDs picked up in the search to inject later into play_video
            for video in all_videos:  # Not elegant to compare search term to each video in existence one by one...
                tagString = str(video.tags)  # Convert to string to allow stripping of brackets
                # print("newTerm is:", newTerm.strip())  # debug
                # print("Current title is:", video.title)  # debug
                if newTerm.strip() in video.title.lower():  # check if term contained in video title
                    print(number, ")", video.title, "(", video.video_id, ")", "[", tagString.strip("()"), "]")
                    idHolder.append(video.video_id)
                    number += 1

            print("Would you like to play any of the above? If yes, specify a number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            choice = input("")
            if not choice.strip().isdecimal():  # Check if there's letters to invalidate
                print("Input contains letters")  # debug
                pass
            elif 1 <= int(choice) <= len(idHolder):  # Valid input, borrowing code from play_video
                vidPlay = self._video_library.get_video(idHolder[int(choice)-1])  # Inject selected video ID to play
                if self.isPlaying:  # Don't this message on first run of function
                    print("Stopping video:", self.currentVideo.title)  # Stop the previous video if any
                    self.isPaused = False
                print("Playing video:", vidPlay.title)
                self.isPlaying = True
                self.currentVideo = vidPlay  # Store the video currently playing in a variable
            else:  # Check if the number is out of index bounds to invalidate
                print("Input is out of bounds")  # debug
                pass

        # print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):  # Unfinished and not working, still has code to see though
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        # Near identical logic as previous function
        newTerm = ""  # new temp variable to hold cleaned search term
        found = False

        # for cha in video_tag:  # Probably not needed given tags require the hashtag
        #     if cha.isalnum():  # Take user input and only put alphanumeric into temporary variable
        #         newTerm += cha

        all_videos = self._video_library.get_all_videos()  # Fetch all the videos, based off above function
        all_videos.sort(key=lambda x: x.title)  # Use key with lambda to dictate sort to only go through video title

        # there should be a way to isolate tags from tuple in order to convert to lowercase for comparisons

        for video in all_videos:  # A not so elegant solution for finding results, using same for loop as below
            if newTerm.strip() in video.tags.lower():  # Code is known to break here, since tuples can't go lowercase
                found = True

        if found is False:
            print("No search results for", video_tag)
        else:
            print("Here are results for", video_tag+":")
            number = 1
            idHolder = []  # Hold the IDs picked up in the search to inject later into play_video
            for video in all_videos:  # Not elegant to compare search term to each video in existence one by one...
                tagString = str(video.tags)  # Convert to string to allow stripping of brackets
                # print("newTerm is:", newTerm.strip())  # debug
                # print("Current title is:", video.title)  # debug
                if newTerm.strip() in video.tags.lower():  # check if term contained in video tags
                    print(number, ")", video.title, "(", video.video_id, ")", "[", tagString.strip("()"), "]")
                    idHolder.append(video.video_id)
                    number += 1

            print("Would you like to play any of the above? If yes, specify a number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            choice = input("")
            if not choice.strip().isdecimal():  # Check if there's letters to invalidate
                print("Input contains letters")  # debug
                pass
            elif 1 <= int(choice) <= len(idHolder):  # Valid input, borrowing code from play_video
                vidPlay = self._video_library.get_video(idHolder[int(choice)-1])  # Inject selected video ID to play
                if self.isPlaying:  # Don't this message on first run of function
                    print("Stopping video:", self.currentVideo.title)  # Stop the previous video if any
                    self.isPaused = False
                print("Playing video:", vidPlay.title)
                self.isPlaying = True
                self.currentVideo = vidPlay  # Store the video currently playing in a variable
            else:  # Check if the number is out of index bounds to invalidate
                print("Input is out of bounds")  # debug
                pass

        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
