import cv2
import numpy as np
from matplotlib import pyplot as plt

# 이미지 읽기
image_path = 'lettuce0514.jpg'  # 상추 이미지 경로
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 블러링 및 엣지 검출
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)

# 컨투어 찾기
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 가장 큰 컨투어 선택 (가장 큰 잎)
largest_contour = max(contours, key=cv2.contourArea)

# 컨투어 면적 계산
leaf_area = cv2.contourArea(largest_contour)

# 결과 시각화
output_image = image.copy()
cv2.drawContours(output_image, [largest_contour], -1, (0, 255, 0), 2)

plt.figure(figsize=(10, 10))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.subplot(1, 2, 2)
plt.title('Detected Leaf Contour')
plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
plt.show()

print(f'Estimated leaf area: {leaf_area} square pixels')
