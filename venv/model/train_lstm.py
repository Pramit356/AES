import pickle
import os

def remove_full_stop(essay):
    essay1 = []
    for word in essay:
        if word!='.':
            essay1.append(word)
    return essay1





from keras.layers import Embedding, LSTM, Dense, Dropout, Lambda, Flatten
from keras.models import Sequential, load_model, model_from_config
import keras.backend as K

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