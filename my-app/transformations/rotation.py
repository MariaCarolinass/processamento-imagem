import cv2

class Rotation:

    def __init__(self, degrees=0):
        self.degrees = degrees

    def rotate_img(self, img):
        (h, w) = img.shape[:2]
        center = (w // 2, h // 2)
        rotation_matrix = cv2.getRotationMatrix2D(center, self.degrees, 1.0)
        return cv2.warpAffine(img, rotation_matrix, (w, h))
