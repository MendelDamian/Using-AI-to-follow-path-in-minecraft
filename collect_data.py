import numpy as np
import cv2
import os
import time
from process_img import grab_screen
from getkeys import key_check
from global_var import *

if os.path.isfile(FILE_NAME):
    print('File exists, loading peravious data!')
    training_data = list(np.load(DATA_DIR, allow_pickle=True))
    print(f'{len(training_data)} examples')
else:
    print('File does not exist, creating new one!')
    training_data = list()


def keys_to_output(keys):
    #        [A, W, D]
    output = [0, 0, 0]
    if 'W' in keys:
        output[1] = 1
    elif 'A' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1

    return output


def collect_data():
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    while(True):
        last_time = time.time()

        # Primitive ROI
        # GET 800 X 600, then cut first 200 pixels from the top - final size 800 x 400
        screen = grab_screen()[200:]
        screen = screen / 255.0

        cv2.imshow('Window', screen)
        screen = cv2.resize(screen, (FINAL_WIDTH, FINAL_HEIGHT))

        fps = 1 / (time.time() - last_time)
        print(f'{round(fps)} FPS')

        keys = key_check()
        output = keys_to_output(keys)

        if 1 in output:
            training_data.append([screen, output])

        if len(training_data) % 1000 == 0 and len(training_data) > 0:
            print(len(training_data))
            np.save(FILE_NAME, training_data)

        if cv2.waitKey(25) and 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    collect_data()
