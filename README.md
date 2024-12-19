# 스마트 식물 모니터링 시스템

## 개발환경
#### 1. 하드웨어
+ Raspberry Pi 5: 프로젝트의 메인 서버 및 IoT 센서 데이터 수집 장치.
+ 각종 센서와 액츄에이터 및 모듈
  + 온습도 센서(DHT11)
  + 조도 센서(BH1750)
  + 수위 센서(SEN0204)
  + 모터 드라이버(L91100s)
  + 수중 펌프 모터(SZH-GNP155)
  + 라즈베리파이 카메라 모듈 V2, 8MP
    
#### 2. 소프트웨어
+ 운영체제: Raspberry Pi OS (Linux 기반, 64비트 버전)
+ 프로그래밍 언어: Python 3.11.2
+ 프레임워크 및 라이브러리:
  + Flask: 웹 서버 및 API 구축
  + Chart.js:데이터 시각화.
  + smbus: 시스템 레벨의 I2C 통신 기능
  + adafruit-circuitpython-dht: 온습도 센서용 라이브러리
+ 데이터베이스: MariaDB
+ 프론트엔드: HTML5/ CSS3/ JS

#### 3. 배포 환경
+ 서버: Raspberry Pi 5 자체를 로컬 서버로 활용.
+ 포트 포워딩: 라우터 설정을 통해 외부에서 Flask 서버 접근을 가능하게 함.
+ 도메인: DDNS (Dynamic DNS) 설정으로 외부 접속 가능.

## 시스템 아키텍쳐
![파이팀_캡디경진대회_전체설계 drawio](https://github.com/user-attachments/assets/97ac5a0f-84ff-4e29-9e43-e6409652f038)
![RPI5_Architect](https://github.com/user-attachments/assets/e7356e29-da30-4520-84c1-75ed9462f67e)
