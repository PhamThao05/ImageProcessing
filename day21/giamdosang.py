import cv2
import numpy as np
img1 = cv2.imread("img2.jpg")
img1 = cv2.resize(img1, (640,480))
img_sub = cv2.subtract(img1, 100)
img_add = cv2.add(img1, 100)
cv2.imshow("anh goc 1", img1)
cv2.imshow("anh bien doi", img_sub)
cv2.imshow("anh bien doi add", img_add)
cv2.waitKey(0)
cv2.destroyAllWindows()