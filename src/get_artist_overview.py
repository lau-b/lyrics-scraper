import utils
import scraper
import re
from tqdm import tqdm

artist_list = []

with open(f'{utils.get_project_root()}/data/artists.csv', 'r') as file:
    for line in file:
        artist_list.append(re.sub(r'\n', '', line))

print('Step 1: Creating folder structure for every artist')
for artist in tqdm(artist_list):
    utils.create_folders(utils.clean_artist(artist))

print('\nStep 2: Scraping lyrics.com\'s artist page')
for artist in tqdm(artist_list):
    scraper.scrape_artist_overview(artist)

print('\nStep 3: Extracting all songs and URLs from every artists page')
for artist in tqdm(artist_list):
    scraper.find_songs_and_url(utils.clean_artist(artist))
