#! python3
import requests
import read_songs_from_file

# this will later be read from a file
# have to make sure spaces are replaced with '-'
artist = 'Neutral-Milk-Hotel'

r = requests.get(f'https://www.lyrics.com/artist/{artist}')

print(r.status_code)

web_page = open(f'../data/{artist}.html', 'w')
web_page.write(r.text)
web_page.close()

get_song_titles('Neutral-Milk-Hotel')
