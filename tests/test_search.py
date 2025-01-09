import pytest
from src.search import search_songs

def test_search_songs():
    songs = [
        {"title": "Song A", "artist": "Artist 1"},
        {"title": "Song B", "artist": "Artist 2"}
    ]
    result = search_songs(songs, "Song A")
    assert len(result) == 1
    assert result[0]["artist"] == "Artist 1"
