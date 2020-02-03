from mss import mss
import numpy as np
import cv2

mon = {'left': 1, 'top': 31, 'width': 800, 'height': 600}
sct = mss()


def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked


def draw_lines(img):
    lines = cv2.HoughLinesP(img, 1, np.pi/180, 180, np.array([]), 50, 10)
    try:
        for line in lines:
            cords = line[0]
            cv2.line(img, (cords[0], cords[1]), (cords[2], cords[3]), [255, 255, 255], 3)
    except:
        pass


def process_image(processed_image):
    processed_image = cv2.Canny(processed_image, threshold1=200, threshold2=300)
    processed_image = cv2.GaussianBlur(processed_image, (5, 5), 0)
    draw_lines(processed_image)

    return processed_image


def grab_screen(process=True):
    img = np.array(sct.grab(mon), dtype='uint8')
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    if process:
        processed_image = process_image(img)

        return processed_image

    return img
