#lọc phông thấp lý tưởng
import cv2
import numpy as np
img = cv2.imread('img3.jpg',0)
img = cv2.resize(img, (640, 480))
M,N = img.shape[:2]
H = np.zeros((M,N), np.float32)
D0 = 10 # 5, 15, 30, 80, 100
for u in range(M):
    for v in range(N):
        D = np.sqrt((u-M/2)**2 + (v-N/2)**2)
        if D <= D0 :
            H[u,v] = 1
        else:
            H[u,v] = 0  
#for u in range(M):
#    for v in range(N):
#        D = np.sqrt((u-M/2)**2 + (v-N/2)**2) #PHONG CAO
#        if D <= D0 :
#            H[u,v] = 0
#        else:
#            H[u,v] = 1 
dft = np.fft.fft2(img)
dft_shift = np.fft.fftshift(dft)
dft_shift_filtered = dft_shift * H
dft_ifft_shift = np.fft.ifftshift(dft_shift_filtered)
img_back = np.abs(np.fft.ifft2(dft_ifft_shift))
cv2.imshow('anh goc',img)
cv2.imshow('loc phong thap ly tuong', img_back.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()