from lyricsgenius import Genius
from dotenv import load_dotenv
import random
import os

load_dotenv()

token = os.getenv("GENIUS_TOKEN")
genius = Genius(token)
genius.remove_section_headers = True  # Removes [Chorus], [Verse], etc.


def get_artists() -> list:
    chart = genius.charts(type_='songs', per_page=50)
    artists = []

    for entry in chart["chart_items"]:
        name = entry["item"]["artist_names"]

        if name not in artists:
            artists.append(name)
        
    return artists


def compose_lyrics() -> None:
    file = "lyrics.txt"
    data = []

    artists = get_artists()
    chosen_artists = random.sample(artists, k=2)

    for artist in chosen_artists:
        print(f"Searching songs of: {artist}")

        artist_data = genius.search_artist(artist, max_songs=3)

        if artist_data:
            for song in artist_data.songs:
                data.append(song.lyrics)
                data.append("\n\n\n")
                print(f"Successfully appended one song from : {artist}")
        else:
            print(f"Could not find songs on {artist}")

    with open(file, "w", encoding="utf-8") as f:
        f.write("".join(data))
        print("Added songs to compose.txt file successfully")


if __name__ == '__main__':
    compose_lyrics()