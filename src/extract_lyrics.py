import utils
import scraper
from bs4 import BeautifulSoup as bs4

song_list = []



with open(f'{utils.get_project_root()}/data/processed/overview.csv', 'r') as file:
    for line in file:
        song_list.append((line.split(',')))


for entry in song_list:
    read_path = (f'{utils.get_project_root()}/data/raw/artists/{entry[1]}/{entry[2]}.html')
    write_path = f'{utils.get_project_root()}/data/processed/list-of-lyrics.txt'
    print(f'{entry[0]} calling lyrics for {read_path}')
    lyrics = scraper.extract_lyrics(read_path)

    file = open(write_path, 'a')
    file.write(f'{entry[1]}|{lyrics}\n')
    file.close()
