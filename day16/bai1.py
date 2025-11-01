import cv2

img = cv2.imread("img2.jpg")
img2 = cv2.imread("img3.jpg")

size = (640, 480)
img_new1 = cv2.resize(img, size)
img_new2 = cv2.resize(img2, size)


[h, w, c] = img.shape
px = img[20, 30]
px = img2[20, 30]
print("px:", px)
img[0:40, 0:60]
img2[0:40, 0:60]
img_c = cv2.hconcat([img_new1, img_new2])

image = cv2.imread(img_c,0)
cv2.imwrite('o.jpg', image)


cv2.imshow("1", img_c)
cv2.waitKey(0)
cv2.destroyAllWindows()
