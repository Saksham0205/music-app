def search_songs(songs, query):
    """
    Searches for songs by title or artist name.

    Args:
        songs (list): List of song dictionaries.
        query (str): Search query string.

    Returns:
        list: A list of songs matching the search query.
    """
    query = query.lower()
    return [
        song for song in songs
        if query in song["title"].lower() or query in song["artist"].lower()
    ]
