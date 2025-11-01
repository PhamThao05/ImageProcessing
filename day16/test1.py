import cv2

img = cv2.imread("img2.jpg")
size = (640, 480)
img_new = cv2.resize(img, size)
img_o = img_new.copy()

# Kích thước ảnh
[h, w, c] = img_new.shape
px = img_new[20, 30]
print("px:", px)
#for i in range(40): 
    #for j in range(60): 
        #img_new[i,j] = (0,255,0) 
        #print(['pixel:'])
                
# Thay đổi màu pixel theo vùng 40x60 đầu tiên (hàng 0-39, cột 0-59) thành xanh lá
img_new[0:40, 0:60] = [255, 0, 0]  # [B, G, R]

# Ghép ảnh theo chiều ngang
img_concat = cv2.hconcat([img_o, img_new])
#img_concat = cv2.vconcat([img_o, img_new]) #theo chiều dọc

cv2.imshow("anh thay doi", img_concat)
cv2.waitKey(0)
cv2.destroyAllWindows()
