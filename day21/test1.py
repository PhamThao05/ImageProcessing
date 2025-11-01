import cv2
import numpy as np
img1 = cv2.imread("img3.jpg")
img1 = cv2.resize(img1, (640,480))
mask = np.zeros(img1.shape[:2], dtype="uint8")
mask = cv2.rectangle(mask, (200,200),(400,400),255,-1) #type:ignore
img_new = cv2.bitwise_and(img1, img1, mask=mask)
cv2.imshow("anh goc", img1)
cv2.imshow("anh mask", mask)
cv2.imshow("anh sau xu ly", img_new)
cv2.waitKey(0)
cv2.destroyAllWindows()