#RPI.GPIO
import RPi.GPIO as GPIO
import time

# GPIO 핀 번호 설정 방식 선택
GPIO.setmode(GPIO.BCM)

# 사용할 GPIO 핀 번호, 예를 들어 GPIO 17
pin = 17

# GPIO 핀의 모드를 입력으로 설정
GPIO.setup(pin, GPIO.IN)

try:
    while True:
        # 센서에서 신호 읽기
        water_detected = GPIO.input(pin)
        if water_detected:
            print("O")
        else:
            print("X")
        time.sleep(1)  # 1초 간격으로 읽기
except KeyboardInterrupt:
    print("Program stopped by user")
finally:
    GPIO.cleanup()  # GPIO 설정 초기화

#gpiozero 사용
# from gpiozero import Button
# from signal import pause

# # 사용할 GPIO 핀 번호, 예를 들어 GPIO 17
# water_sensor = Button(17)

# def high():
#     print("O")

# def low():
#     print("X")

# water_sensor.when_pressed = high
# water_sensor.when_released = low

# pause()
