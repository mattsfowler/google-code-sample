"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist_library import PlaylistLibrary
from random import randint


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video = None
        self._video_paused = False
        self._playlist_library = PlaylistLibrary()

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
        playlist_created = self._playlist_library.add_playlist(playlist_name)
        if not playlist_created:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            print(f"Successfully created new playlist: {playlist_name}")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        playlist_exists = self._playlist_library.get_playlist(playlist_name) is not None
        video = self._video_library.get_video(video_id)
        if not playlist_exists:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
        elif video is None:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
        else:
            video_added = self._playlist_library.add_video_to(playlist_name, video_id)
            if not video_added:
                print(f"Cannot add video to {playlist_name}: Video already added")
            else:
                print(f"Added video to {playlist_name}: {video.title}")

    def show_all_playlists(self):
        """Display all playlists."""
        playlists = self._playlist_library.get_all_playlist_names()
        if len(playlists) == 0:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            for playlist_name in playlists:
                print(playlist_name)

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist = self._playlist_library.get_playlist(playlist_name)
        if playlist is None:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
        else:
            print(f"Showing playlist: {playlist_name}")
            if len(playlist.videos) == 0:
                print("No videos here yet")
            else:
                for video_id in playlist.videos:
                    video = self._video_library.get_video(video_id)
                    print(video.tostring())

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        playlist_exists = self._playlist_library.get_playlist(playlist_name) is not None
        video = self._video_library.get_video(video_id)
        if not playlist_exists:
            print(f"Cannot remove video from {playlist_name}: Playlist does not exist")
        elif video is None:
            print(f"Cannot remove video from {playlist_name}: Video does not exist")
        else:
            video_removed = self._playlist_library.remove_video_from(playlist_name, video_id)
            if not video_removed:
                print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
            else:
                print(f"Removed video from {playlist_name}: {video.title}")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_cleared = self._playlist_library.clear_playlist(playlist_name)
        if not playlist_cleared:
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
        else:
            print(f"Successfully removed all videos from {playlist_name}")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_removed = self._playlist_library.remove_playlist(playlist_name)
        if not playlist_removed:
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
        else:
            print(f"Deleted playlist: {playlist_name}")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        videos = self._video_library.get_all_videos()
        matches = []
        for video in videos:
            if search_term.lower() in video.title.lower():
                matches.append(video)
        print(f"Here are the results for {search_term}:")
        for i in range(len(matches)):
            print(f"{i + 1}) {matches[i].tostring()}")
        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")
        user_response = input("")

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
