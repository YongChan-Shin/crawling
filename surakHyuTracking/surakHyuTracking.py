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

driver.get("https://www.foresttrip.go.kr")

input("로그인 후 작업 시작")

url_1 = "https://www.foresttrip.go.kr/rep/or/sssn/fcfsRsrvtSmplPssblGoodsDetls.do?_csrf=1b9d9c1a-2116-4c58-8479-123e2c0777a9&netfunnel_key=D408EB70D49E925251D07148DE4D0106D0334C7ACEE0DC3CD978FC460B01035BA6733153E2257C300EE3DB844A1E9027F9E6802FC91FCD0B78068CC783FEAAD91AFA79CD78E1B4FC1EBD6FCF917F7CB517B16F302204CFE4FA9F00BB5FFC9C520E707B625E9445A1E4ED461647D254A5322C312C302C30&srchInsttArcd=1&srchInsttId=ID02030129&srchRsrvtBgDt=20250802&srchRsrvtEdDt=20250803&srchStngNofpr=3&srchSthngCnt=1&srchWord=&srchUseDt=&houseCampSctin=&rsrvtPssblYn=N&rsrvtWtngSctin=01&srchHouseCharg=&srchCampCharg=&goodsClsscHouseCdArr=&goodsClsscCampCdArr=&srchInsttTpcd=&cmdogYn=N&bbqYn=N&dsprsYn=N&otsdWeterYn=N&wifiYn=N&snowPlaceYn=N&srchMyLtd=&srchMyLng=&srchDstnc=&gNowPage=1&srchGoodsId=&hmpgId=FRIP"

url_2 = "https://www.foresttrip.go.kr/rep/or/sssn/fcfsRsrvtSmplPssblGoodsDetls.do?_csrf=1b9d9c1a-2116-4c58-8479-123e2c0777a9&netfunnel_key=D408EB70D49E925251D07148DE4D0106D0334C7ACEE0DC3CD978FC460B01035BA6733153E2257C300EE3DB844A1E9027F9E6802FC91FCD0B78068CC783FEAAD91AFA79CD78E1B4FC1EBD6FCF917F7CB517B16F302204CFE4FA9F00BB5FFC9C520E707B625E9445A1E4ED461647D254A5322C312C302C30&srchInsttArcd=1&srchInsttId=ID02030129&srchRsrvtBgDt=20250823&srchRsrvtEdDt=20250824&srchStngNofpr=3&srchSthngCnt=1&srchWord=&srchUseDt=&houseCampSctin=&rsrvtPssblYn=N&rsrvtWtngSctin=01&srchHouseCharg=&srchCampCharg=&goodsClsscHouseCdArr=&goodsClsscCampCdArr=&srchInsttTpcd=&cmdogYn=N&bbqYn=N&dsprsYn=N&otsdWeterYn=N&wifiYn=N&snowPlaceYn=N&srchMyLtd=&srchMyLng=&srchDstnc=&gNowPage=1&srchGoodsId=&hmpgId=FRIP"

url_3 = "https://www.foresttrip.go.kr/rep/or/sssn/fcfsRsrvtSmplPssblGoodsDetls.do?_csrf=1b9d9c1a-2116-4c58-8479-123e2c0777a9&netfunnel_key=D408EB70D49E925251D07148DE4D0106D0334C7ACEE0DC3CD978FC460B01035BA6733153E2257C300EE3DB844A1E9027F9E6802FC91FCD0B78068CC783FEAAD91AFA79CD78E1B4FC1EBD6FCF917F7CB517B16F302204CFE4FA9F00BB5FFC9C520E707B625E9445A1E4ED461647D254A5322C312C302C30&srchInsttArcd=1&srchInsttId=ID02030129&srchRsrvtBgDt=20250830&srchRsrvtEdDt=20250831&srchStngNofpr=3&srchSthngCnt=1&srchWord=&srchUseDt=&houseCampSctin=&rsrvtPssblYn=N&rsrvtWtngSctin=01&srchHouseCharg=&srchCampCharg=&goodsClsscHouseCdArr=&goodsClsscCampCdArr=&srchInsttTpcd=&cmdogYn=N&bbqYn=N&dsprsYn=N&otsdWeterYn=N&wifiYn=N&snowPlaceYn=N&srchMyLtd=&srchMyLng=&srchDstnc=&gNowPage=1&srchGoodsId=&hmpgId=FRIP"

while True:
  
  try:
    time.sleep(2)
    
    driver.get(url_1)
    revDiv_1 = driver.find_elements(By.CLASS_NAME, 'goods_list_area')
    print(len(revDiv_1))
    
    time.sleep(1)
    
    driver.get(url_2)
    revDiv_2 = driver.find_elements(By.CLASS_NAME, 'goods_list_area')
    print(len(revDiv_2))
    
    driver.get(url_3)
    revDiv_3 = driver.find_elements(By.CLASS_NAME, 'goods_list_area')
    print(len(revDiv_3))

    if len(revDiv_1) > 0 or len(revDiv_2) or len(revDiv_3)> 0:
      toaster.show_toast("CHECK!","surakHyu CHECK", icon_path=None, duration=1000, threaded=True)
      print("취소건 발생!(체크)")
    else:
      print("{}회차 탐색 중({})".format(idx, time.strftime("%Y-%m-%d %H:%M:%S")))  
          
    time.sleep(1)
    toaster.__init__()
    idx += 1
  except Exception as e:
    print(e)