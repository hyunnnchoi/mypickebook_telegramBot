# 실로암복지관 전자도서제작 봉사활동 변경 알림 봇
<img src="https://github.com/hyunnnchoi/mypickebook_telegramBot/assets/37583279/114bb797-e118-4479-89ff-6c6f25873e45"  height="800"/>


# Feature
- [실로암복지관 전자도서제작](https://velog.io/@haerong22/%ED%85%94%EB%A0%88%EA%B7%B8%EB%9E%A8-API-%EC%9D%B4%EC%9A%A9%ED%95%B4%EC%84%9C-%EB%A9%94%EC%8B%9C%EC%A7%80-%EC%A0%84%EC%86%A1%ED%95%98%EA%B8%B0)의 작업 변경내역을 텔레그램을 통해 알립니다.

# Requirements
- Python 3.9.13
- BeautifulSoup
- Selenium
- webdriver_manager
- telegram-python-bot

```shell
pip install bs4
pip install selenium
pip install webdriver_manager
pip install telegram-python-bot
```

# How it works
- 5분 단위로 로그인/로그아웃을 반복하며 데이터 수집을 진행합니다.
- 이전 내역과 변경사항이 있을 때, 알림 메시지를 보냅니다.

# How to use
- 놀고 있는 서버 혹은 노트북에, Requirements를 설치하고 코드를 실행해주세요!
  

# Telegram API 참고 자료
[텔레그램 API 이용해서 메시지 전송하기](https://velog.io/@haerong22/%ED%85%94%EB%A0%88%EA%B7%B8%EB%9E%A8-API-%EC%9D%B4%EC%9A%A9%ED%95%B4%EC%84%9C-%EB%A9%94%EC%8B%9C%EC%A7%80-%EC%A0%84%EC%86%A1%ED%95%98%EA%B8%B0)
