import numpy as np
import pandas as pd
from collections import Counter
from random import shuffle
import cv2
from global_var import *


def balance_data():
    train_data = np.load(DATA_DIR, allow_pickle=True)

    # Look on data
    data = pd.DataFrame(train_data)
    print(data.head())
    print(data.shape)
    print(Counter(data[1].apply(str)))
    del(data)

    lefts = list()
    rights = list()
    forwards = list()

    shuffle(train_data)

    for data in train_data:
        img = data[0]
        choice = data[1]

        if choice == [1, 0, 0]:
            lefts.append([img, choice])
        elif choice == [0, 1, 0]:
            forwards.append([img, choice])
        elif choice == [0, 0, 1]:
            rights.append([img, choice])

    lefts = lefts[:len(rights)][:len(lefts)]
    rights = rights[:len(lefts)]
    forwards = forwards[:len(lefts)]

    print(f'lefts: {len(lefts)} forwards: {len(forwards)} rights: {len(rights)}')

    # Organise data
    data = lefts + forwards + rights
    del(lefts, forwards, rights, train_data)
    shuffle(data)

    print(f'length of final data: {len(data)}')

    np.save(FILE_NAME, data)


if __name__ == '__main__':
    balance_data()
