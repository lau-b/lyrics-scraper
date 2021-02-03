import pandas as pd
import utils

df = pd.read_csv(f'{utils.get_project_root()}/data/processed/list-of-lyrics.txt', delimiter='|')

print(df.head(), df.shape)
