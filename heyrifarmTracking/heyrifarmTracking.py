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

while True:
  
  try:
    driver.get("https://m.booking.naver.com/booking/12/bizes/265564/items/3176704?area=plt&lang=ko&startDateTime=2025-09-07T00%3A00%3A00%2B09%3A00&theme=place")
    time.sleep(2)
    status = driver.find_elements(By.CLASS_NAME, 'text')
    
    for i in status:
      print(i.text)
      if i.text != '매진':
        toaster.show_toast("CHECK!","HEYRI CHECK", icon_path=None, duration=1000, threaded=True)
        print("취소건 발생!(체크)")
      else:
        print("{}회차 탐색 중({})".format(idx, time.strftime("%Y-%m-%d %H:%M:%S")))  
      
    toaster.__init__()
    idx += 1
  except Exception as e:
    print(e)
    
  time.sleep(2)