import cv2
import numpy as np
import matplotlib.pyplot as plt
img_gray = cv2.imread('img2.jpg',0)
img_gray = cv2.resize(img_gray, (640, 480))
h,w = img_gray.shape[:2]
#hist = np.zeros([256], np.int32)
#for y in range(h):
#    for x in range(w):
#        g = int(img_gray[y,x])
#        hist[g] += 1
#N = h*w
#hist_norm = hist / float(N)
hist = cv2.calcHist([img_gray],[0],None,[256],[0,256])
plt.figure('Histogram'); plt.plot(hist, color='orange')
plt.title('Histogram cua anh'); plt.xlabel('Gia tri muc xam')
plt.ylabel('s luong diem anh'); plt.figure('anh dau vao')
plt.imshow(img_gray, cmap='gray'); plt.axis('off'); plt.show()