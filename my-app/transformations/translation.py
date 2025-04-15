import numpy as np
import cv2

class Translation:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_img(self, img):
        translation_matrix = np.float32([[1, 0, self.x], [0, 1, self.y]])
        return cv2.warpAffine(img, translation_matrix, (img.shape[1], img.shape[0]))
