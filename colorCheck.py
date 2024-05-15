import cv2
import numpy as np
import matplotlib.pyplot as plt

# lower_green과 upper_green 값 정의
lower_green = np.array([35, 100, 100])
upper_green = np.array([85, 255, 255])

# HSV 값을 시각화하는 함수 정의
def visualize_hsv_color(hsv_value):
    # 100x100 크기의 이미지를 생성
    hsv_image = np.full((100, 100, 3), hsv_value, dtype=np.uint8)
    
    # HSV 이미지를 BGR로 변환
    bgr_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
    
    # BGR 이미지를 RGB로 변환 (Matplotlib에서 시각화하기 위해)
    rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
    
    return rgb_image

# lower_green과 upper_green 값을 시각화
lower_green_rgb = visualize_hsv_color(lower_green)
upper_green_rgb = visualize_hsv_color(upper_green)

# 시각화
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Lower Green')
plt.imshow(lower_green_rgb)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Upper Green')
plt.imshow(upper_green_rgb)
plt.axis('off')

plt.show()
