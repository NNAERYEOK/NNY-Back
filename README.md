# 🚇너낼역🚇

### 🖤서비스 소개 
지하철 좌석 실시간 정보 공유 웹 서비스
<img src="https://user-images.githubusercontent.com/81161750/187938375-e22d1cbf-6286-4ef9-b055-3128f50e05e3.png"  width="800" height="450"/>

**지하철 좌석 실시간 정보 공유 웹 서비스!😍**
대중교통에서 매일 1시간 27분을 보내는 한국인, 언제까지 눈치 싸움으로 자리를 차지하실 건가요?😒
이제 🚇너낼역🚇이 **지하철 실시간 좌석 정보**를 제공합니다!

저희는 지하철 ‘좌석’ 현황 정보를 이용자들이 주도적으로 공유할 수 있는 서비스를 고안하였고,
이는 지하철 이용에 있어 수동적이었던 승객들에게 **주도성을 양도**한다는 점에서 이전에는 존재하지 않았던 가치를 제공하는 전복적 서비스라고 볼 수 있습니다.

유저들은 **유용한 지하철 좌석 실시간 정보 공유 경험**을 통해 **지하철 이용의 스트레스를 최소화** 할 것 입니다.👍
더불어 너낼역은 기존의 지하철 이용에서의 승객들의 스트레스와 갈등을 해결하는 커뮤니티를 조성한다는 점에서 새로운 서비스입니다.

### 🖤기능 구현
- 로그인&회원가입 페이지 : JWT 토큰 기반 인증 방식 (로그인 유지 : redux-toolkit, redux-persist 사용)
<img src="https://user-images.githubusercontent.com/81161750/187946278-77ad2621-ae87-4a45-9c00-7b42b85e6e4c.png"  width="800" height="450"/>

- 지하철 호선과 열차 선택 페이지
<img src="https://user-images.githubusercontent.com/81161750/187946101-797b9745-6752-46d0-9f84-ca1587787ef8.png"  width="800" height="450"/>

- 좌석 선택 페이지
<img src="https://user-images.githubusercontent.com/81161750/187945960-3e70aa6c-c65b-4dde-9dc0-bf9cdf805dc7.png"  width="900" height="420"/>

- 마이페이지(eye 사용&충전 내역과 결제창)
<img src="https://user-images.githubusercontent.com/81161750/187946189-1ce851be-b2f9-4490-8304-26ee7b2721d2.png"  width="800" height="220"/>

[ 너낼역 기능 시연 영상 ](https://youtu.be/SMZjkCxMtDY)

### 🖤기술 스택
| <image src="https://user-images.githubusercontent.com/69039161/215253421-51587157-d431-42b6-9727-549054c5dc80.png" width=100> | <image src="https://user-images.githubusercontent.com/69039161/215253483-61e98ba8-e8bf-48f9-9035-11cd2718ea5e.png" width=100> | <image src="https://user-images.githubusercontent.com/69039161/215253535-0c29e1d3-c407-4102-abba-5b2be2954248.png" width=100> |
| ---------- | ---------- | ---------- |
| Django | AWS | github actions |

### 🖤프로젝트 시작
```
...
```

### 🖤라이브러리
```
...
```

### 🖤BACKEND Contributors
| 이나경 | 임채영 |
| ---------- | ---------- |
| [@rinarina0429](https://github.com/rinarina0429) | [@cha2y0ung](https://github.com/cha2y0ung) |

### 🖤파일 구조
<!--📦CheerCharm
 ┣ 📂.github  
 ┃ ┗ 📂workflows  
 ┃ ┃ ┗ 📜deploy.yml  
 ┣ 📂accounts  
 ┃ ┣ 📂migrations  
 ┃ ┣ 📜admin.py  
 ┃ ┣ 📜apps.py  
 ┃ ┣ 📜models.py  
 ┃ ┣ 📜serializers.py  
 ┃ ┣ 📜tests.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜views.py  
 ┃ ┗ 📜**init**.py  
 ┣ 📂charms  
 ┃ ┣ 📂migrations  
 ┃ ┣ 📜admin.py  
 ┃ ┣ 📜apps.py  
 ┃ ┣ 📜models.py  
 ┃ ┣ 📜serializers.py  
 ┃ ┣ 📜tests.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜views.py  
 ┃ ┗ 📜**init**.py  
 ┣ 📂CheerCharm  
 ┃ ┣ 📂settings  
 ┃ ┃ ┣ 📜base.py  
 ┃ ┃ ┣ 📜dev.py  
 ┃ ┃ ┣ 📜prod.py  
 ┃ ┃ ┗ 📜**init**.py  
 ┃ ┣ 📜asgi.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜wsgi.py  
 ┃ ┗ 📜**init**.py  
 ┣ 📂cheers  
 ┃ ┣ 📂migrations  
 ┃ ┣ 📜admin.py  
 ┃ ┣ 📜apps.py  
 ┃ ┣ 📜models.py  
 ┃ ┣ 📜serializers.py  
 ┃ ┣ 📜tests.py  
 ┃ ┣ 📜urls.py  
 ┃ ┣ 📜views.py  
 ┃ ┗ 📜**init**.py  
 ┣ 📂config  
 ┃ ┣ 📂docker  
 ┃ ┣ 📂nginx  
 ┃ ┗ 📂scripts  
 ┣ 📜.env.prod  
 ┣ 📜docker-compose.prod.yml  
 ┣ 📜Dockerfile.prod  
 ┣ 📜manage.py  
 ┣ 📜README.md  
 ┗ 📜requirements.txt
-->
<img src="https://github.com/NNAERYEOK/NNY-Back/assets/101031854/439391bb-e24f-4148-be08-be9483c36d26" width="50" height="50" align="right">
