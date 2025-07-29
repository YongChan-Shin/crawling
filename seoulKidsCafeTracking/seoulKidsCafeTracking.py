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

driver.get("https://icare.seoul.go.kr")

input("로그인 후 작업 시작")

while True:
  
  try:
    driver.get("https://icare.seoul.go.kr/icare/user/kidsCafeResve/BD_selectKidsCafeResveCal.do?q_fcltyId=SB240702")
    driver.find_element(By.CLASS_NAME, 'agree_close').click()
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, 'next').click()
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, 'agree_close').click()
    time.sleep(3)
    
    firstTime = driver.find_element(By.CSS_SELECTOR, '#calendar > tbody > tr:nth-child(1) > td:nth-child(7) > div > p:nth-child(1) > span > i').text
    secondTime = driver.find_element(By.CSS_SELECTOR, '#calendar > tbody > tr:nth-child(1) > td:nth-child(7) > div > p:nth-child(2) > span > i').text
    thirdTime = driver.find_element(By.CSS_SELECTOR, '#calendar > tbody > tr:nth-child(1) > td:nth-child(7) > div > p:nth-child(3) > span > i').text
    firstTime2 = driver.find_element(By.CSS_SELECTOR, '#calendar > tbody > tr:nth-child(2) > td:nth-child(1) > div > p:nth-child(1) > span > i').text
    secondTime2 = driver.find_element(By.CSS_SELECTOR, '#calendar > tbody > tr:nth-child(2) > td:nth-child(1) > div > p:nth-child(2) > span > i').text
    thirdTime2 = driver.find_element(By.CSS_SELECTOR, '#calendar > tbody > tr:nth-child(2) > td:nth-child(1) > div > p:nth-child(3) > span > i').text

    print(firstTime)
    print(secondTime)
    print(thirdTime)
    print(firstTime2)
    print(secondTime2)
    print(thirdTime2)

    # if firstTime != '0' or firstTime2 != '0' or secondTime != '0' or secondTime2 != '0' or thirdTime != '0' or thirdTime2 != '0':
    if thirdTime2 != '0':
      toaster.show_toast("CHECK!","SEOUL CHECK", icon_path=None, duration=1000, threaded=True)
      print("취소건 발생!(체크)")
    else:
      print("{}회차 탐색 중({})".format(idx, time.strftime("%Y-%m-%d %H:%M:%S")))  
          
    time.sleep(1)
    toaster.__init__()
    idx += 1
  except Exception as e:
    print(e)