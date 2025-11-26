from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from win10toast import ToastNotifier
from random import randint

# 알림 호출 기본 세팅
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

options = webdriver.ChromeOptions()
# options.add_argument('headless')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

idx = 1
errCnt = 0
urlList = [
  'https://www.nowoncosmos.or.kr/payment_step1.html?cal=3562',
  'https://www.nowoncosmos.or.kr/payment_step1.html?cal=3563',
  'https://www.nowoncosmos.or.kr/payment_step1.html?cal=3564'
  ]
checkDate = ''

driver.get("https://www.nowoncosmos.or.kr/bbs/login.php")

input("로그인 후 작업 시작")

driver.execute_script('document.title = "nwAstro"')

while True:

  try:
    
    for arrIdx, url in enumerate(urlList):
      
      if arrIdx == 0:
        checkDate = '12/5(금)'
      elif arrIdx == 1:
        checkDate = '12/6(토)'
      else:
        checkDate = '12/13(토)'
        
      driver.get(url)
      
      driver.execute_script('document.title = "nwAstro"')
      
      time.sleep(1)
      num = int(driver.find_element(By.CSS_SELECTOR, '#time_table > tbody > tr.status > td:nth-child(3)').text.split('/')[0])
      num2 = int(driver.find_element(By.CSS_SELECTOR, '#time_table > tbody > tr.status > td:nth-child(4)').text.split('/')[0])
      print(checkDate)
      print(num)
      print(num2)
    
      if num <= 32 or num <= 32:
        toaster.show_toast("{} CHECK!".format(checkDate),"nwAstro CHECK", icon_path=None, duration=1000, threaded=True)
        print("{} 취소건 발생!(체크)".format(checkDate))
      else:
        print("{}회차 탐색 중({})".format(idx, time.strftime("%Y-%m-%d %H:%M:%S")))
        
      toaster.__init__()
      
      idx += 1
      
      time.sleep(1)
        
  except Exception as e:
    print(e)
    errCnt += 1
    print("errCnt : {}".format(errCnt))
    if errCnt >= 30:
      toaster.show_toast("ERROR!","ERROR CHECK", icon_path=None, duration=1000, threaded=True)
      print("에러 발생!(체크)")
      
  time.sleep(2)