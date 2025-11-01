import cv2
import numpy as np
img = cv2.imread('img3.jpg', 0)
img = img.astype(np.float32)
img = cv2.resize(img, (640, 480))
c = 255 / np.log(1 + np.max(img))
img_log = c*(np.log(img + 1))
img_log = np.array(img_log, dtype=np.uint8)
img_log = np.clip(img_log, 0, 255)
cv2.imshow('Original Image', img.astype(np.uint8))
cv2.imshow('Log Transformed Image', img_log)
cv2.waitKey(0)
cv2.destroyAllWindows()