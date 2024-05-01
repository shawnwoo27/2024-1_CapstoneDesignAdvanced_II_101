import smbus2
import time

# I2C 버스 1을 사용 (라즈베리 파이 모델에 따라 다를 수 있음)
bus = smbus2.SMBus(1)

# BH1750 주소 (일반적으로 0x23, 모드에 따라 0x5C도 가능)
address = 0x23

# 측정 모드
# 0x10: 일반 모드
# 0x11: 원 스톱 고해상도 모드
mode = 0x10

def read_light(addr=address):
    data = bus.read_i2c_block_data(addr, mode, 2)
    # 조도 측정식, data[0]와 data[1]은 I2C 통신을 통해 BH1750 센서로부터 읽은 두 바이트의 데이터
    return (data[0] << 8 | data[1]) / 1.2

try:
    while True:
        light_level = read_light()
        print(f"Light Level: {light_level} lx")
        time.sleep(1)
except KeyboardInterrupt:
    print("Measurement stopped by User")
    bus.close()
