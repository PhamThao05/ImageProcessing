import cv2
import numpy as np
from matplotlib import pyplot as plt

# --- a. Đọc ảnh và lọc ---
img = cv2.imread('img3.jpg', 0)
img = cv2.resize(img, (640, 480))

# Lọc trung bình (Average)
img_avg = cv2.blur(img, (9,9))

# Lọc Gaussian
img_gaus = cv2.GaussianBlur(img, (9,9), 0)

cv2.imwrite('average_filtered.jpg', img_avg)
cv2.imwrite('gaussian_filtered.jpg', img_gaus)

# Hiển thị ảnh sau khi lọc
cv2.imshow('Original Image', img)
cv2.imshow('Average Filtered Image', img_avg)
cv2.imshow('Gaussian Filtered Image', img_gaus)
cv2.waitKey(0)
cv2.destroyAllWindows()

# --- b. Vẽ Histogram trước và sau khi điều chỉnh độ tương phản ---
def plot_histogram(img, title):
    plt.figure()
    plt.title(title)
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.hist(img.ravel(), 256, [0,256])
    plt.show()

# Histogram trước điều chỉnh
plot_histogram(img_avg, 'Histogram - Average Filter')
plot_histogram(img_gaus, 'Histogram - Gaussian Filter')

# Điều chỉnh độ tương phản (tăng bằng alpha/beta)
def adjust_contrast(image, alpha=1.5, beta=20):
    # alpha: hệ số tăng contrast, beta: độ sáng thêm
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

img_avg_contrast = adjust_contrast(img_avg)
img_gaus_contrast = adjust_contrast(img_gaus)

cv2.imshow('Average Filter - Adjusted Contrast', img_avg_contrast)
cv2.imshow('Gaussian Filter - Adjusted Contrast', img_gaus_contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Histogram sau điều chỉnh độ tương phản
plot_histogram(img_avg_contrast, 'Histogram - Average Filter (Adjusted)')
plot_histogram(img_gaus_contrast, 'Histogram - Gaussian Filter (Adjusted)')

# --- c. Cân bằng Histogram ---
img_avg_eq = cv2.equalizeHist(img_avg)
img_gaus_eq = cv2.equalizeHist(img_gaus)

cv2.imshow('Average Filter - Equalized', img_avg_eq)
cv2.imshow('Gaussian Filter - Equalized', img_gaus_eq)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Histogram sau khi cân bằng
plot_histogram(img_avg_eq, 'Histogram - Average Filter (Equalized)')
plot_histogram(img_gaus_eq, 'Histogram - Gaussian Filter (Equalized)')