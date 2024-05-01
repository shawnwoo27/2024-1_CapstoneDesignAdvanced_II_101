import smbus2
import time

# I2C 버스 설정 (라즈베리 파이 모델에 따라 번호 확인 필요)
bus = smbus2.SMBus(1)

# PCF8591 디바이스 주소
address = 0x48

def read_analog(channel):
    """지정된 채널에서 아날로그 값 읽기"""
    if channel in [0, 1, 2, 3]:
        # Control byte 설정 (채널 선택)
        control_byte = 0x40 | channel
        # 읽기 명령 실행
        bus.write_byte(address, control_byte)
        bus.read_byte(address)  # 첫 번째 읽기 결과는 무시
        return bus.read_byte(address)
    else:
        return None

def convert_to_voltage(analog_value):
    """아날로그 값을 전압으로 변환"""
    max_voltage = 3.3  # 모듈의 최대 출력 전압
    max_adc = 255  # ADC의 최대 읽을 수 있는 값
    voltage = (analog_value / max_adc) * max_voltage
    return voltage

# 메인 루프
try:
    while True:
        analog_value = read_analog(0)  # 첫 번째 아날로그 채널에서 읽기
        voltage = convert_to_voltage(analog_value)
        print(f"Analog value: {analog_value}, Voltage: {voltage:.2f}V")
        time.sleep(1)
except KeyboardInterrupt:
    print("Measurement stopped by user")
    bus.close()
