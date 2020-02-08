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
    paused = True
    model = load_model('my_model.h5')

    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    while(True):
        if not paused:
            last_time = time.time()

            screen, lines = grab_screen()
            screen = screen[200:] / 255.0
            screen = cv2.resize(screen, (FINAL_WIDTH, FINAL_HEIGHT))
            screen = screen.reshape([-1, FINAL_HEIGHT, FINAL_WIDTH, 1])

            predictions = model.predict([screen])
            #print(predictions)

        # SHOWING LINES (UNNECESSARY)
        # clear_screen = grab_screen(process=False)
        # if not paused:
        #     try:
        #         for line in lines:
        #             cords = line[0]
        #             if cords[1] > 200 or cords[3] > 200:
        #                 cv2.line(clear_screen, (cords[0], cords[1]), (cords[2], cords[3]), [0, 255, 0], 3)
        #     except:
        #         pass
        # cv2.imshow('Window', clear_screen)
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
        #     break
        # SHOWING LINES (UNNECESSARY)  END

        if not paused:
            predictions_to_direct(predictions)
            fps = 1 / (time.time() - last_time)
            print(f'{round(fps)} FPS')

        keys = key_check()
        if 'Y' in keys:
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
