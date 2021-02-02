#! python3
import requests
import pandas as pd

def scrape_artist_overview(artist):

    r = requests.get(f'https://www.lyrics.com/artist/{artist}')

    web_page = open(f'../data/raw/{artist}.html', 'w')
    web_page.write(r.text)
    web_page.close()


df = pd.read_csv('../data/artists.csv')

for artist in df['Artist']:
    scrape_artist_overview(artist)
