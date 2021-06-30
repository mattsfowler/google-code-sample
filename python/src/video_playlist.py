"""A video playlist class."""

from typing import Sequence


class Playlist:
    """A class used to represent a Playlist."""

    def __init__(self, name: str, videos: Sequence[str]):
        self._name = name
        self._videos = videos

    @property
    def name(self) -> str:
        return self._name

    @property
    def videos(self) -> Sequence[str]:
        return self._videos
