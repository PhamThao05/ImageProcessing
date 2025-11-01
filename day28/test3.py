import cv2
import numpy as np
img = cv2.imread('img3.jpg',0)
img = img.astype(np.float32)
img = cv2.resize(img, (640, 480))
dst = cv2.blur(src=img, ksize=(5,5))
cv2.imshow('Original Image', img.astype(np.uint8))
cv2.imshow('Averaging Filtered Image', dst.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()