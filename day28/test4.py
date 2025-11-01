import cv2
img = cv2.imread('img3.jpg', 0)
img = cv2.resize(img, (640, 480))
img_gaus = cv2.GaussianBlur(img, (5,5), 0)
cv2.imwrite('gaussian_filtered_image.jpg', img_gaus)
cv2.imshow('Original Image', img)
cv2.imshow('Gaussian Filtered Image', img_gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()
