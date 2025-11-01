import cv2

# Đường dẫn tới file ảnh
file_path = 'img2.jpg'  # đổi thành tên file của bạn

# Đọc ảnh
image = cv2.imread(file_path,0)

    # Chuyển sang màu xám
#gray_image = cv2.cvtColor(image)

    # Hiển thị ảnh xám
cv2.imshow('Gray Image', image)
cv2.waitKey(0)  # nhấn phím bất kỳ để đóng cửa sổ
cv2.destroyAllWindows()

    # Lưu ảnh xám
cv2.imwrite('output_gray.jpg', image)
