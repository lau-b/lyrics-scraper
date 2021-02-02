#! python3
import os
import utils
from pathlib import Path
import scraper
import pandas as pd


# Setting Path to project root
PATH = Path(f'{utils.get_project_root()}/data/artists.csv')

df_artist_list = pd.read_csv(PATH)


# for artist in df['Artist']:
#     scrape_artist_overview(artist)

df = pd.DataFrame({'artist': [],
                    'song': [],
                    'url': []})


for artist in df_artist_list['Artist']:
    try:
        os.makedirs(f'{utils.get_project_root()}/data/raw/artists/{artist}')
    except FileExistsError:
        print(f'Directory for {artist} already exsists.')

    scraper.scrape_artist_overview(artist)
    # df = df.append(scraper.find_songs_and_urls(artist))
    # print(scraper.find_songs_and_urls(artist))


print(df)
# for artist in song_list:
#     counter = 0
#     for song in artist:
#         counter += 1
#         print(f'Downloading song ({counter}/{len(artist)}) .......')
#         # print(song['artist'], counter, song['url'])
#         scrape_lyrics_page(song['artist'], counter, song['url'])



# create folder for ever artist:
# Path.mkdir(Path(f'{utils.get_project_root()}/data/artists/', artist))

