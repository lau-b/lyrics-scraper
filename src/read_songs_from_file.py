#! python3
import requests
import time
import pandas as pd
from bs4 import BeautifulSoup as bs4

def find_songs_and_urls(artist):

    with open(f'../data/raw/{artist}.html') as fp:
        soup = bs4(fp, 'html.parser')

    musician = soup.body.find('h1', 'artist').string
    table_data = soup.body.find_all('td', 'tal qx')

    songs = []
    for data in table_data:
        songs.append({'artist': musician,
                      'title': data.string,
                      'url': data.a['href']})

    return songs


def scrape_lyrics_page(artist, song, url):
    r = requests.get(f'https://www.lyrics.com/artist{url}')

    # TODO: import os, create directories in eigene funktion schreiben. Eventuell schon im Loop selbst.
    web_page = open(f'../data/raw/artists/{artist}_{song}.html', 'w')
    web_page.write(r.text)
    web_page.close()
    time.sleep(0.5)


song_list = []

df = pd.read_csv('../data/artists.csv')
for artist in df['Artist']:
    song_list.append(find_songs_and_urls(artist))


for artist in song_list:
    counter = 0
    for song in artist:
        counter += 1
        print(f'Downloading song ({counter}/{len(artist)}) .......')
        # print(song['artist'], counter, song['url'])
        scrape_lyrics_page(song['artist'], counter, song['url'])
