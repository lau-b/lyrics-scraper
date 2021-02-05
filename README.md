# lyrics-scraper

This project scrapes songs from [Lyrics.com](www.lyrics.com) based on a list of artists to train a model that classifies potential artists by receiving snippets of text.

To achieve this from scratch you need to follow some steps:
1. Create a list of artists by putting them into `/data/artists.csv`
    - Sadly you need to also put in an ID, because of Lyrics.com
2. run `src/get_artist_overview.py`
3. run `src/remove_duplicates.py`
4. run `src/get_artist_overview.py`
5. run `src/extract_lyrics.py`
6. run `create_model.py`
7. run `src/predict_this.py` and get trolled.
