import pickle
import os
import pandas as pd
from keras.layers import Embedding, LSTM, Dense, Dropout, Lambda, Flatten
from keras.models import Sequential, load_model, model_from_config
import keras.backend as K
from sklearn.cross_validation import KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import cohen_kappa_score

def get_model():
    """Define the model."""
    model = Sequential()
    model.add(LSTM(300, dropout=0.4, recurrent_dropout=0.4, input_shape=[1, 300], return_sequences=True))
    model.add(LSTM(64, recurrent_dropout=0.4))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='relu'))

    model.compile(loss='mean_squared_error', optimizer='rmsprop', metrics=['mae'])
    model.summary()

    return model


def train_model():
    cur_path = os.path.dirname(__file__)

    new_path = os.path.relpath('..\\Preprocessing\\preliminary_results.txt', cur_path)

    with open(new_path, "rb") as myFile:
        contents = pickle.load(myFile)

    wordvec = remove_full_stop(contents[0])

X = pd.read_csv('model/Dataset/training_set_rel3.tsv', sep='\t', encoding='ISO-8859-1')
df = pd.read_excel(r'model\Dataset\cleaned_dataset.xlsx')
y1 = df['domain1_score']
#print(df)
df = df.dropna(thresh = 12000, axis=1)
df = df.drop(columns=['rater1_domain1', 'rater2_domain1'])
print(df.head())

minimum_scores = [-1, 2, 1, 0, 0, 0, 0, 0, 0]
maximum_scores = [-1, 12, 6, 3, 3, 4, 4, 30, 60]




# y = X['domain1_score']
# print(X)
# X = X.dropna(axis=1)
# X = X.drop(columns=['rater1_domain1', 'rater2_domain1'])
# print(X)
#print(X.head())
# print(y)
# print(y1)