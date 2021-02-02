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
        print(f'{artist}: Directory already exsists.')

    scraper.scrape_artist_overview(artist)
    df = df.append(scraper.find_songs_and_urls(artist))


for i in range(len(df)):
    artist, song, url = df[['artist', 'song', 'url']].iloc[i]
    print(f'scraping {1}/{len(df) + 1}')
    scraper.scrape_lyrics_page('Neutral-Milk-Hotel', song, url)


print('success!! Hooray')


