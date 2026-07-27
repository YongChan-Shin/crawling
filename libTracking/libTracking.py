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

while True:
    
  try:
    driver.get("https://www.jungnanglib.seoul.kr/jnlib/menu/10134/program/30001/searchResultList.do?searchType=SIMPLE&searchKeyword=%28%EB%82%98%EC%9D%98+%EC%B2%AB+%EB%B2%88%EC%A7%B8%29+%EB%B6%80%EB%8F%99%EC%82%B0+%EA%B5%90%EA%B3%BC%EC%84%9C&recentKeywordSaveYn=Y&searchManageCodeArr=MA")
    driver.execute_script('document.title = "lib"')

    time.sleep(2)

    els = driver.find_elements(By.CLASS_NAME, 'bookBtn')

    for i in els:
      if i.text == '도서예약신청':
        toaster = WindowsToaster('lib CHECK')
        newToast.text_fields = ['lib CHECK!']
        toaster.show_toast(newToast)
        print("lib 예약 가능!(체크)")
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
      toaster = WindowsToaster('lib ERROR CHECK')
      newToast.text_fields = ['lib ERROR!']
      toaster.show_toast(newToast)
      print("lib 에러 발생!(체크)")
      
    time.sleep(5)