import time
import board
import adafruit_dht

# GPIO 핀 설정
dht_device = adafruit_dht.DHT11(board.D4)  # GPIO 핀 번호를 D4로 설정, 라즈베리파이 보드에 맞게 조정

while True:
    try:
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        if humidity is not None and temperature is not None:
            print(f"Temperature: {temperature:.1f} C, Humidity: {humidity:.1f}%")
        else:
            print("Failed to retrieve data from humidity sensor")

    except RuntimeError as error:
        print(error.args[0])

    time.sleep(2)  # 2초 간격으로 데이터 읽기
