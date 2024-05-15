import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# 스크립트의 현재 디렉토리 얻기
script_dir = os.path.dirname(os.path.abspath(__file__))

# 이미지 경로 설정 (스크립트와 동일한 디렉토리)
image_path = os.path.join(script_dir, 'lettuce0514.jpg')

# 이미지 읽기
image = cv2.imread(image_path)

# 이미지가 제대로 읽혔는지 확인
if image is None:
    print("Error: Image not found or unable to load.")
else:
    # BGR에서 HSV로 변환
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # HSV 채널 분리
    h, s, v = cv2.split(hsv)

    # 히스토그램 계산 및 시각화
    plt.figure(figsize=(18, 6))

    plt.subplot(1, 3, 1)
    plt.hist(h.ravel(), bins=180, range=[0, 180], color='r')
    plt.title('Hue Channel Histogram')
    plt.xlabel('Hue')
    plt.ylabel('Frequency')

    plt.subplot(1, 3, 2)
    plt.hist(s.ravel(), bins=256, range=[0, 256], color='g')
    plt.title('Saturation Channel Histogram')
    plt.xlabel('Saturation')
    plt.ylabel('Frequency')

    plt.subplot(1, 3, 3)
    plt.hist(v.ravel(), bins=256, range=[0, 256], color='b')
    plt.title('Value Channel Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()
