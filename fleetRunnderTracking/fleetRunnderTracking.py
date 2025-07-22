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

def crawling():
  driver.get("https://map.naver.com/p/entry/place/12217947?placePath=/ticket?entry=plt&from=map&fromPanelNum=1&additionalHeight=76&timestamp=202507221153&locale=ko&svcName=map_pcv5&from=map&fromPanelNum=1&additionalHeight=76&timestamp=202507221153&locale=ko&svcName=map_pcv5&searchType=place&lng=127.1148979&lat=37.5153818&c=15.00,0,0,0,dh")
  time.sleep(1)
  driver.switch_to.frame("entryIframe")
  driver.find_elements(By.CLASS_NAME, 'lsthu')[0].click()
  time.sleep(2)
  driver.find_element(By.CSS_SELECTOR, '#root > main > section.section_calendar > div > div.section_content > div.calendar_area > div > div > button.btn_next').click()

while True:
  
  try:
    
    crawling()
    
    time.sleep(2)
    
    dateTable = driver.find_element(By.CLASS_NAME, 'calendar_body')
    dateEls = dateTable.find_elements(By.TAG_NAME, 'button')
    
    for i in dateEls:
      numEl = i.find_element(By.CLASS_NAME,'num').text
      textEl = i.find_element(By.CLASS_NAME,'text').text
      
      print("8/{} : {}".format(numEl, textEl), end=' / ')
      
      if textEl != '휴무' and textEl != '마감':
        toaster.show_toast("CHECK!","fleetRunner CHECK", icon_path=None, duration=1000, threaded=True)
        print("취소건 발생!(체크)")
      else:
        print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡ {}회차 탐색 중({}) ㅡㅡㅡㅡㅡㅡㅡㅡㅡ".format(idx, time.strftime("%Y-%m-%d %H:%M:%S")))  
        
    toaster.__init__()
    idx += 1
    
  except Exception as e:
    print(e)