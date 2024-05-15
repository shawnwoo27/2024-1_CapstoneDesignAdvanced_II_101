import cv2
import numpy as np

image = cv2.imread('lettuce0514.jpg', cv2.IMREAD_GRAYSCALE)
adaptive_thresh_mean = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11, 2)
kernel = np.ones((3, 3), np.uint8)

# # 침식
# eroded = cv2.erode(image, kernel, iterations=1)
# # 팽창
# dilated = cv2.dilate(image, kernel, iterations=1)
# # 열기
# opened = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
# # 닫기
# closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# 침식
eroded = cv2.erode(adaptive_thresh_mean, kernel, iterations=1)
# 팽창
dilated = cv2.dilate(adaptive_thresh_mean, kernel, iterations=1)
# 열기
opened = cv2.morphologyEx(adaptive_thresh_mean, cv2.MORPH_OPEN, kernel)
# 닫기
closed = cv2.morphologyEx(adaptive_thresh_mean, cv2.MORPH_CLOSE, kernel)

cv2.imshow('Original Image', adaptive_thresh_mean)
cv2.imshow('Eroded Image', eroded)
cv2.imshow('Dilated Image', dilated)
cv2.imshow('Opened Image', opened)
cv2.imshow('Closed Image', closed)
cv2.waitKey(0)
cv2.destroyAllWindows()
