# 🚇너낼역🚇

### 🖤서비스 소개 
지하철 좌석 실시간 정보 공유 웹 서비스
<img src="https://user-images.githubusercontent.com/81161750/187938375-e22d1cbf-6286-4ef9-b055-3128f50e05e3.png"  width="800" height="450"/>

**지하철 좌석 실시간 정보 공유 웹 서비스!😍** </br>
대중교통에서 매일 1시간 27분을 보내는 한국인, 언제까지 눈치 싸움으로 자리를 차지하실 건가요?😒</br>
이제 🚇너낼역🚇이 **지하철 실시간 좌석 정보**를 제공합니다!</br>

저희는 지하철 ‘좌석’ 현황 정보를 이용자들이 주도적으로 공유할 수 있는 서비스를 고안하였고, </br>
이는 지하철 이용에 있어 수동적이었던 승객들에게 **주도성을 양도**한다는 점에서 이전에는 존재하지 않았던 가치를 제공하는 전복적 서비스라고 볼 수 있습니다. </br>

유저들은 **유용한 지하철 좌석 실시간 정보 공유 경험**을 통해 **지하철 이용의 스트레스를 최소화** 할 것 입니다.👍 </br>
더불어 너낼역은 기존의 지하철 이용에서의 승객들의 스트레스와 갈등을 해결하는 커뮤니티를 조성한다는 점에서 새로운 서비스입니다. </br>

- 로그인&회원가입 페이지
<img src="https://user-images.githubusercontent.com/81161750/187946278-77ad2621-ae87-4a45-9c00-7b42b85e6e4c.png"  width="800" height="450"/>

- 지하철 호선과 열차 선택 페이지
<img src="https://user-images.githubusercontent.com/81161750/187946101-797b9745-6752-46d0-9f84-ca1587787ef8.png"  width="800" height="450"/>

- 좌석 선택 페이지
<img src="https://user-images.githubusercontent.com/81161750/187945960-3e70aa6c-c65b-4dde-9dc0-bf9cdf805dc7.png"  width="900" height="420"/>

- 마이페이지(eye 사용&충전 내역과 결제창)
<img src="https://user-images.githubusercontent.com/81161750/187946189-1ce851be-b2f9-4490-8304-26ee7b2721d2.png"  width="800" height="220"/>

[ 너낼역 기능 시연 영상 ](https://youtu.be/SMZjkCxMtDY)

### 🖤Contributors
| 이나경 | 임채영 |
| ---------- | ---------- |
| [@rinarina0429](https://github.com/rinarina0429) | [@cha2y0ung](https://github.com/cha2y0ung) |

### 🖤프로젝트 시작
```
...
```

### 🖤기술 스택
- Frontend : <img src="https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=React&logoColor=white"> <img src="https://img.shields.io/badge/Redux-764ABC?style=flat-square&logo=Redux&logoColor=white"> <img src="https://img.shields.io/badge/ReduxToolkit-764ABC?style=flat-square&logo=Redux&logoColor=white"> <img src="https://img.shields.io/badge/ReduxPersist-764ABC?style=flat-square&logo=Redux&logoColor=white"> <img src="https://img.shields.io/badge/styled_components-DB7093?style=flat-square&logo=styled-components&logoColor=white">  
- Package Manager : <img src="https://img.shields.io/badge/npm-CB3837?style=flat-square&logo=npm&logoColor=white">
- Code Formmater : <img src="https://img.shields.io/badge/Prettier-F7B93E?style=flat-square&logo=React&logoColor=white">
- Depoly : <img src="https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=Vercel&logoColor=white">

### 🖤라이브러리
```
...
```

### 🖤기능 구현
1. 로그인 유지 : redux-toolkit, redux-persist 사용
2. 로그인, 회원가입 : JWT 토큰 기반 인증 방식 

### 🖤파일 구조
📦CheerCharm  
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
