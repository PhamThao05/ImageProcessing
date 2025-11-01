#lọc song phương
import cv2
img = cv2.imread('img3.jpg')
img = cv2.resize(img, (640, 480))
mean = cv2.blur(img, (9,9))
biltateral = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow('anh goc',img)
cv2.imshow('loc trung binh', mean)
cv2.imshow('loc song phuong', biltateral)
cv2.waitKey(0)
cv2.destroyAllWindows()