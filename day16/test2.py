import cv2

img = cv2.imread("img3.jpg")
size = (640,480)
img_new = cv2.resize(img,size) # kích thước ảnh[chiều rộng, chiều cao]
img_o = img_new.copy()
img2 = cv2.transpose(img_new)
cv2.imshow("anh goc", img_new)
cv2.imshow("anh goc transpose", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()