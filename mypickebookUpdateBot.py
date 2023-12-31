import os
import schedule
import time
import telegram
import asyncio

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

async def send(str):
    token = '텔레그램 토큰을 입력해주세요'
    bot = telegram.Bot(token=token)
    await bot.send_message(-1002112802471, str)

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

service = ChromeService(executable_path=ChromeDriverManager().install())

# chrome driver
driver = webdriver.Chrome(service=service, options=options)  # <- options로 변경

def login():
    myID = "아이디를 입력해주세요"
    myPW = "비밀번호를 입력해주세요"
    url_login = "http://www.mypickebook.org/member/login.html"
    driver.get(url_login)
    driver.find_element(By.ID, 'login_id').send_keys(myID)
    driver.find_element(By.ID, 'login_pwd').send_keys(myPW)
    driver.find_element(By.CLASS_NAME, 'lgbtn').click()
    time.sleep(2)

    url = "http://www.mypickebook.org/mypage/book.html"
    driver.get(url)
    time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    lists = soup.select('#prjctList > tbody')

    table = driver.find_element(By.XPATH, "//*[@id='content']/div[4]/table/tbody")
    try:
        tr = table.find_elements(By.TAG_NAME, "tr")
        # for j in range(0, len(tr)):
        #     total_table.append(tr[j].text)
        latest = tr[0].text
    except:
        pass
    with open(os.path.join(BASE_DIR, 'latest.txt'), 'r') as f_read:
        before = f_read.readline()
        f_read.close()
        if before != latest:
            # bot.sendMessage(chat_id=chat_id, text='새 글이 올라왔어요!')
            asyncio.run(send("변경 사항을 발견했어요!"))
            asyncio.run(send(latest))
            with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
                f_write.write(latest)
                f_write.close()
    time.sleep(10)
    url_logout = "http://www.mypickebook.org/member/logout.html"
    driver.get(url_logout)

def main():
    #5분 주기로 갱신합니다.
    schedule.every(5).minutes.do(login)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()

