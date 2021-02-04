from pathlib import Path
import re
import os


def get_project_root():
    return Path(__file__).parent.parent


def create_folders(artist):
    try:
        os.makedirs(f'{get_project_root()}/data/raw/artists/{artist}')
    except FileExistsError:
        # maybe include loggin here later
        pass

    try:
        os.makedirs(f'{get_project_root()}/data/processed/artists/{artist}')
    except FileExistsError:
        # maybe include loggin here later
        pass


def clean_string(string):
    string = re.sub(r'\s+', '-', re.sub(r'\.|,|\/', '', string)).lower()
    return string


def clean_artist(artist):
    return re.sub(r'\/\d{3,}', '', artist).lower()
