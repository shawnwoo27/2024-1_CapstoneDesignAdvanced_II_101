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

    # 녹색의 HSV 범위 정의
    lower_green = np.array([35, 100, 100])
    upper_green = np.array([85, 255, 255])

    # CLAHE를 적용하여 조명 조건 균일화
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    v = clahe.apply(v)

    # HSV 채널을 병합
    hsv_clahe = cv2.merge([h, s, v])

    # 다시 BGR로 변환
    image_clahe = cv2.cvtColor(hsv_clahe, cv2.COLOR_HSV2BGR)

    # BGR에서 HSV로 변환
    hsv = cv2.cvtColor(image_clahe, cv2.COLOR_BGR2HSV)

     # BGR에서 HSV로 변환
    hsv = cv2.cvtColor(image_clahe, cv2.COLOR_BGR2HSV)

    # 녹색 부분 마스크 생성
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # 녹색 부분만 추출
    green_parts = cv2.bitwise_and(image_clahe, image_clahe, mask=mask)

    # 녹색 픽셀 개수 계산
    green_pixel_count = cv2.countNonZero(mask)
    print(f"Number of green pixels: {green_pixel_count}")

    # 원본 이미지와 CLAHE 적용 이미지, 녹색 부분 이미지 시각화
    cv2.imshow('Original Image', image)
    cv2.imshow('CLAHE Image', image_clahe)
    cv2.imshow('Green Parts', green_parts)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
