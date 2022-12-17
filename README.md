# 교내 캡스톤 졸업작품 최우수상 수상


----

> __'스마트 캐리어' 소스코드입니다.__

> __작동모습이나 설명이 포함된 동영상은 'capstone_ucc.mp4' 파일을 참조바랍니다.__


### 작동원리
-----

+ 1. 여행하면 빼놓을 수 없는 것이 캐리어이며, 낮선 곳으로 여행을 가는 것이니만큼 도난을 당하게 되면 여러모로 일이 복잡해지게 되므로 이러한 점에서 도난을 방지할 수 있는 스마트 캐리어 개발
+ 2. 내부 웹캠과 외부 웹캠을 동시에 설치하여 물품은 캐리어 내에 잘 보관되어 있는지, 혹시 누군가가 캐리어를 가지고 가지는 않는지 확인 가능하다. 카메라를 촬영시 내부는 어두울 수 있으므로 LED가 가동된다.
+ 3. 캐리어 내에 3축 가속도센서와 GPS 센서를 설치하여 캐리어가 일정 범위 이상의 움직임이 있는 경우 감지 가능. 또한 GPS 센서로 캐리어의 현 위치 파악 가능.
+ 4. Twilio라는 API를 이용하여 앱 내에 언제든지 사용자가 원할때 캐리어의 상태를 문자로 받아볼 수 있는 버튼이 존재함. 캐리어 내 센서를 이용해 현재 캐리어의 위치를 알 수도 있고, 누군가가 캐리어를 가져갈 경우 움직임이 감지되었다는 알림도 전송. 112에 바로 신고 가능한 신고버튼도 존재
> iv-1. 버튼을 눌렀을 경우 기준으로, gps가 조금이라도 잡히면 외부에 있는 걸로 간주, gps 수신정보를 문자로 보내며, gps가 잡히지 않을 경우 내부에 있는 것으로 간주, 3축 가속도센서를 이용해 움직임이 감지될 시 움직임이 감지되었다는 문자를 보냄.
+ 5. 파이썬과 쉘 프로그래밍을 이용하여 센서와 서버를 동작시켰으며,  crontab 기능을 이용하여 라즈베라파이에 전원이 들어오면 바로 시스템이 작동되도록 설정함.
+ 6. 안드로이드 앱의 경우 웹서버 측에서 디자인하고 구현하는 하이브리드 앱의 형태로 개발하였고, android studio와 flask 를 이용하였다.

### 작동화면 및 발표, 수상 사진

---

<img src="https://user-images.githubusercontent.com/85730066/170670134-a8ff4867-6d13-41ab-9301-3f515babba6c.jpg" width="500" height="1000">


<img src="https://user-images.githubusercontent.com/85730066/170671794-dccb5b39-c44c-48fb-8a0c-05a21fac7a69.jpg" width="500" height="700">


<img src="https://user-images.githubusercontent.com/85730066/171318191-674f19ca-3e15-4371-b530-8397c477eecb.jpg" width="500" height="500">


<img src="https://user-images.githubusercontent.com/85730066/171319669-dde49ee0-deff-40f3-87aa-b9fe005dc449.jpg" width="500" height="900">

