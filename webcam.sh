#!/bin/bash
DATE=$(date +"%Y-%m-%d-%H%M%S")
#DATE_EX=$("capstone_cctv")
#sudo sysctl -w vm.drop_caches=2 # 시스템 블록에 있는 캐시 삭제
sudo sysctl -w vm.drop_caches=3 # 페이지 캐시까지 모두 삭제
python3 /home/pi/Desktop/capstone/LED_bar_on.py
fswebcam -r 800x600 --no-banner /home/pi/Desktop/capstone/webpage/static/capstonecctv.png
python3 /home/pi/Desktop/capstone/LED_bar_off.py
