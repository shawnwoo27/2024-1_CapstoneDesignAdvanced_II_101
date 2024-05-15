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

    # 녹색의 HSV 범위 정의
    lower_green = np.array([35, 100, 100])
    upper_green = np.array([85, 255, 255])

    # 녹색 부분 마스크 생성
    mask_hsv = cv2.inRange(hsv, lower_green, upper_green)

    # 적응형 이진화와 HSV 마스크 결합
    combined_mask = cv2.bitwise_and(mask_hsv, adaptive_thresh)

    # 모폴로지 연산 (침식 후 팽창)
    kernel = np.ones((5, 5), np.uint8)
    combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_CLOSE, kernel)
    combined_mask = cv2.morphologyEx(combined_mask, cv2.MORPH_OPEN, kernel)

    # 큰 컨투어 선택
    contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        combined_mask = np.zeros_like(combined_mask)
        cv2.drawContours(combined_mask, [largest_contour], -1, 255, thickness=cv2.FILLED)

    # 녹색 부분만 추출
    green_parts = cv2.bitwise_and(image, image, mask=combined_mask)

    # 녹색 픽셀 개수 계산
    green_pixel_count = cv2.countNonZero(combined_mask)
    print(f"Number of green pixels: {green_pixel_count}")

    # 원본 이미지와 녹색 부분 이미지 시각화
    cv2.imshow('Original Image', image)
    cv2.imshow('Green Parts', green_parts)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
