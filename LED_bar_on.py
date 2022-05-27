# coding: utf-8

# GPIO 라이브러리 임포트
import RPi.GPIO as GPIO

# time 라이브러리 임포트
import time

# 핀 번호 할당 방법은 커넥터 핀 번호로 설정
GPIO.setmode(GPIO.BCM)

# 사용할 핀 번호 할당
LED = 27

# 11번 핀을 출력 핀으로 설정, 초기 출력은 로우 레벨
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)



# 하이 레벨 출력
GPIO.output(LED, GPIO.HIGH)


#time.sleep(3.0)