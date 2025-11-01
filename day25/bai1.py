import cv2
import matplotlib.pyplot as plt

# Đọc ảnh
img = cv2.imread('img3.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Tách 3 kênh
r, g, b = cv2.split(img_rgb)

# Vẽ histogram
plt.figure(figsize=(10,5))
plt.subplot(1, 3, 1)
plt.hist(r.ravel(), 256, [0,256], color='red')
plt.title('Histogram R')

plt.subplot(1, 3, 2)
plt.hist(g.ravel(), 256, [0,256], color='green')
plt.title('Histogram G')

plt.subplot(1, 3, 3)
plt.hist(b.ravel(), 256, [0,256], color='blue')
plt.title('Histogram B')

plt.tight_layout()
plt.show()