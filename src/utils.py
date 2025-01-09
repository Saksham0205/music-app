import os
import json

def load_songs_dataset(file_path="data/songs_dataset.json"):
    # Get the absolute path of the file
    abs_path = os.path.join(os.path.dirname(__file__), "../", file_path)
    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"File not found at {abs_path}")
    with open(abs_path, "r") as file:
        return json.load(file)


def save_songs(songs, file_path="data/songs_dataset.json"):
    """
    Saves the song dataset to a JSON file.

    Args:
        songs (list): List of song dictionaries.
        file_path (str): Path to save the dataset file.
    """
    with open(file_path, "w") as file:
        json.dump(songs, file, indent=4)
