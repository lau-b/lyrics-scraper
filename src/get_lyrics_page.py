import utils
import scraper
import re
from tqdm import tqdm


song_list = []

with open(f'{utils.get_project_root()}/data/processed/overview.csv', 'r') as file:
    for line in file:
        song_list.append(line.split('|'))

# TODO: might inclode a step here in which to remove duplicates before loading them
for song in tqdm(song_list):
    scraper.scrape_lyrics_page(song[0], song[1], re.sub('\n', '', song[2]))
