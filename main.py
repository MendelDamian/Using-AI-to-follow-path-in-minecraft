import numpy as np
import cv2
import os
import time
from process_img import grab_screen
from direct_keys import PressKey, ReleaseKey, W, S, A, D
from getkeys import key_check
from tensorflow.keras.models import load_model
from global_var import *


def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)


def left():
    PressKey(A)
    ReleaseKey(W)
    ReleaseKey(D)


def right():
    PressKey(D)
    ReleaseKey(W)
    ReleaseKey(A)


def predictions_to_direct(predictions):
    direct = np.argmax(predictions[0])

    if direct == 0:
        left()
    elif direct == 1:
        straight()
    elif direct == 2:
        right()


def main():
    paused = False
    model = load_model('my_model.h5')

    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    while(True):
        last_time = time.time()

        screen = grab_screen()[200:]
        screen = screen / 255.0
        screen = cv2.resize(screen, (FINAL_WIDTH, FINAL_HEIGHT))
        screen = screen.reshape([-1, FINAL_HEIGHT, FINAL_WIDTH, 1])

        predictions = model.predict([screen])
        #print(predictions)

        fps = 1 / (time.time() - last_time)
        print(f'{round(fps)} FPS')

        if not paused:
            predictions_to_direct(predictions)

        keys = key_check()

        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                time.sleep(1)
            ReleaseKey(A)
            ReleaseKey(W)
            ReleaseKey(D)


if __name__ == '__main__':
    main()
