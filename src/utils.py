from pathlib import Path
import re


def get_project_root():
    return Path(__file__).parent.parent


def clean_string(string):
    string = re.sub(r'\s+', '-', re.sub(r'\.|,|\/', '', string)).lower()
    return string


def clean_artist(artist):
    return re.sub(r'\/\d{3,}', '', artist)
