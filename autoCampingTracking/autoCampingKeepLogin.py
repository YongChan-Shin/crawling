from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
# options.add_argument('headless')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

idx = 1

driver.get("https://www.campingkorea.or.kr/user/reservation/BD_reservation.do")

input("로그인 후 작업 시작")

while True:
  
  try:
    
    driver.get("https://www.campingkorea.or.kr/user/reservation/BD_reservation.do")
    
    time.sleep(60)


  except Exception as e:
    print(e)