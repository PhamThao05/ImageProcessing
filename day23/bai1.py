import cv2
import numpy as np
img = cv2.imread('img4.jpg')
img = cv2.resize(img, (640, 480))
# Tăng sáng/tương phản trên kênh L (LAB) để giữ màu
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
L, A, B = cv2.split(lab)
L = cv2.convertScaleAbs(L, alpha=1.3, beta=15)  # chỉ chỉnh độ sáng/contrast kênh L
out = cv2.merge([L, A, B])
out = cv2.cvtColor(out, cv2.COLOR_LAB2BGR)
imgs = cv2.hconcat([img,out])
cv2.imshow('anh goc va anh sau khi tang sang tuong phan',imgs)
cv2.waitKey(0)
cv2.destroyAllWindows()