import cv2

class Conversion:

    def __init__(self):
        pass

    def convert_rgb_to_gray(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    def convert_rgb_to_hsv(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    def convert_rgb_to_lab(self, img):
        return cv2.cvtColor(img, cv2.COLOR_BGR2LAB)