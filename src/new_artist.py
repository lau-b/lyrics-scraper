import utils
import scraper
import re

artist_list = []

with open(f'{utils.get_project_root()}/data/artists.csv', 'r') as file:
    for line in file:
        artist_list.append(re.sub(r'\n', '', line))

for artist in artist_list:
    clean_artist = utils.clean_artist(artist)
    utils.create_folders(clean_artist)
    scraper.scrape_artist_overview(artist)

print(artist_list)



