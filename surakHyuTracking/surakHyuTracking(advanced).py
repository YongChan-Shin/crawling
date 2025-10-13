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
month = 11

driver.get("https://www.foresttrip.go.kr/rep/or/sssn/monthRsrvtSmplStatus.do")
driver.execute_script('document.title = "{}"'.format(month))

input("로그인 후 작업 시작")

srchBtn = driver.find_element(By.ID, 'searchBtn')

while True:
  
  driver.execute_script('document.title = "{}"'.format(month))
  
  try:
    srchBtn.click() 
    time.sleep(3)

    spanEls = driver.find_elements(By.CLASS_NAME, 'apt_mark')
    
    checkList = []

    for i in spanEls:
      if i.text == '예' or i.text == '대' or i.text == '대1' or i.text == '대2' or i.text == '대3':
        checkList.append(i.text)
        
    print(len(checkList) - 2)
    
    if len(checkList) > 2:
        toaster.show_toast("{}월 CHECK!".format(month),"surakHyu CHECK", icon_path=None, duration=1000, threaded=True)
        print("{}월 취소건 발생!(체크)".format(month))
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
      toaster.show_toast("{}월 ERROR!".format(month),"ERROR CHECK", icon_path=None, duration=1000, threaded=True)
      print("{}월 에러 발생!(체크)".format(month))
      
    time.sleep(5)