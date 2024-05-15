import cv2
import numpy as np
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

    # HSV에서 V 채널을 추출
    h, s, v = cv2.split(hsv)

    # 적응형 이진화 적용
    v_blur = cv2.GaussianBlur(v, (5, 5), 0)
    adaptive_thresh = cv2.adaptiveThreshold(
        v_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # 마스크 생성
    mask = adaptive_thresh

    # 녹색 부분 마스크 적용
    mask = cv2.bitwise_and(mask, mask, mask=cv2.inRange(hsv, np.array([35, 100, 100]), np.array([85, 255, 255])))

    # 모폴로지 연산 (침식 후 팽창)
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    # 녹색 부분만 추출
    green_parts = cv2.bitwise_and(image, image, mask=mask)

    # 녹색 픽셀 개수 계산
    green_pixel_count = cv2.countNonZero(mask)
    print(f"Number of green pixels: {green_pixel_count}")

    # 원본 이미지와 녹색 부분 이미지 시각화
    cv2.imshow('Original Image', image)
    cv2.imshow('Green Parts', green_parts)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
