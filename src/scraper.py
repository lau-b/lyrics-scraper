#! python3
import requests
import time
import os
import pandas as pd
import utils
from bs4 import BeautifulSoup as bs4



def scrape_artist_overview(artist):

    r = requests.get(f'https://www.lyrics.com/artist/{artist}')

    web_page = open(f'{utils.get_project_root()}/data/raw/{artist}.html', 'w')
    web_page.write(r.text)
    web_page.close()


def scrape_lyrics_page(artist, song, url):
    r = requests.get(f'https://www.lyrics.com/{url}')

    # TODO: import os, create directories in eigene funktion schreiben. Eventuell schon im Loop selbst.
    web_page = open(f'{utils.get_project_root()}/data/raw/artists/{artist}_{song}.html', 'w')
    web_page.write(r.text)
    web_page.close()
    time.sleep(0.5)


def find_songs_and_urls(artist):

    with open(f'{utils.get_project_root()}/data/raw/{artist}.html') as fp:
        soup = bs4(fp, 'html.parser')

    songs = []
    musician = soup.body.find('h1', 'artist').string
    table_data = soup.body.find_all('td', 'tal qx')

    for data in table_data:
        songs.append({'artist': musician,
                      'song': data.string,
                      'url': data.a['href']})
    return songs



