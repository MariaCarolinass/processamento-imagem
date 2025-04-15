import os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import cv2
from transformations.translation import Translation
from transformations.rotation import Rotation
from transformations.scale import Scale
from operations.adjustment import Adjustment
from operations.conversion import Conversion
from corrections.control import Control

matplotlib.use('Agg') 

file_path = 'images/cat.jpg'
img = cv2.imread(file_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

translation = Translation(50, 100)
translated_image = translation.move_img(img)

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1), plt.imshow(img), plt.title('Original'), plt.axis('off')
plt.subplot(1, 2, 2), plt.imshow(translated_image), plt.title(f'Transladada ({translation.x}, {translation.y})'), plt.axis('off')
plt.tight_layout()
plt.savefig('output/translated_image.png')

rotation = Rotation(45)
rotation_image = rotation.rotate_img(img)

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1), plt.imshow(img), plt.title('Original'), plt.axis('off')
plt.subplot(1, 2, 2), plt.imshow(rotation_image), plt.title(f'Rotacionada ({rotation.degrees}°)'), plt.axis('off')
plt.tight_layout()
plt.savefig('output/rotation_image.png')

scale = Scale(2.0)
scale_image = scale.change_scale(img)

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1), plt.imshow(img), plt.title('Original'), plt.axis('off')
plt.subplot(1, 2, 2), plt.imshow(scale_image), plt.title(f'Escala {scale.scale}'), plt.axis('off')
plt.tight_layout()
plt.savefig('output/scale_image.png')

conversion = Conversion()
conversion_gray_image = conversion.convert_rgb_to_gray(img)
conversion_hsv_image = conversion.convert_rgb_to_hsv(img)
conversion_lab_image = conversion.convert_rgb_to_lab(img)

plt.figure(figsize=(16, 5))
plt.subplot(1, 4, 1), plt.imshow(img), plt.title('RGB'), plt.axis('off')
plt.subplot(1, 4, 2), plt.imshow(conversion_gray_image, cmap='gray'), plt.title('Grayscale'), plt.axis('off')
plt.subplot(1, 4, 3), plt.imshow(conversion_hsv_image), plt.title('HSV'), plt.axis('off')
plt.subplot(1, 4, 4), plt.imshow(conversion_lab_image), plt.title('LAB'), plt.axis('off')
plt.tight_layout()
plt.savefig('output/conversion_image.png')

adjustment = Adjustment(1.5)
adjust_image = adjustment.adjust_contrast(img)

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1), plt.imshow(img), plt.title('Original'), plt.axis('off')
plt.subplot(1, 2, 2), plt.imshow(adjust_image), plt.title(f'Imagem com Contraste {adjustment.constant}'), plt.axis('off')
plt.tight_layout()
plt.savefig('output/adjust_image.png')

control = Control(2.2)
control_image = control.control_gammar(img)

plt.figure(figsize=(15, 6))
plt.subplot(1, 2, 1), plt.imshow(img), plt.title('Original'), plt.axis('off')
plt.subplot(1, 2, 2), plt.imshow(control_image), plt.title(f'γ = {control.gamma}'), plt.axis('off')
plt.tight_layout()
plt.savefig('output/control_image.png')