#! python3
import requests
import time
import os
import utils
import re
from bs4 import BeautifulSoup as bs4


def scrape_artist_overview(artist):
    r = requests.get(f'https://www.lyrics.com/artist/{artist}')

    web_page = open(f'{utils.get_project_root()}/data/raw/{utils.clean_artist(artist)}.html', 'w')
    web_page.write(r.text)
    web_page.close()


def scrape_lyrics_page(artist, song, url):
    r = requests.get(f'https://www.lyrics.com/{url}')

    web_page = open(f'{utils.get_project_root()}/data/raw/artists/{artist}/{song}.html', 'w')
    web_page.write(r.text)
    web_page.close()
    time.sleep(0.3)


def extract_lyrics(filepath):
    try:
        with open(filepath, 'r') as file:
            soup = bs4(file, 'html.parser')
            lyrics = re.sub(r'\n', ' ', soup.body.pre.text)
            return re.sub(r'\[[vVcCsS]\w+]', '', lyrics)
    except (AttributeError, FileNotFoundError) as e:
        # print(f'could not find {filepath}')
        pass


def find_songs_and_url(artist):
    path = (f'{utils.get_project_root()}/data/raw/{artist}.html')
    with open(path, 'r') as file:
        soup = bs4(file, 'html.parser')

    musician = utils.clean_string(soup.body.find('h1', 'artist').string)
    table_data = soup.body.find_all('td', 'tal qx')

    for data in table_data:
        song = utils.clean_string(data.string)
        url = data.a['href']
        overview_file = open(f'{utils.get_project_root()}/data/processed/overview.csv', 'a')
        overview_file.write(f'{musician}|{song}|{url}\n')
        overview_file.close
