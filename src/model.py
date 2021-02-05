import pandas as pd
import utils

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn import metrics

import pickle

print('### Reading data')
df = pd.read_csv(f'{utils.get_project_root()}/data/processed/list-of-lyrics.txt', delimiter='|', names=['artist', 'song_name', 'lyrics'])

df.drop_duplicates(subset=['artist', 'song_name'], inplace=True, keep='first')
df.drop_duplicates(subset='lyrics', keep='first', inplace=True)


X = df['lyrics']
y = df['artist']

X_train, X_test, y_train, y_test = train_test_split(X, y)

# Prepocessing starts here
model_pipeline = make_pipeline(
    CountVectorizer(
        lowercase=True,
        stop_words='english',
        ngram_range=(1, 2)
    ),
    LogisticRegression(
        # class_weight='balanced',
        max_iter=10000
    )
)

grid = {
    'logisticregression__C': [0.01, 0.1, 1, 10]
}

print('### Training the model')
grid_search = GridSearchCV(
    estimator=model_pipeline,
    param_grid=grid,
    # scoring='balanced_accuracy',
    scoring='accuracy',
    return_train_score=True,
    n_jobs=-1
)

# finding the best parameter for logistig regression and training the final model
grid_search.fit(X_train, y_train)
final_model = grid_search.best_estimator_

print('Balanced accuracy score of final model: ', metrics.balanced_accuracy_score(y_test, final_model.predict(X_test)))
print('Accuracy score of final model: ', metrics.accuracy_score(y_test, final_model.predict(X_test)))

print('### Saving model')
with open(f'{utils.get_project_root()}/src/lyrics_model.pickle', 'wb') as file:
    pickle.dump(final_model, file)
