"""A video player class."""

from .video_library import VideoLibrary
from random import randint


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video = None
        self._video_paused = False
        # Each playlist is an array containing 2 items: the name, and a list of video ids.
        # If any further complexity is required from playlists, a separate Playlist class should be implemented.
        self._playlists = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        videos = self._video_library.get_all_videos()
        videos.sort(key=lambda x: x.title)
        for video in videos:
            print(video.tostring())

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        video = self._video_library.get_video(video_id)
        if video is None:
            print("Cannot play video: Video does not exist")
        else:
            if self._current_video is not None:
                self.stop_video()
            self._current_video = video
            self._video_paused = False
            print(f"Playing video: {self._current_video.title}")

    def stop_video(self):
        """Stops the current video."""
        if self._current_video is None:
            print("Cannot stop video: No video is currently playing")
        else:
            print(f"Stopping video: {self._current_video.title}")
            self._current_video = None

    def play_random_video(self):
        """Plays a random video from the video library."""
        videos = self._video_library.get_all_videos()
        video_index = randint(0, len(videos) - 1)
        self.play_video(videos[video_index].video_id)

    def pause_video(self):
        """Pauses the current video."""
        if self._current_video is None:
            print("Cannot pause video: No video is currently playing")
        elif self._video_paused:
            print(f"Video already paused: {self._current_video.title}")
        else:
            self._video_paused = True
            print(f"Pausing video: {self._current_video.title}")

    def continue_video(self):
        """Resumes playing the current video."""
        if self._current_video is None:
            print("Cannot continue video: No video is currently playing")
        elif not self._video_paused:
            print("Cannot continue video: Video is not paused")
        else:
            self._video_paused = False
            print(f"Continuing video: {self._current_video.title}")

    def show_playing(self):
        """Displays video currently playing."""
        if self._current_video is None:
            print("No video is currently playing")
        else:
            print(f"Currently playing: {self._current_video.tostring()}" + (" - PAUSED" if self._video_paused else ""))

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_key = playlist_name.lower()
        if playlist_key in self._playlists.keys():
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            self._playlists[playlist_key] = [playlist_name, []]
            print(f"Successfully created new playlist: {playlist_name}")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        playlist_key = playlist_name.lower()
        if playlist_key not in self._playlists.keys():
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
        elif video_id in self._playlists[playlist_key][1]:
            print(f"Cannot add video to {playlist_name}: Video already added")
        else:
            video = self._video_library.get_video(video_id)
            if video is None:
                print(f"Cannot add video to {playlist_name}: Video does not exist")
            else:
                self._playlists[playlist_key][1].append(video_id)
                print(f"Added video to {playlist_name}: {video.title}")

    def show_all_playlists(self):
        """Display all playlists."""
        keys = list(self._playlists.keys())
        if len(keys) == 0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            keys.sort()
            for key in keys:
                print(self._playlists[key][0])

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_key = playlist_name.lower()
        if playlist_key not in self._playlists.keys():
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
        else:
            print(f"Showing playlist: {playlist_name}")
            playlist = self._playlists[playlist_key]
            if len(self._playlists[playlist_key][1]) == 0:
                print("No videos here yet")
            else:
                for video_id in playlist[1]:
                    video = self._video_library.get_video(video_id)
                    print(video.tostring())

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        playlist_key = playlist_name.lower()
        if playlist_key not in self._playlists.keys():
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
        elif self._video_library.get_video(video_id) is None:
            print(f"Cannot remove video from {playlist_name}: Video does not exist")
        elif video_id not in self._playlists[playlist_key][1]:
            print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
        else:
            video_title = self._video_library.get_video(video_id).title
            video_index = self._playlists[playlist_key][1].index(video_id)
            del self._playlists[playlist_key][1][video_index]
            print(f"Removed video from {playlist_name}: {video_title}")


    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_key = playlist_name.lower()
        if playlist_key not in self._playlists.keys():
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
        else:
            self._playlists[playlist_key][1] = []
            print(f"Successfully removed all videos from {playlist_name}")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_key = playlist_name.lower()
        if playlist_key not in self._playlists.keys():
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
        else:
            del self._playlists[playlist_key]
            print(f"Deleted playlist: {playlist_name}")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
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
