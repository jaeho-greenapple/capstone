# -*- coding: utf-8 -*-
"""
Created on Mon May 23 19:26:19 2022

@author: 이재호
"""

# coding: utf-8

# smbus 라이브러리 임포트
import smbus

# time 라이브러리 임포트
import time
import io
 
import pynmea2
import serial
 

# smbus 객체 인스턴스 생성
bus = smbus.SMBus(1)

from twilio.rest import Client

account_sid='ACf5245c20b049be1e29763df5d6389563'
auth_token='8e4cae83eaf081f23b935fa99b11497f'
client=Client(account_sid,auth_token)

ser = serial.Serial('/dev/ttyS0', 9600, timeout=5.0)
sio = io.TextIOWrapper(io.BufferedRWPair(ser, ser))

# IC 주소
address = 0x53

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


# 예외 처리
try:
    
    # IC 초기화
    init_ADXL345()

    # 무한 반복
    while 1:
        # 함수를 호출해서 데이터 얻음
        x_acc = measure_acc(x_adr)
        y_acc = measure_acc(y_adr)
        z_acc = measure_acc(z_adr)
        # 결과 표시
        #print ('X = %2.2f' % x_acc, '[g], Y = %2.2f' % y_acc, '[g], Z = %2.2f' % z_acc, '[g]')
        # 0.5초 대기
        
        c=-0.20<x_acc<0.30 or 0.00<y_acc<0.10 or 1.18<z_acc<1.28
        
        print ('X = %2.2f' % x_acc, '[g], Y = %2.2f' % y_acc, '[g], Z = %2.2f' % z_acc, '[g]')
        time.sleep(0.5)
        if not c:
            message=client.messages.create(
                        body="움직임이 감지되었습니다",
                        from_='+12765288586',
                        to='+8201056294406'
                         )
                    time.sleep(120)#2분마다 움직임 알림 문자
        else:
            continue