import cv2
img = cv2.imread('img3.jpg',0)
img = cv2.resize(img, (640, 480))
img_dedian = cv2.medianBlur(img,7)
cv2.imwrite('img_anh.jpg', img_dedian)
cv2.imshow('anh goc',img)
cv2.imshow('media blurring', img_dedian)
cv2.waitKey(0)
cv2.destroyAllWindows()