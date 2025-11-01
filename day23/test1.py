import cv2
import numpy as np                                        
img = cv2.imread('img4.jpg',0)
img = cv2.resize(img, (640, 480))
r_min = np.min(img).astype(np.float32)
r_max = np.max(img).astype(np.float32)
g=(img.astype(np.float32)-r_min)/(r_max - r_min)*255
img_new = np.clip(g,0,255).astype(np.uint8)
imgs = cv2.hconcat([img,img_new])
cv2.imshow('anh goc va anh sau khi tang cung tuong phan',imgs)
cv2.waitKey(0)
cv2.destroyAllWindows()