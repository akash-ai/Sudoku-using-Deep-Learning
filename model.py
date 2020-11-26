#data preparation
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
#model building
import keras
from keras.layers import Activation
from keras.layers import Conv2D, BatchNormalization, Dense, Flatten, Reshape


def get_file(file):
    data = pd.read_csv(file)

    feat_raw = data['quizzes']  # column 1
    label_raw = data['solutions']  # column 2

    feat = []
    label = []

    for i in feat_raw:
        x = np.array([int(j) for j in i]).reshape(
            (9, 9, 1))  # converting that list to np. array with shape 9,9,1 (for CNN)
        feat.append(x)

    # scaling down
    feat = np.array(feat)
    feat = feat / 9  # dividing all values by 9
    feat = feat - 0.5

    for i in label_raw:
        x = np.array([int(j) for j in i]).reshape(
            (81, 1)) - 1  # output dense layer with 81 outputs for each sudoku game
        label.append(x)

    label = np.array(label)  # no need of scaling for the solutions

    # removing old lists object
    del (feat_raw)
    del (label_raw)

    x_train, x_test, y_train, y_test = train_test_split(feat, label, test_size=0.2, random_state=420)

    return x_train, x_test, y_train, y_test


def get_model():
    model = keras.models.Sequential()

    # first Conv2D layer with 64 filters 3x3. relu activation. No padding (default: same), input shape 3D amtrix of 9x9x1
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu', padding='same', input_shape=(9, 9, 1)))
    model.add(BatchNormalization())

    # second Conv2D layer
    model.add(Conv2D(64, kernel_size=(3, 3), activation='relu', padding='same'))
    model.add(BatchNormalization())

    # third Conv2D layer
    model.add(Conv2D(128, kernel_size=(1, 1), activation='relu', padding='same'))

    # flatten layer
    model.add(Flatten())

    # output layer
    model.add(Dense(81 * 9))  # each no. output in a cell will have 9 classes. So, in total we have 81*9 possibilities.
    model.add(Reshape((-1, 9)))
    model.add(Activation('softmax'))  # for probability.. as each output will have 9 probabilities

    return model


#load data
X_train, X_test, y_train, y_test = get_file('sudoku.csv') # 1million sudoku records.

#model.save("sudoku_model")

model = keras.models.load_model('sudoku_model')

#solve sudoku one by one
def norm(a):
    return (a/9)-.5


def denorm(a):
    return (a + .5) * 9


import copy


def inference_sudoku(sample):
    '''
        This function solve the sudoku by filling blank positions one by one.
    '''

    feat = copy.copy(
        sample)  # making a shallow copy that means. 2 different objects are connected with same data points

    while (1):

        out = model.predict(feat.reshape((1, 9, 9, 1)))  # predicting the result 4 dimensional array.
        out = out.squeeze()  # remove single-dimensional entries from the shape of an array.

        pred = np.argmax(out, axis=1).reshape((9, 9)) + 1  # taking highest probability
        prob = np.around(np.max(out, axis=1).reshape((9, 9)), 2)

        feat = denorm(feat).reshape((9, 9))
        mask = (feat == 0)

        if (mask.sum() == 0):
            break

        prob_new = prob * mask

        ind = np.argmax(prob_new)
        x, y = (ind // 9), (ind % 9)

        val = pred[x][y]
        feat[x][y] = val
        feat = norm(feat)

    return pred


def test_accuracy(feats, labels):
    correct = 0

    for i, feat in enumerate(feats):

        pred = inference_sudoku(feat)

        true = labels[i].reshape((9, 9)) + 1

        if (abs(
                true - pred).sum() == 0):  # comparing with the difference with the test set and solution. difference should be zero.
            correct += 1

    print(correct / feats.shape[0])


# test my game
def solve_sudoku(game):
    #game = game.replace('\n', '')
    #game = game.replace(' ', '')
    game = np.array([int(j) for j in game]).reshape((9, 9, 1))
    game = norm(game)
    game = inference_sudoku(game)
    return game

#game = '''
#          0 0 9 7 5 0 0 0 0
#          0 0 0 0 0 0 0 0 0
#          0 0 5 3 8 2 0 0 0
#          0 1 0 0 0 0 0 0 3
#          0 0 2 0 0 0 9 0 8
#          4 0 6 0 0 0 0 0 0
#          9 0 0 0 4 0 1 3 0
#          7 0 0 0 0 6 5 4 9
#          0 0 0 2 0 0 0 0 0
#      '''

game = [4,3,0,0,0,0,0,0,8, 0,7,0,0,0,3,0,0,9, 2,0,0,4,9,0,0,0,0,
        0,2,0,7,4,1,0,0,6, 0,0,0,0,0,0,0,0,0, 1,0,0,8,6,5,0,4,0,
        0,0,0,0,2,4,0,0,7, 5,0,0,1,0,0,0,3,0, 9,0,0,0,0,0,0,6,1]

game = solve_sudoku(game)

print('solved puzzle:\n')
print(game)