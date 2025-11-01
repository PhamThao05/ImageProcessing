import cv2
import numpy as np
img = cv2.imread("img3.jpg")
#imgHSV = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("anh RGB", img)
cv2.imshow("anh xam", imggray)
#cv2.imshow("anh HSV", imgHSV)
cv2.waitKey(0)
cv2.destroyAllWindows()