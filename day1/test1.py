import cv2
import numpy as np
img = cv2.imread('img3.jpg',0)
img = cv2.resize(img, (640, 480))
m_prewittx = np.array([[-1, 0, 1],
                      [-1, 0, 1],
                        [-1, 0, 1]])
m_prewitty = np.array([[1, 1, 1],
                      [0, 0, 0],
                        [-1, -1, -1]])
img_prewittx = cv2.filter2D(img, -1, m_prewittx)
img_prewitty = cv2.filter2D(img, -1, m_prewitty)
img_prewittxy = np.sqrt(img_prewittx.astype('float32')**2 + img_prewitty.astype('float32')**2).astype('uint8')
print("prewitt x", img_prewittx)
print("prewitt y", img_prewitty)
cv2.imshow('anh goc', img)
cv2.imshow('prewitt x', img_prewittx)
cv2.imshow('prewitt y', img_prewitty)
cv2.imshow('prewitt xy', img_prewittxy)
cv2.waitKey(0)
cv2.destroyAllWindows()