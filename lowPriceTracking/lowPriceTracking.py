# from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import requests
import time
import datetime
from dotenv import load_dotenv
import os
import shutil
import json
import products
import priceData

load_dotenv()
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

while True:

  # 최저가 정보
  lowPriceData = {}

  for prd in products.products:
    try:
      driver.get('https://search.shopping.naver.com/search/all?query={}&sort=price_asc&fo=true'.format(prd))
      priceEl = driver.find_elements(By.CLASS_NAME, 'price_num__S2p_v')[0].text
      lowPriceData[prd] = priceEl
      thumbnailImg = driver.find_elements(By.CLASS_NAME, 'product_item__MDtDF')[0]
      thumbnailImg.screenshot('./thumbnails/{}.jpg'.format(prd.replace('키즈꼬모 ', '')))
      
      # 썸네일 이미지 복사
      from_thumbnail_path = './thumbnails/{}.jpg'.format(prd.replace('키즈꼬모 ', ''))
      to_thumbnail_path = 'D:/1.업무/10.기타자료/Development/kidscomo/public/img/lowPriceTracking/{}.jpg'.format(prd.replace('키즈꼬모 ', ''))
      shutil.copy(from_thumbnail_path, to_thumbnail_path)
      
      time.sleep(2)
    except Exception as e:
      print(e)
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
          'salePrice': priceData.priceData[key]['salePrice'],
          'dealPrice': priceData.priceData[key]['dealPrice'],
          'lowPrice': int(value.replace(',', '').replace('원', '')),
          'diffPrice': int(value.replace(',', '').replace('원', '')) - priceData.priceData[key]['dealPrice'],
      })
    except Exception as e:
      print(e)
    
  print(jsonData)
      
  with open('./trackingJSON/lowPriceTracking.json', 'w', encoding='UTF-8') as outfile:
    json.dump(jsonData, outfile, indent=2, ensure_ascii=False)

  # 트래킹 json 파일 복사
  from_jsonFile_path = './trackingJSON/lowPriceTracking.json'
  to_jsonFile_path = 'D:/1.업무/10.기타자료/Development/kidscomo/public/data/lowPriceTracking.json'
  shutil.copy(from_jsonFile_path, to_jsonFile_path)

  time.sleep(180)
