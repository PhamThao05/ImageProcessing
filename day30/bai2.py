# ==========================================
# Lọc nhiễu và khôi phục ảnh theo nhiều phương pháp
# ==========================================
import cv2
import numpy as np
from scipy.signal import wiener

# ----------- 1. Đọc ảnh -------------
img = cv2.imread('img3.jpg', 0)
img = cv2.resize(img, (640, 480))

# Lọc trung vị (median filter)
img_median = cv2.medianBlur(img, 3)

# Lọc thông thấp (Gaussian Low-pass)
img_low = cv2.GaussianBlur(img, (5, 5), 0)

# Lọc thông cao (High-pass)
# kernel thông cao (tăng biên, giảm nền mờ)
hp_kernel = np.array([[-1, -1, -1],
                      [-1,  9, -1],
                      [-1, -1, -1]])
img_high = cv2.filter2D(img, -1, hp_kernel)

# Lọc Wiener (khôi phục ảnh nhiễu + nhòe)
img_wiener = wiener(img, (5, 5))
img_wiener = np.uint8(np.clip(img_wiener, 0, 255))

# ----------- 3. Hiển thị kết quả -------------
cv2.imshow('Anh goc', img)
cv2.imshow('Loc trung vi', img_median)
cv2.imshow('Loc thong thap', img_low)
cv2.imshow('Loc thong cao', img_high)
cv2.imshow('Loc Wiener', img_wiener)

cv2.waitKey(0)
cv2.destroyAllWindows()
