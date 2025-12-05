from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 윈도우 알림 세팅
from windows_toasts import Toast, WindowsToaster
newToast = Toast()

options = webdriver.ChromeOptions()
# options.add_argument('headless')
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

idx = 1
errCnt = 0
month = 12

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
        toaster = WindowsToaster('surakHyu CHECK')
        newToast.text_fields = ['{}월 CHECK!'.format(month)]
        toaster.show_toast(newToast)
        print("{}월 취소건 발생!(체크)".format(month))
    else:
      print("{}회차 탐색 중({})".format(idx, time.strftime("%Y-%m-%d %H:%M:%S")))
      
    
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