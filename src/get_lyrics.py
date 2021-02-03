import utils
import os
from pathlib import Path
import scraper
import pandas as pd

path_overview = f'{utils.get_project_root()}/data/processed/overview.csv'

df = pd.read_csv(path_overview)


lyrics = []
for url in df['url']:
    lyrics.append(scraper.scrape_lyrics_into_df(url))


print(lyrics)
