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

driver.get("https://www.campingkorea.or.kr/user/reservation/BD_reservation.do")

input("로그인 후 작업 시작")


while True:
  
  try:
    
    driver.get("https://www.campingkorea.or.kr/user/reservation/BD_reservation.do")
    # driver.implicitly_wait(60)
    time.sleep(2)

    daysEl = driver.find_elements(By.CLASS_NAME, 'gDay')
    
    for i in daysEl:
      dayEl = i.find_element(By.CLASS_NAME, 'day').find_element(By.CLASS_NAME, 'da').text
      if  dayEl == '19' or dayEl == '26':
        print("7월{}일".format(dayEl), i.find_element(By.CLASS_NAME, 'lst').find_element(By.TAG_NAME, 'span').text)
        
        if i.find_element(By.CLASS_NAME, 'lst').find_element(By.TAG_NAME, 'span').text != '예약마감':
          toaster.show_toast("7월 CHECK!","autoCamping CHECK", icon_path=None, duration=1000, threaded=True)
          print("7월{}일 / 취소건 발생!(체크)".format(dayEl))
        else:
          print("{}회차 탐색 중({})".format(idx, time.strftime("%Y-%m-%d %H:%M:%S")))
          
    driver.find_element(By.CLASS_NAME, 'next').click()
    # driver.implicitly_wait(60)
    time.sleep(2)
    
    daysEl = driver.find_elements(By.CLASS_NAME, 'gDay')
  
    for i in daysEl:
      dayEl = i.find_element(By.CLASS_NAME, 'day').find_element(By.CLASS_NAME, 'da').text
      if dayEl == '2' or dayEl == '9' or dayEl == '15' or dayEl == '16' or dayEl == '23' or dayEl == '30':
        print("8월{}일".format(dayEl), i.find_element(By.CLASS_NAME, 'lst').find_element(By.TAG_NAME, 'span').text)
        
        if i.find_element(By.CLASS_NAME, 'lst').find_element(By.TAG_NAME, 'span').text != '예약마감':
          toaster.show_toast("8월 CHECK!","autoCamping CHECK", icon_path=None, duration=1000, threaded=True)
          print("8월{}일 / 취소건 발생!(체크)".format(dayEl))
        else:
          print("{}회차 탐색 중({})".format(idx, time.strftime("%Y-%m-%d %H:%M:%S")))
    
    time.sleep(1)
    toaster.__init__()
    idx += 1
  except Exception as e:
    print(e)