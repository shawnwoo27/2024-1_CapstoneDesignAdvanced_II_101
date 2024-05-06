
from flask import Flask, jsonify, render_template
import smbus2
import time
import board
import adafruit_dht

app = Flask(__name__)

# GPIO 핀 설정, DHT11
dht_device = adafruit_dht.DHT11(board.D4)

# IC2 버스 1을 사용
bus = smbus2.SMBus(1)

# BH1750 주소 (일반적으로 0x23, 모드에 따라 0x5C도 가능)
address = 0x23

# BH1750 측정 모드 설정
mode = 0x10

# BH1750 조도 계산식
def read_light(addr=address):
    data = bus.read_i2c_block_data(addr, mode, 2)
    light_level = (data[0] << 8 | data[1]) / 1.2
    return light_level


# 라우팅 설정
@app.route('/')
def main():
    return render_template('main.html')

@app.route('/cam-check')
def cam_check():
    return render_template('camCheck.html')

@app.route('/daily-photo')
def daily_photo():
    return render_template('DailyPhoto.html')

@app.route('/daily-plant-state')
def daily_plant_state():
    return render_template('DailyPlantState.html')

@app.route('/sensor_data')
def sensor_data():
    try:
        temperature = dht_device.temperature
        light = read_light()
        humidity = dht_device.humidity

        if humidity is not None and temperature is not None:
            return jsonify({
                'temperature': temperature,
                'light': light,
                'humidity': humidity
            })
        else:
            return jsonify({'error': 'Failed to retrieve data from sensor'}), 500

    except RuntimeError as error:
        return jsonify({'error': str(error)}), 500

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
