#! python3
import pandas as pd
from bs4 import BeautifulSoup as bs4

def get_song_titles(artist):

    # QUESTION: does the stream get closed again?
    with open(f'../data/{artist}.html') as fp:
        soup = bs4(fp, 'html.parser')

    musician = soup.body.find('h1', 'artist').string

    table_data = soup.body.find_all('td', 'tal qx')

    songs = []
    for data in table_data:
        songs.append({'artist': musician,
                      'song': data.string,
                      'url': data.a['href']})

    return songs

df = pd.read_csv('../data/artists.csv')
for artist in df['Artist']:
    print(get_song_titles(artist))
