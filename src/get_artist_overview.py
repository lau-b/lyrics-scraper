#! python3
'''
This file reads a list of artists and scrapes www.lyrics.com for a list of
songs. It stores the artist name, song name and url to the lyrics page
in a .csv file.
'''

import utils
import os
from pathlib import Path
import scraper
import pandas as pd

# set absolute path
PATH = Path(f'{utils.get_project_root()}/data/artists.csv')

artist_list = pd.read_csv(PATH)
df = pd.DataFrame({'artist': [],
                   'song': [],
                   'url': [],
                   'lyrics': []})

# creating missing folders to store lyric pages in
for artist in artist_list['Artist']:
    try:
        os.makedirs(f'{utils.get_project_root()}/data/raw/artists/{artist}')
    except FileExistsError:
        print(f'{artist}: Directory already exsists.')

    # getting artist overview pages
    scraper.scrape_artist_overview(artist)

    # extracting artist and song information and saving into a csv
    df = df.append(scraper.find_songs_and_urls(artist))

df.to_csv(f'{utils.get_project_root()}/data/processed/overview.csv')
