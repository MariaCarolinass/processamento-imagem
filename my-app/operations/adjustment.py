import numpy as np
import cv2

class Adjustment:

    def __init__(self, constant=1):
        self.constant = constant

    def adjust_contrast(self, img):
        adjusted = img * self.constant
        return np.clip(adjusted, 0, 255).astype(np.uint8)