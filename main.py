import cv2
import numpy as np
import easyocr
import mss
from monitor_select import real
from playsound import playsound
import pygame
import time

reader = easyocr.Reader(['en'])
pygame.mixer.init()
pygame.mixer.music.load('test.mp3')


def find_death_text(image_array):
    text = reader.readtext(image_array, detail=0)
    print(text)
    if "COMBAT REPORT" in text:
        return True
    return False


def capture_screen(region=None):
    with mss.mss() as sct:
        if region:
            monitor = {"top": region[1], "left": region[0], "width": region[2], "height": region[3]}
        else:
            monitor = sct.monitors[0]
        sct_img = sct.grab(monitor)
        img = np.array(sct_img)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
        return img


def load_reference_image(path):
    image = cv2.imread(path)
    return image


def region_select():
    region = real()
    return region


def main(region):

    screen_capture = capture_screen(region)

    if find_death_text(screen_capture):
        print("Images are a close match.")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        time.sleep(25)
    else:
        print("Images are not a close match.")


area = region_select()

while True:
    main(area)

