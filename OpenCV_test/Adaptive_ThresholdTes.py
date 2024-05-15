import cv2

image = cv2.imread('lettuce0514.jpg', cv2.IMREAD_GRAYSCALE)
adaptive_thresh_mean = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY, 11, 2)
adaptive_thresh_gaussian = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 2)

cv2.imshow('Original Image', image)
cv2.imshow('Adaptive Threshold Mean', adaptive_thresh_mean)
cv2.imshow('Adaptive Threshold Gaussian', adaptive_thresh_gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()
