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

driver.get("https://fire.seoul.go.kr/gwangnaru/res_status")

input('ㅡㅡㅡ 작업 시작 ㅡㅡㅡ')

while True:
  
  try:
    
    driver.find_element(By.CLASS_NAME, 'mdi-calendar').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'body > div.v-overlay-container > div > div.v-overlay__content > div > div.calendar > table > tbody > tr:nth-child(1) > td:nth-child(7)').click()
    driver.find_element(By.CLASS_NAME, 'v-btn--elevated').click()
    time.sleep(1)
    firstTime0906 = int(driver.find_elements(By.TAG_NAME, 'td')[4].text)
    secondTime0906 = int(driver.find_elements(By.TAG_NAME, 'td')[9].text)
    thirdTime0906 = int(driver.find_elements(By.TAG_NAME, 'td')[14].text)
    time.sleep(1)
    
    driver.find_element(By.CLASS_NAME, 'mdi-calendar').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'body > div.v-overlay-container > div > div.v-overlay__content > div > div.calendar > table > tbody > tr:nth-child(3) > td:nth-child(7)').click()
    driver.find_element(By.CLASS_NAME, 'v-btn--elevated').click()
    time.sleep(1)
    firstTime0920 = int(driver.find_elements(By.TAG_NAME, 'td')[4].text)
    secondTime0920 = int(driver.find_elements(By.TAG_NAME, 'td')[9].text)
    thirdTime0920 = int(driver.find_elements(By.TAG_NAME, 'td')[14].text)
      
    print(firstTime0906)
    print(secondTime0906)
    print(thirdTime0906)
    print(firstTime0920)
    print(secondTime0920)
    print(thirdTime0920)
    
    if firstTime0906 >= 2 or secondTime0906 >= 2 or thirdTime0906 >= 2 or firstTime0920 >= 2 or secondTime0920 >= 2 or thirdTime0920 >= 2:
      toaster.show_toast("CHECK!","GWANGNARU CHECK", icon_path=None, duration=1000, threaded=True)
      print("취소건 발생!(체크)")
    else:
      print("{}회차 탐색 중({})".format(idx, time.strftime("%Y-%m-%d %H:%M:%S")))  
          
    time.sleep(1)
    toaster.__init__()
    idx += 1
    
    time.sleep(3)
    
  except Exception as e:
    print(e)