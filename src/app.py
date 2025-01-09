from src.filters import filter_songs
from search import search_songs
from utils import load_songs_dataset

def main():
    songs = load_songs_dataset()
    print("Welcome to the Music App!")
    while True:
        print("\nMenu:")
        print("1. Search Songs")
        print("2. Filter Songs")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            query = input("Enter song title or artist name to search: ")
            results = search_songs(songs, query)
            if results:
                print("\nSearch Results:")
                for song in results:
                    print(f"Title: {song['title']}, Artist: {song['artist']}")
            else:
                print("No songs found.")

        elif choice == "2":
            print("\nAvailable Filters: language, artist, region, country, genre")
            filters = {}
            for filter_key in ["language", "artist", "region", "country", "genre"]:
                filters[filter_key] = input(f"Enter {filter_key} (or leave blank to skip): ")
            results = filter_songs(songs, filters)
            if results:
                print("\nFiltered Songs:")
                for song in results:
                    print(f"Title: {song['title']}, Artist: {song['artist']}, Language: {song['language']}, Country: {song['country']}, Genre: {song['genre']}")
            else:
                print("No songs match the filters.")

        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
