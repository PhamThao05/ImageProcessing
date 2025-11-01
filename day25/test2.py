import cv2
import numpy as np
img = cv2.imread('img3.jpg',0)
img = cv2.resize(img, (640, 480))
img1 = cv2.equalizeHist(img)
cv2.imshow('anh goc',img)
cv2.imshow('anh sau khi can bang phoi mau',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()