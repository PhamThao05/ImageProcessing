import cv2
import numpy as np
img = cv2.imread('img3.jpg')
img = cv2.resize(img, (640, 480))
k = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
img_laplacian = cv2.filter2D(img, -1, k)
cv2.imshow('anh goc',img)
cv2.imshow('laplacian', img_laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()