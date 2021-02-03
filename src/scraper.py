#! python3
import requests
import time
import os
import pandas as pd
import utils
import re
from bs4 import BeautifulSoup as bs4



def scrape_artist_overview(artist):
    print(f'downloading: {artist}')
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
            return re.sub(r'\n', ' ', soup.body.pre.text)
    except FileNotFoundError:
        return(f'could not find {filepath}')




def find_songs_and_urls(artist):

    with open(f'{utils.get_project_root()}/data/raw/{artist}.html') as fp:
        soup = bs4(fp, 'html.parser')

    print(f'finding songs for {artist}')
    songs = []
    musician = soup.body.find('h1', 'artist').string
    table_data = soup.body.find_all('td', 'tal qx')

    for data in table_data:
        songs.append({'artist': utils.clean_string(musician),
                      'song': utils.clean_string(data.string),
                      'url': data.a['href']})
    return songs
