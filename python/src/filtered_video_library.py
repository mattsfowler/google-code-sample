from .video_library import VideoLibrary


class FilteredVideoLibrary(VideoLibrary):
    def __init__(self):
        super().__init__()
        self._flagged_videos = []
        self._flag_reasons = []

    def get_video(self, video_id):
        video = super().get_video(video_id)
        if video is not None:
            video = self._set_flagged_status(video)
        return video

    def get_all_videos(self):
        initial_videos = super().get_all_videos()
        videos = []
        for video in initial_videos:
            videos.append(self._set_flagged_status(video))
        return videos

    def get_all_non_flagged_videos(self):
        videos = self.get_all_videos()
        non_flagged_videos = []
        for video in videos:
            if video.video_id not in self._flagged_videos:
                non_flagged_videos.append(video)
        return non_flagged_videos

    def flag_video(self, video_id, flag_reason=""):
        video = self.get_video(video_id)
        if video is None:
            return False
        if video.is_flagged:
            return False
        self._flagged_videos.append(video_id)
        self._flag_reasons.append(flag_reason if flag_reason != "" else "Not supplied")
        return True

    def allow_video(self, video_id):
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
