import utils
import pandas as pd

df = pd.read_csv(f'{utils.get_project_root()}/data/processed/overview.csv',
                 delimiter='|',
                 names=['artist', 'song_name', 'lyrics'])

df.drop_duplicates(subset=['artist', 'song_name'], inplace=True, keep='first')

df.to_csv(f'{utils.get_project_root()}/data/processed/overview.csv',
    header=False,
    index=False,
    sep='|')
