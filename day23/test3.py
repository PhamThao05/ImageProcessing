import cv2
import numpy as np
img = cv2.imread('img4.jpg',0)
img = cv2.resize(img, (640, 480))
b = cv2.convertScaleAbs(img, alpha=1.5, beta=0) #tăng độ tương phản
img_new = np.clip(b,0,255).astype(np.uint8)
imgs = cv2.hconcat([img,img_new])
cv2.imshow('anh goc va anh sau khi tang tuong phan',imgs)
cv2.waitKey(0)
cv2.destroyAllWindows()