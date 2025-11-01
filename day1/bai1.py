import cv2
import numpy as np

# Đọc ảnh màu (chú ý dấu gạch chéo đôi hoặc dấu gạch chéo thẳng trong đường dẫn)
img = cv2.imread(r'D:/CloneRepoImageProcessing/ImageProcessing/img3.jpg')  # Thay 'img3.jpg' bằng tên tệp ảnh của bạn
img = cv2.resize(img, (640, 480))  # Đảm bảo kích thước ảnh phù hợp

# Kiểm tra nếu ảnh đã được đọc thành công
if img is None:
    print("Không thể đọc ảnh. Kiểm tra lại đường dẫn tệp ảnh.")
else:
    # Chuyển ảnh màu sang ảnh xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Áp dụng Sobel với kernel 3x3 (đạo hàm theo chiều x và y)
    sobel_x = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=3)
    sobel_y = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=3)

    # Chuyển đổi kết quả Sobel thành kiểu float32 (đảm bảo cùng kiểu dữ liệu)
    sobel_x = sobel_x.astype(np.float32)
    sobel_y = sobel_y.astype(np.float32)

    # Tính toán magnitude của Sobel (phát hiện biên)
    sobel_magnitude = cv2.magnitude(sobel_x, sobel_y)

    # Chuyển đổi kết quả Sobel về kiểu uint8 để hiển thị
    sobel_magnitude = np.uint8(np.absolute(sobel_magnitude))

    # Kernel Sobel theo các giá trị bạn đã cung cấp
    Hx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)  # Kernel Sobel theo x
    Hy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32)  # Kernel Sobel theo y

    # Áp dụng filter 2D với kernel Sobel (chỉ dùng kernel 3x3)
    sobel_filter_x = cv2.filter2D(gray, -1, Hx)
    sobel_filter_y = cv2.filter2D(gray, -1, Hy)

    # Đảm bảo sobel_filter_x và sobel_filter_y có kiểu float32 trước khi tính magnitude
    sobel_filter_x = sobel_filter_x.astype(np.float32)
    sobel_filter_y = sobel_filter_y.astype(np.float32)

    # Tính toán magnitude của Sobel sau khi áp dụng filter 2D
    sobel_filter_magnitude = cv2.magnitude(sobel_filter_x, sobel_filter_y)

    # Chuyển đổi kết quả Sobel sau filter 2D về kiểu uint8 để hiển thị
    sobel_filter_magnitude = np.uint8(np.absolute(sobel_filter_magnitude))

    # Hiển thị kết quả
    cv2.imshow('Sobel Magnitude (OpenCV)', sobel_magnitude)
    cv2.imshow('Sobel Magnitude (Filter 2D)', sobel_filter_magnitude)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
