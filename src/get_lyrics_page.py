import utils
import os
from pathlib import Path
import scraper
import pandas as pd

path_overview = f'{utils.get_project_root()}/data/processed/overview.csv'

df = pd.read_csv(path_overview)

for i in range(len(df)):
    song = df['song'].iloc[i]
    artist = df['artist'].iloc[i]
    print(f'downloading {i+1}/{len(df)+1}: {song} from {artist} ... ')
    scraper.scrape_lyrics_page(artist, song, df['url'].iloc[i])


# iterrows
# read csv in as a dictionary or list
