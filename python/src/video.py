"""A video class."""

from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        """Video constructor."""
        self._title = video_title
        self._video_id = video_id

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)
        self._is_flagged = False
        self._flag_reason = ""

    @property
    def title(self) -> str:
        """Returns the title of a video."""
        return self._title

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags

    @property
    def is_flagged(self) -> bool:
        """Returns whether or not this video is flagged."""
        return self._is_flagged

    @is_flagged.setter
    def is_flagged(self, value):
        self._is_flagged = value

    @property
    def flag_reason(self):
        """Returns the reason why this video was flagged (if it is not flagged, will be an empty string)."""
        return self._flag_reason

    @flag_reason.setter
    def flag_reason(self, value):
        self._flag_reason = value

    def tostring(self):
        """Returns a formatted string representation of the video."""
        video_text = f"{self.title} ({self.video_id}) [{' '.join(self.tags)}]"
        flag_text = "" if not self._is_flagged else f" - FLAGGED (reason: {self._flag_reason})"
        return video_text + flag_text
