import numpy as np

class Control:

    def __init__(self, gamma=1.0):
        self.gamma = gamma

    def control_gammar(self, img):
        corrected = np.power(img/255., self.gamma)
        return (corrected * 255).astype(np.uint8)