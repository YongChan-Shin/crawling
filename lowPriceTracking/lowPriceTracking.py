# from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime
from dotenv import load_dotenv
import os
import shutil
import json
import products
import priceData

def Crawling():
  
  load_dotenv()
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
  options = webdriver.ChromeOptions()
  options.add_argument('headless')
  options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
  
  errCnt = 0
  
  while True:

    # 최저가 정보
    lowPriceData = {}

    for idx, prd in enumerate(products.products):
      try:
        driver.get('https://search.shopping.naver.com/search/all?query={}&sort=price_asc&fo=true'.format(prd))
        priceEl = driver.find_elements(By.CLASS_NAME, 'price_num__S2p_v')[0].text
        lowPriceData[prd] = [priceEl]
        thumbnailImg = driver.find_elements(By.CLASS_NAME, 'product_item__MDtDF')[0]
        thumbnailImg.screenshot('./thumbnails/{}.jpg'.format(prd.replace('키즈꼬모 ', '')))
        
        # 썸네일 이미지 복사
        from_thumbnail_path = './thumbnails/{}.jpg'.format(prd.replace('키즈꼬모 ', ''))
        to_thumbnail_path = 'D:/1.업무/10.기타자료/Development/kidscomo/public/img/lowPriceTracking/{}.jpg'.format(prd.replace('키즈꼬모 ', ''))
        shutil.copy(from_thumbnail_path, to_thumbnail_path)
        
        time.sleep(2)
      except Exception as e:
        print('ㅡㅡㅡㅡㅡ (네이버 가격비교 조회 오류) {} / {} ㅡㅡㅡㅡㅡ'.format(idx, prd))
        print(e)
        continue
      
      # 쿠팡 판매가 크롤링
      try:
        driverCoupang = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        url = 'https://www.coupang.com/vp/products/{}'.format(priceData.priceData[prd.replace('키즈꼬모 ', '')]['coupangId'])
        driverCoupang.get(url)
        
        coupangPriceEl = driverCoupang.find_element(By.CLASS_NAME, 'total-price').find_element(By.TAG_NAME, 'strong').text.replace(',', '').replace('원', '')
        
        lowPriceData[prd].append(coupangPriceEl)
        print("{} / ({}) {} {}".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), idx+1, prd, lowPriceData[prd]))
        
        driverCoupang.quit()
        errCnt = 0
        time.sleep(25)
      except Exception as e:
        print('ㅡㅡㅡㅡㅡ (쿠팡 가격 조회 오류) {} ㅡㅡㅡㅡㅡ'.format(prd))
        print(e)
        errCnt += 1
        print('Error Cnt : {}'.format(errCnt))
        if errCnt > 10:
          driver.quit()
          time.sleep(1800)
          Crawling()
        continue
    
    # JSON 파일로 저장
    jsonData = {}
    jsonData['checkTime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    jsonData['data'] = []

    for key, value in lowPriceData.items():
      key = key.replace('키즈꼬모 ', '')
      try:
        jsonData['data'].append({
            'prdName': key,
            'season': priceData.priceData[key]['season'],
            'salePrice': priceData.priceData[key]['salePrice'],
            'dealPrice': priceData.priceData[key]['dealPrice'],
            'lowPrice': int(value[0].replace(',', '').replace('원', '')),
            'diffPrice': int(value[0].replace(',', '').replace('원', '')) - priceData.priceData[key]['dealPrice'],
        })
      except Exception as e:
        print(e)
      
      try:
        for item in jsonData['data']:
          if item['prdName'] == key:
            item['coupangPrice'] = int(value[1])
            item['coupangDiffPrice'] = int(value[1]) - priceData.priceData[key]['salePrice']
      except:
        try:
          for item in jsonData['data']:
            if item['prdName'] == key:
              item['coupangPrice'] = 0
              item['coupangDiffPrice'] = 0
        except:
          pass
      
    print(jsonData)
        
    with open('./trackingJSON/lowPriceTracking.json', 'w', encoding='UTF-8') as outfile:
      json.dump(jsonData, outfile, indent=2, ensure_ascii=False)

    # 트래킹 json 파일 복사
    from_jsonFile_path = './trackingJSON/lowPriceTracking.json'
    to_jsonFile_path = 'D:/1.업무/10.기타자료/Development/kidscomo/public/data/lowPriceTracking.json'
    shutil.copy(from_jsonFile_path, to_jsonFile_path)

    time.sleep(180)
    
Crawling()