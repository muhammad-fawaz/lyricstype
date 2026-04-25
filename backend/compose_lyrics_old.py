from lyricsgenius import Genius
import random

def getting_lyrics():

    token = "_6oTGNO2nsIuf9dbZKRH0spc8DqS7TpjxVebdWDixCsgMxY5SsgrW6vVRoOwVQfi"
    genius = Genius(token)

    # Clean up settings for a typing test
    genius.remove_section_headers = True  # Removes [Chorus], [Verse], etc.
    genius.verbose = False               # Stops the terminal from getting cluttered

    artists = ["The Beatles", "Daft Punk", "Radiohead", "Billie Eilish", "Justin Bieber", "Sabrina Carpenter", "Shawn Mendez"]
    artists_chosen = []
    master_lyrics = ""

    for i in range(3):
        artists_chosen.append(random.choice(artists))

    for name in artists_chosen:
        print(f"Fetching songs for {name}...")
        # max_songs=5 keeps it fast and within API limits
        artist_data = genius.search_artist(name, max_songs=5, sort="popularity")
        
        if artist_data:
            for song in artist_data.songs:
                master_lyrics += f"\n{song.lyrics}"
                print(f"Added {song.title} to the file...")

    # Save everything to one file for your Markov script to read
                with open("corpus.txt", "a", encoding="utf-8") as f:
                    f.write(master_lyrics)

    print("Done! All lyrics saved to corpus.txt")



getting_lyrics()
