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


## 시스템 아키텍쳐 다이어그램
![파이팀_캡디경진대회_전체설계 drawio](https://github.com/user-attachments/assets/97ac5a0f-84ff-4e29-9e43-e6409652f038)


## 하드웨어 구성 및 배선도
![RPI5_Architect](https://github.com/user-attachments/assets/e7356e29-da30-4520-84c1-75ed9462f67e)


## 페이지별 기능 설명
#### 1. 메인 페이지
접속시, 처음 보게되는 웹 사이트의 메인 페이지
![명지키움_PC대표](https://github.com/user-attachments/assets/302b85fb-8768-4f4e-b947-c6105669b264)
![명지키움_대표화면_편집](https://github.com/user-attachments/assets/d64c6b0e-c139-45f8-9bfe-ad31cc4310ab)
1. 식물의 실시간 상태를 확인할 수 있는 화면 제공. 해당 화면을 클릭하면, '2. 캠 확인'으로 이동할 수 있다.
2. 식물의 실사간 온도/조도/습도/수위를 측정해, 적정 수치인지 표기해준다.
3. 매일 매일 식물의 사진을 찍고 저장해놓은 '3. 일간 사진첩'으로 이동할 수 있다.

#### 2. 캠 확인
'1. 메인 페이지'에서 식물 이미지를 클릭해, 더 크고 자세하게 식물 이미지를  볼 수 있는 화면
<img width="960" alt="5  실시간 스트리밍" src="https://github.com/user-attachments/assets/3971b941-df90-47d3-b9da-cefcf770c685" />

#### 3. 일간 사진첩
'1. 메인 페이지'에서 '일간 사진첩' 버튼을 누르면 도착하는 화면. 자동 기록된 식물의 일간 사진을 살펴볼 수 있다.
또한, 원하는 날짜를 클릭해 해당 날짜 식물의 상태가 어땠는지 확인할 수 있는 '4. 일시별 식물 상태' 로 이동할 수 있다.
<img width="960" alt="6  앨범" src="https://github.com/user-attachments/assets/c16e61cf-0623-4c24-8eb6-a3191fd9a5b1" />

#### 4. 일시별 식물 상태
식물의 상태를 일정 시간을 간격으로 기록해 놓은 화면. 아래 예시 화면은 '3. 일간 사진첩'에서 '2024-06-13'을 클릭해 도달할 수 있다.
<img width="960" alt="7  일간상태표" src="https://github.com/user-attachments/assets/f3f49342-aa29-451f-a7f5-0b0ef64b8a52" />
