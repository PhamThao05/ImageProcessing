import cv2
import numpy as np

# Mở camera
cap = cv2.VideoCapture(0)

# Khởi tạo background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

# Đọc khung hình đầu tiên
ret, frame = cap.read()

while ret:
    # Áp dụng background subtraction
    fgmask = fgbg.apply(frame)

    # Làm sạch mask bằng phép toán morphological (loại bỏ nhiễu nhỏ)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, None)  # Mở - loại bỏ nhiễu nhỏ
    fgmask = cv2.dilate(fgmask, None, iterations=3)  # Mở rộng vùng mask, giúp giữ lại người rõ hơn

    # Áp dụng mask vào ảnh gốc để chỉ giữ lại người
    result = cv2.bitwise_and(frame, frame, mask=fgmask)

    # Hiển thị ảnh gốc, ảnh trừ nền, và ảnh chỉ còn người
    cv2.imshow("Anh goc", frame)
    cv2.imshow("Anh sau khi trừ nền", fgmask)
    cv2.imshow("Anh chi con nguoi", result)

    # Đọc khung hình tiếp theo
    ret, frame = cap.read()

    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng camera và đóng cửa sổ
cap.release()
cv2.destroyAllWindows()
