import pytest
from src.filters import filter_songs


def test_filter_songs():
    songs = [
        {"title": "Song A", "language": "English"},
        {"title": "Song B", "language": "Hindi"}
    ]
    filters = {"language": "English"}
    result = filter_songs(songs, filters)
    assert len(result) == 1
    assert result[0]["title"] == "Song A"
