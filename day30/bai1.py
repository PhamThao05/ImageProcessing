from calendar import c
import matplotlib.pyplot as plt
import numpy as np
from numpy import fft
import math
import cv2

def motion_process(image_size, motion_angle):
    PSF = np.zeros(image_size)
    print(image_size)
    center_position = (image_size[0] - 1) / 2
    print(center_position)
    slope_tan = math.tan(motion_angle * math.pi / 180)
    slope_cot = 1 / slope_tan
    if slope_tan <= 1:
        for i in range(15):
            offset = round(i * slope_tan)
            PSF[int(center_position + offset), int(center_position - offset)] = 1
        return PSF / PSF.sum()
    else:
        for i in range(15):
            offset = round(i * slope_cot)
            PSF[int(center_position - offset), int(center_position + offset)] = 1
        return PSF / PSF.sum()
def wiener(input, PSF, eps, K=0.01):
    input_fft = fft.fft2(input)
    PSF_fft = fft.fft2(PSF) + eps
    PSF_fft_1 = np.conj(PSF_fft) / (np.abs(PSF_fft) ** 2 + K)
    result= fft.ifft2(input_fft * PSF_fft_1)
    result = np.abs(fft.fftshift(result))
    return result
if __name__ == "__main__":
    img = cv2.imread('image.jpg',0)
    h, w = img.shape[:2]
    PSF = motion_process((h, w), 75)
    result = wiener(img, PSF, 1e-3)
    """ plt.figure("PSF")
    plt.imshow(result, cmap='gray')
    plt.show() """
    imgs = cv2.hconcat([img, result.astype(np.uint8)])
    cv2.imshow('result', imgs)
    cv2.waitKey(0)
    cv2.destroyAllWindows()