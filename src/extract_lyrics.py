import utils
import scraper
from tqdm import tqdm

song_list = []
with open(f'{utils.get_project_root()}/data/processed/overview.csv', 'r') as file:
    for line in file:
        song_list.append((line.split(',')))


for entry in tqdm(song_list):
    read_path = (f'{utils.get_project_root()}/data/raw/artists/{entry[1]}/{entry[2]}.html')
    write_path = f'{utils.get_project_root()}/data/processed/list-of-lyrics.txt'

    lyrics = scraper.extract_lyrics(read_path)

    file = open(write_path, 'a')
    file.write(f'{entry[1]}|{lyrics}\n')
    file.close()

print('Done')
