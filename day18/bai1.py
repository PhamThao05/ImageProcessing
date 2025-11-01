import cv2
import numpy as np
img = cv2.imread("img2.jpg")
#thay đổi kích thước ảnh
size = (640, 480)
img_new = cv2.resize(img, size)
img_o = img_new.copy()
#in ra màn hình các thông tin: số kênh, chiều cao, chiều dài ảnh
[h, w, c] = img_o.shape
px = img_new[20, 30]
print("px:", px)

#chuyen anh sang mau xam i1
imggray = cv2.cvtColor(img_o, cv2.COLOR_BGR2GRAY)

#6. chuyen anh mau i2


#7. HSV
img_hsv = cv2.cvtColor(img_o, cv2.COLOR_BGR2HSV)

#8. tach 3 kenh mau rieng

#9. chuyen anh sang nhi phan

#10. chuyen anh i2 sang nhi nhan

cv2.imshow("doc anh", img)
cv2.imshow("anh moi", img_o)
cv2.imshow("anh xam", imggray)
cv2.imshow("anh hsv", img_hsv [...,::-1])
cv2.waitKey(0)
cv2.destroyAllWindows()

#11. ghi cac anh ra file (*.jpg)
cv2.imwrite('img.jpg', img)
cv2.imwrite('img_o.jpg', img_o)
cv2.imwrite('imggray.jpg', imggray)
cv2.imwrite('img_hsv.jpg', img_hsv)