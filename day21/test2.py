import cv2
import numpy as np
img1 = cv2.imread("img2.jpg")
img2 = cv2.imread("img3.jpg")
img1 = cv2.resize(img1, (640,480))
img2 = cv2.resize(img2,(640,480))
img_add = cv2.add(img1, img2)
cv2.imshow("anh goc 1", img1)
cv2.imshow("anh goc 2", img2)
cv2.imshow("anh bien doi", img_add)
cv2.waitKey(0)
cv2.destroyAllWindows()