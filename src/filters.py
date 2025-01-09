def filter_songs(songs, filters):
    filtered_songs = songs
    for key, value in filters.items():
        if value:
            print(f"Filtering by {key}: {value}")  # Debug
            filtered_songs = [song for song in filtered_songs if song.get(key, "").lower() == value.lower()]
            print(f"Remaining songs: {filtered_songs}")  # Debug
    return filtered_songs
