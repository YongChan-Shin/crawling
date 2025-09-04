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

url_1 = "https://www.foresttrip.go.kr/rep/or/sssn/fcfsRsrvtSmplPssblGoodsDetls.do?_csrf=1562c729-a43b-4c72-89e5-44733fcbf819&netfunnel_key=FE4B357A11F98F3365FFB6A104318966EE02449F578530B324BE9F1587DB802994535D25B2D0592A58AA3B685772A1AC3D4A64E2DB812769A75AA6A62B05F4C91AFA79CD78E1B4FC1EBD6FCF917F7CB580F63CEC080D0FCA7DB09F3C181742030E707B625E9445A1E4ED461647D254A5362C312C302C30&srchInsttArcd=1&srchInsttId=ID02030129&srchRsrvtBgDt=20250906&srchRsrvtEdDt=20250907&srchStngNofpr=3&srchSthngCnt=1&srchWord=&srchUseDt=&houseCampSctin=&rsrvtPssblYn=N&rsrvtWtngSctin=01&srchHouseCharg=&srchCampCharg=&goodsClsscHouseCdArr=&goodsClsscCampCdArr=&srchInsttTpcd=&cmdogYn=N&bbqYn=N&dsprsYn=N&otsdWeterYn=N&wifiYn=N&snowPlaceYn=N&srchMyLtd=&srchMyLng=&srchDstnc=&gNowPage=1&srchGoodsId=&hmpgId=FRIP"

url_2 = "https://www.foresttrip.go.kr/rep/or/sssn/fcfsRsrvtSmplPssblGoodsDetls.do?_csrf=1562c729-a43b-4c72-89e5-44733fcbf819&netfunnel_key=1935E36C515F0769A1797D1C411FF9515160D22FA8554CB41F85D5638364EEF0CD5804D89D520733A8CBF2861DE6ED0F6DD104B1B2F08EAC14AC4F7E43DEA27D1AFA79CD78E1B4FC1EBD6FCF917F7CB580F63CEC080D0FCA7DB09F3C181742030E707B625E9445A1E4ED461647D254A5332C312C302C30&srchInsttArcd=1&srchInsttId=ID02030129&srchRsrvtBgDt=20250913&srchRsrvtEdDt=20250914&srchStngNofpr=3&srchSthngCnt=1&srchWord=&srchUseDt=&houseCampSctin=&rsrvtPssblYn=N&rsrvtWtngSctin=01&srchHouseCharg=&srchCampCharg=&goodsClsscHouseCdArr=&goodsClsscCampCdArr=&srchInsttTpcd=&cmdogYn=N&bbqYn=N&dsprsYn=N&otsdWeterYn=N&wifiYn=N&snowPlaceYn=N&srchMyLtd=&srchMyLng=&srchDstnc=&gNowPage=1&srchGoodsId=&hmpgId=FRIP"

url_3 = "https://www.foresttrip.go.kr/rep/or/sssn/fcfsRsrvtSmplPssblGoodsDetls.do?_csrf=1562c729-a43b-4c72-89e5-44733fcbf819&netfunnel_key=858C030AF4A2B23AB9765E8E77C743F81E8E0F19EAFE302D7E0EDF32A663D68C6147945D2A50A0F89DF8F902E512753BDA60C5A1E53AAE647422A01EBECADD061AFA79CD78E1B4FC1EBD6FCF917F7CB580F63CEC080D0FCA7DB09F3C181742030E707B625E9445A1E4ED461647D254A5332C312C302C30&srchInsttArcd=1&srchInsttId=ID02030129&srchRsrvtBgDt=20250920&srchRsrvtEdDt=20250921&srchStngNofpr=3&srchSthngCnt=1&srchWord=&srchUseDt=&houseCampSctin=&rsrvtPssblYn=N&rsrvtWtngSctin=01&srchHouseCharg=&srchCampCharg=&goodsClsscHouseCdArr=&goodsClsscCampCdArr=&srchInsttTpcd=&cmdogYn=N&bbqYn=N&dsprsYn=N&otsdWeterYn=N&wifiYn=N&snowPlaceYn=N&srchMyLtd=&srchMyLng=&srchDstnc=&gNowPage=1&srchGoodsId=&hmpgId=FRIP"

url_4 = "https://www.foresttrip.go.kr/rep/or/sssn/fcfsRsrvtSmplPssblGoodsDetls.do?_csrf=1562c729-a43b-4c72-89e5-44733fcbf819&netfunnel_key=858C030AF4A2B23AB9765E8E77C743F81E8E0F19EAFE302D7E0EDF32A663D68C6147945D2A50A0F89DF8F902E512753BDA60C5A1E53AAE647422A01EBECADD061AFA79CD78E1B4FC1EBD6FCF917F7CB580F63CEC080D0FCA7DB09F3C181742030E707B625E9445A1E4ED461647D254A5332C312C302C30&srchInsttArcd=1&srchInsttId=ID02030129&srchRsrvtBgDt=20250927&srchRsrvtEdDt=20250928&srchStngNofpr=3&srchSthngCnt=1&srchWord=&srchUseDt=&houseCampSctin=&rsrvtPssblYn=N&rsrvtWtngSctin=01&srchHouseCharg=&srchCampCharg=&goodsClsscHouseCdArr=&goodsClsscCampCdArr=&srchInsttTpcd=&cmdogYn=N&bbqYn=N&dsprsYn=N&otsdWeterYn=N&wifiYn=N&snowPlaceYn=N&srchMyLtd=&srchMyLng=&srchDstnc=&gNowPage=1&srchGoodsId=&hmpgId=FRIP"

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
    time.sleep(1)
    
    driver.get(url_3)
    revDiv_3 = driver.find_elements(By.CLASS_NAME, 'goods_list_area')
    print(len(revDiv_3))
    time.sleep(1)
    
    driver.get(url_4)
    revDiv_4 = driver.find_elements(By.CLASS_NAME, 'goods_list_area')
    print(len(revDiv_4))
    time.sleep(1)

    if len(revDiv_1) > 0 or len(revDiv_2) > 0 or len(revDiv_3) > 0 or len(revDiv_4) > 0:
      toaster.show_toast("CHECK!","surakHyu CHECK", icon_path=None, duration=1000, threaded=True)
      print("취소건 발생!(체크)")
    else:
      print("{}회차 탐색 중({})".format(idx, time.strftime("%Y-%m-%d %H:%M:%S")))  
          
    time.sleep(1)
    toaster.__init__()
    
    idx += 1
  except Exception as e:
    print(e)