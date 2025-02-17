# from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os

load_dotenv()

# options = ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.instagram.com/')
url = os.environ.get('URL')

# 로그인
inputID = driver.find_elements(By.TAG_NAME, 'input')[0]
inputID.send_keys(os.environ.get("INSTA_ID"))
time.sleep(3)
inputPW = driver.find_elements(By.TAG_NAME, 'input')[1]
inputPW.send_keys(os.environ.get('INSTA_PW'))
time.sleep(3)
inputPW.send_keys(Keys.ENTER)
time.sleep(5)

# 로그인 저장 안 함 선택
try:
  btn = driver.find_element(By.CLASS_NAME, 'x1yc6y37')
  btn.click()
except:
  try:
    time.sleep(5)
    btn = driver.find_element(By.CLASS_NAME, 'x1yc6y37')
    btn.click()
  except:
    pass

# 팔로우 목록 팝업 띄우기
time.sleep(3)
driver.get(url)
time.sleep(3)

# TODO 대상 목록 체크
# followBtn = driver.find_elements(By.CLASS_NAME, 'x1vvkbs')[4] # 팔로우 목록 띄우기
followBtn = driver.find_elements(By.CLASS_NAME, 'x1vvkbs')[3] # 팔로워 목록 띄우기

followBtn.click()
time.sleep(3)

# 팔로우 목록 스크롤
followListBox = driver.find_element(By.CLASS_NAME, 'xyi19xy')
for i in range(int(followBtn.text) // 8):
# for i in range(5):
  followListBox.send_keys(Keys.END)
  time.sleep(2)
  
# 팔로우 ID 정보 추출
followIDs = followListBox.find_elements(By.CLASS_NAME, '_aacx')

for i in followIDs:
  f = open('followIDs.txt', 'a')
  f.write('{}\n'.format(i.text))

time.sleep(100000000)