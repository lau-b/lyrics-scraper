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
from tqdm import tqdm

# set absolute path
PATH = Path(f'{utils.get_project_root()}/data/artists.csv')

artist_list = pd.read_csv(PATH)
df = pd.DataFrame({'artist': [],
                   'song': [],
                   'url': []})

# creating missing folders to store lyric pages in
for artist in tqdm(artist_list['Artist']):
    # getting artist overview pages
    scraper.scrape_artist_overview(artist)
    artist = utils.clean_artist(artist)

    try:
        os.makedirs(f'{utils.get_project_root()}/data/raw/artists/{artist}')
    except FileExistsError:
        print(f'{artist}: Directory already exsists.')



    # extracting artist and song information and saving into a csv
    df = df.append(scraper.find_songs_and_urls(artist))


df.drop_duplicates(['artist', 'song'], inplace=True)
df.to_csv(f'{utils.get_project_root()}/data/processed/overview.csv')
