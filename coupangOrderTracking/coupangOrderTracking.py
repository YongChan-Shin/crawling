from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime
from dotenv import load_dotenv
import os

from win10toast import ToastNotifier
from random import randint

# 신규 발주건 발생 시 알림 호출 기본 세팅
def bubbleSort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break

    return array

toaster = ToastNotifier()
array = [randint(-3000, 3000) for i in range(3000)]

load_dotenv()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url_1 = os.environ.get("URL_1")
url_2 = os.environ.get("URL_2")


driver.get(os.environ.get("URL_1"))

# 로그인
inputID = driver.find_elements(By.TAG_NAME, 'input')[0]
inputID.send_keys(os.environ.get("ID"))
time.sleep(3)
inputPW = driver.find_elements(By.TAG_NAME, 'input')[1]
inputPW.send_keys(os.environ.get('PW'))
time.sleep(3)
inputPW.send_keys(Keys.ENTER)
time.sleep(5)

idx = 1

while True:
  
  print("idx : {} / {}".format(idx, time.strftime("%Y-%m-%d %H:%M:%S"))) 
  
# 발주리스트 페이지 이동
  driver.get(os.environ.get("URL_2"))
  time.sleep(2)

  # 최근 발주리스트 추출
  recentOrderNum = []
  # orderTable = driver.find_element(By.CLASS_NAME, 'scmTableArea')
  # recentOrderList = orderTable.find_elements(By.TAG_NAME, 'a')
  
  recentOrderList = driver.find_elements(By.CSS_SELECTOR, '#app > div.contentsArea > div.scmContentsArea > div.scmTableArea > table > tbody > tr > td:nth-child(2) > a:nth-child(1)')

  for el in recentOrderList:
    data = el.text
    recentOrderNum.append(data)
      
  with open('./confirmList.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    
    for num in recentOrderNum:
      if num not in lines:
        toaster.show_toast("쿠팡 신규 발주건 발생!","발주리스트 확인 요망", icon_path=None, duration=1000, threaded=True)
        with open('쿠팡 신규 발주건({}).txt'.format(datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')), 'a') as f:
          f.write('{}\n'.format(num))
        print('(신규 발주건 발생) 발주번호 : {}'.format(num))
        
  time.sleep(300)
  toaster.__init__()
  idx += 1