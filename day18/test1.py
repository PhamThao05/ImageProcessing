import cv2
import numpy as np
img = cv2.imread("img3.jpg")
img = img.astype(np.float64)/ 255
#B,G,R = cv2.split(img)
#B = B.astype(np.float32)
#G = G.astype(np.float32)
#R = R.astype(np.float32)

#Y = 16 + (65.481 * R + 128.553 * G + 24.966 * B) / 255
#Cb = 128 + (-37.797 * R - 74.204 * G + 112.000 * B) / 255
#Cr = 128 + (112.000 * R - 93.786 * G - 18.214 * B) / 255
#img_new = cv2.merge([Y,Cr,Cb])
#img_new = img_new.astype(np.uint8)


#C = 255 - R
#M = 255 - G
#Y = 255 - B
#img1 = cv2.merge([C,M,Y])
#img1 = img1.astype(np.uint8)

K = 1 - np.max(img, axis=2)
C = (1 - img[...,2] - K) / (1-K)
M = (1 - img[...,1] - K) / (1-K)
Y = (1 - img[...,0] - K) / (1-K)
img_cmy = (np.dstack((C,M,Y)) * 255).astype(np.uint8)

cv2.imshow("anh RGB", img)
#cv2.imshow("anh CMY", img1 [...,::-1]) #Đảo ngược 
#cv2.imshow("anh YRcCb", img_new)
cv2.imshow("anh cmy", img_cmy [...,::-1])
cv2.waitKey(0)
cv2.destroyAllWindows()