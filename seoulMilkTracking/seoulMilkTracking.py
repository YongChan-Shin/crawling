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
month = [1, 2, 3]

driver.get("https://tour.seoulmilk.co.kr/tour/visit_01.php?int_place=1")
driver.execute_script('document.title = "milk"')

time.sleep(3)

# # 체크박스 체크 처리
driver.execute_script('document.getElementById("check-1").setAttribute("checked", "check")')
driver.execute_script('document.getElementById("check-2").setAttribute("checked", "check")')
driver.execute_script('document.getElementById("check-3").setAttribute("checked", "check")')
driver.execute_script('document.getElementById("check-4").setAttribute("checked", "check")')
driver.execute_script('document.getElementById("check-5").setAttribute("checked", "check")')
driver.execute_script('document.getElementById("check-6").setAttribute("checked", "check")')
driver.execute_script('document.getElementById("check-7").setAttribute("checked", "check")')
driver.execute_script('document.getElementById("check-8").setAttribute("checked", "check")')
driver.execute_script('document.getElementById("check-9").setAttribute("checked", "check")')
driver.execute_script('document.getElementById("check-10").setAttribute("checked", "check")')
driver.execute_script('document.getElementById("check-12").setAttribute("checked", "check")')
driver.execute_script('document.getElementById("check-13").setAttribute("checked", "check")')
driver.execute_script('document.getElementById("check-14").setAttribute("checked", "check")')
driver.execute_script('document.getElementById("check-15").setAttribute("checked", "check")')

input("로그인 후 작업 시작")

while True:
  
  for i in month:
    
    checkedDate = []
    
    try:
      driver.get("https://tour.seoulmilk.co.kr/tour/visit_02.php?Txt_year=2026&Txt_month={}&Txt_day=1&int_place=1&int_group=1&int_gtype=1".format(i))
      driver.execute_script('document.title = "{}"'.format(i))
      
      time.sleep(5)
      
      spanEls = driver.find_elements(By.CSS_SELECTOR, 'span.txt')
      
      for txt in spanEls:
        if txt.text != '신청마감' and txt.text != "":
          print('{}월 / {}'.format(i,txt.text))
          checkedDate.append(1)
        else:
          pass

      if len(checkedDate) != 0:
        toaster = WindowsToaster('seoulMilk CHECK')
        newToast.text_fields = ['{}월 CHECK!'.format(i)]
        toaster.show_toast(newToast)
        print("{}월 취소건 발생!(체크)".format(i))
      else:
        print("{}회차 탐색 중({})".format(idx, time.strftime("%Y-%m-%d %H:%M:%S")))
        
      idx += 1
      
      time.sleep(1)
      
    except Exception as e:
      print(e)
      errCnt += 1
      print("errCnt : {}".format(errCnt))
      if errCnt >= 30:
        toaster = WindowsToaster('seoulMilk ERROR CHECK')
        newToast.text_fields = ['{}월 ERROR!'.format(i)]
        toaster.show_toast(newToast)
        print("{}월 에러 발생!(체크)".format(i))
        
      time.sleep(3)