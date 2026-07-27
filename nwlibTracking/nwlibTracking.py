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

turnCnt = 1
errCnt = 0
flag = False

while True:
    
  try:
    driver.get("https://nwllc.sen.go.kr/nwllc/intro/search/detail.do?vLoca=111022&vCtrl=5897434592&isbn=9791193904435&menu_idx=4")
    driver.execute_script('document.title = "nwlib"')

    time.sleep(2)

    try:
      target = driver.find_element(By.CLASS_NAME, 'loan_resve')
      flag = True
    except:
      pass

    if flag:
        toaster = WindowsToaster('nwlib CHECK')
        newToast.text_fields = ['nwlib CHECK!']
        toaster.show_toast(newToast)
        print("nwlib 예약 가능!(체크)")
        time.sleep(10000)
    else:
      print("{}회차 탐색 중({})".format(turnCnt, time.strftime("%Y-%m-%d %H:%M:%S")))
      
    turnCnt += 1

    time.sleep(1)
    
  except Exception as e:
    print(e)
    
    errCnt += 1
    print("errCnt : {}".format(errCnt))
    
    if errCnt >= 30:
      toaster = WindowsToaster('nwlib ERROR CHECK')
      newToast.text_fields = ['nwlib ERROR!']
      toaster.show_toast(newToast)
      print("nwlib 에러 발생!(체크)")
      
    time.sleep(5)