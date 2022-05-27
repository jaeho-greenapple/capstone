# coding: utf-8

# smbus 라이브러리 임포트
import smbus

# time 라이브러리 임포트
import time
import io
 
import pynmea2
import serial
from flask import Flask, render_template

from twilio.rest import Client

account_sid='ACf5245c20b049be1e29763df5d6389563'
auth_token='8e4cae83eaf081f23b935fa99b11497f'
client=Client(account_sid,auth_token)

# smbus 객체 인스턴스 생성
bus = smbus.SMBus(1)

ser = serial.Serial('/dev/ttyS0', 9600, timeout=5.0)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))
# IC 주소
address = 0x53
line = sio.readline() 
msg = pynmea2.parse(line)
# 각 축의 데이터 주소
x_adr = 0x32
y_adr = 0x34
z_adr = 0x36

# 센서 IC를 초기화하는 함수
def init_ADXL345():
    # POWER_CTL 레지스터(주소: 0x2D)의 Measure 비트에 1을 써서 계측 시작
    bus.write_byte_data(address, 0x2D, 0x08)

# IC에서 데이터를 얻는 함수
def measure_acc(adr):
    # 각 축의 측정값 하위 바이트를 읽기
    acc0 = bus.read_byte_data(address, adr)
    # 각 축의 측정값 상위 바이트를 읽기
    acc1 = bus.read_byte_data(address, adr + 1)

    # 수신한 2바이트 데이터를 10비트 데이터로 합치기
    acc = (acc1 << 8) + acc0
    # 부호가 있는지 (10비트째가 1인지) 판정
    if acc > 0x1FF:
        # 음수로 변환
        acc = (65536 - acc) * -1
    # 가속도 값으로 변환
    acc = acc * 3.9 / 1000
        # 결과 반환
    return acc


try:

    init_ADXL345()

    # 무한 반복
    while 1:
        global x_acc, y_acc, z_acc
        # 함수를 호출해서 데이터 얻음
        x_acc = measure_acc(x_adr)
        y_acc = measure_acc(y_adr)
        z_acc = measure_acc(z_adr)
        
        x_acc=round(x_acc,2)
        y_acc=round(y_acc,2)
        z_acc=round(z_acc,2)
        
        
        time.sleep(0.5)
        line = sio.readline()
        if (line[0:6] == "$GPGGA"):
            msg = pynmea2.parse(line)
            
            lat=msg.lat
            times=msg.timestamp
            lon=msg.lon
            
            app=Flask(__name__)

            @app.route('/')
            def webpage():
               return render_template('index.html',x=x_acc,y=y_acc,z=z_acc,lat_real=lat,lon_real=lon,time_real=times) # 자동으로 templates 폴더 안에 있는 파일을 클라이언트한테 갖다 준다.
            

            @app.route('/on')
            def sms_on():
                line = sio.readline()                   
                if (line[7] == ","): # gps가 잡히지 않았을때, 기울기 정보를 보낸다.
                    #msg = pynmea2.parse(line)
                    c=-0.10<x_acc<0.10 or -0.10<y_acc<0.10 or -1.15<z_acc<-0.90
                    if not c: # 일정 범위 이상으로 움직임이 감지되었을 경우
                        message=client.messages.create(
                            body="캐리어가 내부에 있습니다. \n하지만 캐리어에 움지임이 감지되었습니다.",
                            from_='+12765288586',
                            to='+8201056294406'
                            )
                        
                        #time.sleep(1800)#30분마다 한번씩 기울기 판정
                else: #gps가 잡혔을때
                    
                    message=client.messages.create(
                        body="위도:"+ str(msg.lat) +"경도:"+ str(msg.lon) +"\n 캐리어가 외부에 있습니다. \ngps 정보를 보내 드립니다.", #시간(-9h):"+ str(msg.timestamp) +"
                        from_='+12765288586',
                        to='+8201056294406'
                        )
                return render_template('complete_on.html')
                


        
            if __name__ == '__main__':
                app.run('192.168.197.72',port=7070,debug=False)
        
        
        else:
            continue
            

                


            
            

            
##############################################################
    

# 키보드에서 예외 검출
except KeyboardInterrupt:
    # 아무것도 하지 않음
    pass






