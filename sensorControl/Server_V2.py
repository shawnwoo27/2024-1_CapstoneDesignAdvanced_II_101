# flask 사용/ jsonify - json 데이터 처리/ render_template - flask가 templates 폴더 위치를 찾게 해줌.
from flask import Flask, jsonify, render_template

# IC2 버스를 사용하기 위한 라이브러리
import smbus2

# 시간 관련 python 내장 라이브러리
import time
from datetime import datetime, timedelta

# GPIO 핀 번호 확인용 라이브러리
import board

#온습도 센서 모듈 회사에서 제공하는 라이브러리
import adafruit_dht

# csv 파일 처리용
import csv
from collections import defaultdict

# 병렬적인 작업을 위한 스레드 라이브러리
import threading

app = Flask(__name__)

# GPIO 핀 설정, DHT11
dht_device = adafruit_dht.DHT11(board.D4)

# IC2 버스 1을 사용
bus = smbus2.SMBus(1)

# BH1750 주소 (일반적으로 0x23, 모드에 따라 0x5C도 가능)
address = 0x23

# BH1750 측정 모드 설정
mode = 0x10

# CSV 파일 경로 설정
CSV_FILE_PATH = 'sensor_data.csv'

# BH1750 조도 계산식
def read_light(addr=address):
    data = bus.read_i2c_block_data(addr, mode, 2)
    light_level = (data[0] << 8 | data[1]) / 1.2
    return light_level


# 센서 데이터를 처리하는 함수
def sensor_data_process():
    try:
        temperature = dht_device.temperature
        light = read_light()
        humidity = dht_device.humidity

        if temperature is not None and humidity is not None and light is not None:
            return temperature, light, humidity
        else:
            return None, None, None

    except RuntimeError as error:
        print("Error:", str(error))
        return None, None, None


# CSV 파일에 데이터를 추가하는 함수
def write_to_csv(datetime_str, temperature, light, humidity):
    with open(CSV_FILE_PATH, mode='a') as file:
        writer = csv.writer(file)
        writer.writerow([datetime_str, temperature, light, humidity])

# CSV 파일 읽기
def read_csv(file_path):
    data = defaultdict(list)
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            date_time = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
            date_str = date_time.strftime('%Y-%m-%d')
            temperature = row[1]
            light = row[2]
            humidity = row[3]
            data[date_str].append({
                'time': date_time.strftime('%H:%M:%S'),
                'temperature': temperature,
                'light': light,
                'humidity': humidity
            })
    return data


# 센서 데이터를 주기적으로 읽어서 CSV 파일에 저장하는 스레드 동작 함수
def save_sensor_data_to_csv():
    while True:
        try:
            # 현재 시간 확인
            now = datetime.now()
            minute = now.minute

            # 매 정시와 매 정시 30분에만 데이터 저장
            if minute == 0 or minute == 30:
                temperature, light, humidity = sensor_data_process()

                if temperature is not None and light is not None and humidity is not None:
                    # 현재 시간 문자열 반환
                    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    # csv 파일에 데이터 추가
                    write_to_csv(current_time, temperature, light, humidity)
                    print("Data added to CSV at: " + f'일시-{current_time}, 온도-{temperature:.1f}°C, 조도-{light:.1f} lux, 습도-{humidity}%')
                else:
                    print("Failed to receive data from sensor")
            else:
                print("Data save skipped", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            
            # 1분마다 작업 수행
            time.sleep(60)

        except Exception as e:
            print("An error occurred:", e)


# 데이터 읽기 -> 추후 해당 위치 조정 필요.
data = read_csv(CSV_FILE_PATH)

# 라우팅 설정
@app.route('/')
def main():
    return render_template('main.html')

@app.route('/cam-check')
def cam_check():
    return render_template('camCheck.html')

@app.route('/daily-photo')
def daily_photo():
    dates = list(data.keys())

    return render_template('DailyPhoto.html', dates=dates)

@app.route('/daily-photo/<date>')
def date_page(date):
    if date in data:
        daily_data = data[date]
    else:
        daily_data = []
    return render_template('DailyPlantState.html', date=date, daily_data=daily_data)


# 센서 데이터 처리 라우팅
@app.route('/sensor_data')
def sensor_data_route():
    temperature, light, humidity = sensor_data_process()

    if temperature is not None and humidity is not None and light is not None:
        return jsonify({
            'temperature': temperature,
            'light': light,
            'humidity': humidity
        })
    else:
        return jsonify({'error': 'Failed to retrieve data from sensor'}), 500


if __name__ == '__main__':
    # 스레드 생성 및 시작
    sensor_data_thread = threading.Thread(target=save_sensor_data_to_csv)
    sensor_data_thread.start()

    # 디버그 모드 False, 0.0.0.0 모든 사용자로부터, 서버 여는 포트 8080
    app.run(debug=False, host='0.0.0.0', port=8080)