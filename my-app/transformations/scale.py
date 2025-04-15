import cv2

class Scale:
    
    def __init__(self, scale=1.0):
        self.scale = scale

    def change_scale(self, img):
        (h, w) = img.shape[:2]
        center = (w // 2, h // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, 0, self.scale)
        return cv2.warpAffine(img, rotation_matrix, (w, h))