#! python3
from bs4 import BeautifulSoup as bs4

def get_song_titles(artist):

    # QUESTION: does the stream get closed again?
    with open(f'../data/{artist}.html') as fp:
        soup = bs4(fp, 'html.parser')

    # artist = soup.body.find('h1', 'artist').string
    print(artist)

    table_data = soup.body.find_all('td', 'tal qx')

    songs = []
    for data in table_data:
        songs.append({'artist': artist,
                      'song': data.string,
                      'url': data.a['href']})

    return songs

