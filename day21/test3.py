import cv2 
import numpy as np

img1 = cv2.imread("img2.jpg")
img1 = cv2.resize(img1, (640, 480))

img_sqrt = np.sqrt(img1.astype(np.float32))
img_sqrt = np.clip(img_sqrt,0,255).astype(np.uint8)

# Hiển thị kết quả
cv2.imshow("anh doc1", img1)
cv2.imshow("anh img_sqrt", img_sqrt)

cv2.waitKey(0)
cv2.destroyAllWindows()
