"""Potential for optimisations: all searches are implemented as linear search, and video_ids must
be converted to lowercase for each comparison.

Additionally, flags are not stored anywhere persistently, and must manually be tacked-on after
retrieving the videos from file. Ideally, this information would be stored either with the video,
or all video information would be stored in a database.
"""

from .video_library import VideoLibrary


class FilteredVideoLibrary(VideoLibrary):
    """A modified version of VideoLibrary class with added functionality for flagging videos."""
    def __init__(self):
        super().__init__()
        self._flagged_videos = []
        self._flag_reasons = []

    def get_video(self, video_id):
        # Adds flag information to the video before returning them.
        video = super().get_video(video_id)
        if video is not None:
            video = self._set_flagged_status(video)
        return video

    def get_all_videos(self):
        # Adds flag information to the videos before returning them.
        initial_videos = super().get_all_videos()
        videos = []
        for video in initial_videos:
            videos.append(self._set_flagged_status(video))
        return videos

    def get_all_non_flagged_videos(self):
        """Filters the master video list and removes any flagged videos"""
        videos = self.get_all_videos()
        non_flagged_videos = []
        for video in videos:
            if video.video_id not in self._flagged_videos:
                non_flagged_videos.append(video)
        return non_flagged_videos

    def flag_video(self, video_id, flag_reason=""):
        """Adds a flag to a given video

        Args:
            video_id: The ID of a video that exists in the system
            flag_reason: (optional) A description of why the video was flagged

        Returns:
            A bool indicating whether the video was successfully flagged
        """
        video = self.get_video(video_id)
        if video is None:
            return False
        if video.is_flagged:
            return False
        self._flagged_videos.append(video_id)
        self._flag_reasons.append(flag_reason if flag_reason != "" else "Not supplied")
        return True

    def allow_video(self, video_id):
        """Removes the flag from a previously flagged video

        Args:
            video_id: The ID of a previously flagged video

        Returns:
            A bool indicating whether a flag was removed from the given video
        """
        video = self.get_video(video_id)
        if video is None:
            return False
        if not video.is_flagged:
            return False
        index = self._get_flag_index(video_id)
        del self._flagged_videos[index]
        del self._flag_reasons[index]
        return True

    def _set_flagged_status(self, video):
        flag_index = self._get_flag_index(video.video_id)
        if flag_index == -1:
            video.is_flagged = False
            video.flag_reason = ""
        else:
            video.is_flagged = True
            video.flag_reason = self._flag_reasons[flag_index]
        return video

    def _get_flag_index(self, video_id):
        for i in range(len(self._flagged_videos)):
            if self._flagged_videos[i].lower() == video_id.lower():
                return i
        return -1
