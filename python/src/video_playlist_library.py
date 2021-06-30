""" Manages playlists """
import math

from .video_playlist import Playlist


class PlaylistLibrary:
    """Manages access to and manipulation of the user's playlists."""

    def __init__(self):
        self._playlists = []

    def add_playlist(self, playlist_name):
        """Adds a new playlist - returns false if a playlist by the given name already exists
        Args:
            playlist_name: Unique playlist name string
        """
        for i in range(len(self._playlists)):
            if self._playlists[i].name.lower() == playlist_name.lower():
                return False
            if self._playlists[i].name.lower() > playlist_name.lower():
                self._playlists.insert(i, Playlist(playlist_name, []))
                return True
        self._playlists.append((Playlist(playlist_name, [])))
        return True

    def get_all_playlist_names(self):
        """Returns a list of strings containing the names of all current playlists."""
        return list(map(lambda x: x.name, self._playlists))

    def get_playlist(self, playlist_name):
        """Retrieves the playlist object whose name matches the given argument
        Args:
            playlist_name: Name of the playlist to find
        """
        index = self._find_playlist_index(playlist_name)
        if index == -1:
            return None
        else:
            return self._playlists[index]

    def add_video_to(self, playlist_name, video_id):
        """Adds a video to the playlist with the given name.
        Args:
            playlist_name: Name of the playlist to modify
            video_id: ID of the video to add to the playlist (must not exists in that playlist already)
        """
        index = self._find_playlist_index(playlist_name)
        if index == -1:
            return False
        elif video_id in self._playlists[index].videos:
            return False
        else:
            self._playlists[index].videos.append(video_id)
            return True

    def remove_video_from(self, playlist_name, video_id):
        """Removes a video from the playlist with the given name.
        Args:
            playlist_name: Name of the playlist to modify
            video_id: ID of the video to remove from the playlist
        """
        index = self._find_playlist_index(playlist_name)
        if index == -1:
            return False
        elif video_id not in self._playlists[index].videos:
            return False
        else:
            self._playlists[index].videos.remove(video_id)
            return True

    def clear_playlist(self, playlist_name):
        """Removes all videos from the given playlist, but keeps the playlist in the list.
        Args:
            playlist_name: Name of the playlist to wipe
        """
        index = self._find_playlist_index(playlist_name)
        if index == -1:
            return False
        else:
            self._playlists[index].videos.clear()
            return True

    def remove_playlist(self, playlist_name):
        """Delete the given playlist and remove all reference to it
        Args:
            playlist_name: Name of the playlist to remove
        """
        index = self._find_playlist_index(playlist_name)
        if index == -1:
            return False
        else:
            del self._playlists[index]
            return True

    # Has the potential to implemented a binary search to improve access speed
    def _find_playlist_index(self, playlist_name):
        playlist_key = playlist_name.lower()
        for i in range(len(self._playlists)):
            if self._playlists[i].name.lower() == playlist_key:
                return i
        return -1
