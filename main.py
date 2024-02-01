import cv2
import numpy as np
import pyautogui
from screeninfo import get_monitors
import time
import easyocr
import mss
from monitor_select import real

start_time = time.time()

reader = easyocr.Reader(['en'])


def find_death_text(image_array):  # Ensure the parameter name matches the variable you're passing
    # Directly use the image_array variable here
    text = reader.readtext(image_array, detail=0)
    print(text)
    if "combat report" in text:
        return True
    return False


def capture_screen(region=None):
    with mss.mss() as sct:
        if region:
            monitor = {"top": region[1], "left": region[0], "width": region[2], "height": region[3]}
        else:
            monitor = sct.monitors[0]  # Capture the entire screen
        sct_img = sct.grab(monitor)
        # Convert to an array that OpenCV can use
        img = np.array(sct_img)
        # Convert from BGRA to RGB
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
    else:
        print("Images are not a close match.")


area = region_select()

while True:
    main(area)

