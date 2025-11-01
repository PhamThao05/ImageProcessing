import cv2
import numpy as np

# Hàm áp dụng Sobel với các kích thước kernel khác nhau
def apply_sobel(gray, ksize):
    sobel_x = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=ksize)
    sobel_y = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=ksize)
    magnitude = cv2.magnitude(sobel_x, sobel_y)
    return np.uint8(np.absolute(magnitude))

# Hàm áp dụng filter 2D với kernel Sobel 3x3
def apply_filter2D(gray):
    Hx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float32)  # Kernel Sobel theo x
    Hy = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float32)  # Kernel Sobel theo y

    sobel_filter_x = cv2.filter2D(gray, -1, Hx)
    sobel_filter_y = cv2.filter2D(gray, -1, Hy)

    # Đảm bảo sobel_filter_x và sobel_filter_y có kiểu float32 trước khi tính magnitude
    sobel_filter_x = sobel_filter_x.astype(np.float32)
    sobel_filter_y = sobel_filter_y.astype(np.float32)

    # Tính toán magnitude của Sobel sau khi áp dụng filter 2D
    sobel_filter_magnitude = cv2.magnitude(sobel_filter_x, sobel_filter_y)
    return np.uint8(np.absolute(sobel_filter_magnitude))

# Hàm hiển thị kết quả
def show_result(sobel_3x3, sobel_5x5, sobel_7x7, sobel_filter_magnitude):
    cv2.imshow('Sobel Magnitude 3x3', sobel_3x3)
    cv2.imshow('Sobel Magnitude 5x5', sobel_5x5)
    cv2.imshow('Sobel Magnitude 7x7', sobel_7x7)
    cv2.imshow('Sobel Magnitude (Filter 2D)', sobel_filter_magnitude)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Hàm xử lý ảnh
def process_image(image_path):
    # Đọc ảnh màu
    img = cv2.imread(image_path)  # Thay 'img3.jpg' bằng tên tệp ảnh của bạn
    img = cv2.resize(img, (640, 480))  # Đảm bảo kích thước ảnh phù hợp

    # Kiểm tra nếu ảnh đã được đọc thành công
    if img is None:
        print("Không thể đọc ảnh. Kiểm tra lại đường dẫn tệp ảnh.")
        return

    # Chuyển ảnh màu sang ảnh xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Áp dụng Sobel với các mặt nạ có kích thước khác nhau
    sobel_3x3 = apply_sobel(gray, ksize=3)
    sobel_5x5 = apply_sobel(gray, ksize=5)
    sobel_7x7 = apply_sobel(gray, ksize=7)

    # Áp dụng filter 2D với kernel Sobel 3x3
    sobel_filter_magnitude = apply_filter2D(gray)

    # Hiển thị kết quả
    show_result(sobel_3x3, sobel_5x5, sobel_7x7, sobel_filter_magnitude)

# Chạy chương trình
if __name__ == "__main__":
    process_image(r'D:/CloneRepoImageProcessing/ImageProcessing/img3.jpg')  # Thay bằng đường dẫn ảnh của bạn
