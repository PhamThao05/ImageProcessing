import cv2
import numpy as np
img = cv2.imread('img4.jpg', 0)
img = cv2.resize(img, (640, 480))
c, e , gamma = 1,0,3
img_exp = c*(255*(img/255)**gamma)
img_exp = np.array(img_exp, dtype=np.uint8)
cv2.imshow('Original Image', img)
cv2.imshow('Gamma Corrected Image', img_exp)
cv2.waitKey(0)
cv2.destroyAllWindows()
