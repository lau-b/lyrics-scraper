#! python3
import os
import utils
from pathlib import Path
import scraper
import pandas as pd


# Setting Path to project root
PATH = f'{utils.get_project_root()}/data/artists.csv'
print(PATH)

df = pd.read_csv(PATH)
print(df)

# for artist in df['Artist']:
#     scrape_artist_overview(artist)

df2 = pd.DataFrame({
    'artist': [],
    'song': [],
    'url': []
    })


for artist in df['Artist']:
    df2 = df2.append(scraper.find_songs_and_urls(artist))
    # print(scraper.find_songs_and_urls(artist))


print(df2)
# for artist in song_list:
#     counter = 0
#     for song in artist:
#         counter += 1
#         print(f'Downloading song ({counter}/{len(artist)}) .......')
#         # print(song['artist'], counter, song['url'])
#         scrape_lyrics_page(song['artist'], counter, song['url'])
