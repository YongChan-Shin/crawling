from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime
import json
import shutil
import brandList

# 브랜드 리스트
brandList = brandList.brandList

while True:
  
  options = webdriver.ChromeOptions()
  options.add_argument('headless')
  options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정

  # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
  
  
  # 채널별 상품 베스트상품 리스트
  gmarketBest = []
  auctionBest = []
  boriboriBest = []
  elevenStBest = []
  smartStoreBest = []
  lotteOnBest = []
  kidikidiBest = []
  talkdealBest = []
  ssgBest = []
  momQBest = []

  # 미매칭 브랜드
  unknownBrand = []


  # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 지마켓 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

  url = 'https://www.gmarket.co.kr/n/best?groupCode=100000007&subGroupCode=200006003'
  driver.get(url)
  time.sleep(1)

  items = driver.find_element(By.CLASS_NAME, 'list__best').find_elements(By.CLASS_NAME, 'list-item')

  for idx, item in enumerate(items):
    try:
      itemTitle = item.find_element(By.CLASS_NAME, 'box__item-title').text.replace(' ', '')
      for idx, brand in enumerate(brandList):
        if itemTitle.find(brand) != -1:
          gmarketBest.append(brandList[idx])
    except:
      pass
    
  for idx, item in enumerate(items):
    searchCnt = 0
    try:
      itemTitle = item.find_element(By.CLASS_NAME, 'box__item-title').text.replace(' ', '')
      for brand in brandList:
        if itemTitle.find(brand) != -1:
          searchCnt += 1
      if searchCnt == 0:
        unknownBrand.append(itemTitle)
    except:
      pass  
  
  if '키즈꼬모' in gmarketBest:
    gmarketRating = gmarketBest.index('키즈꼬모') + 1
  else:
    gmarketRating = '-'
  
  print('ㅡㅡㅡㅡㅡ 지마켓 ㅡㅡㅡㅡㅡ')
  print(gmarketBest[:20])

  with open('./extractedInfo/지마켓베스트상품.txt', 'w') as f:
    for i in gmarketBest:
      f.write('{}\n'.format(i))

  with open('./extractedInfo/지마켓신규브랜드.txt', 'w') as f:
    for i in unknownBrand:
      f.write('{}\n'.format(i))


  # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 옥션 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

  url = 'https://corners.auction.co.kr/corner/categorybest.aspx?catetab=5&category=32000000'
  driver.get(url)
  time.sleep(1)

  items = driver.find_elements(By.CLASS_NAME, 'text__item-title')

  for idx, item in enumerate(items):
    try:
      itemTitle = item.find_element(By.TAG_NAME, 'a').text.replace(' ', '')
      for idx, brand in enumerate(brandList):
        if itemTitle.find(brand) != -1:
          auctionBest.append(brandList[idx])
    except:
      pass
    
  for idx, item in enumerate(items):
    searchCnt = 0
    try:
      itemTitle = item.find_element(By.TAG_NAME, 'a').text.replace(' ', '')
      for brand in brandList:
        if itemTitle.find(brand) != -1:
          searchCnt += 1
      if searchCnt == 0:
        unknownBrand.append(itemTitle)
    except:
      pass  
    
  if '키즈꼬모' in auctionBest:
    auctionRating = auctionBest.index('키즈꼬모') + 1
  else:
    auctionRating = '-'
  
  print('ㅡㅡㅡㅡㅡ 옥션 ㅡㅡㅡㅡㅡ')
  print(auctionBest)

  with open('./extractedInfo/옥션_베스트상품.txt', 'w') as f:
    for i in auctionBest:
      f.write('{}\n'.format(i))

  with open('./extractedInfo/옥션_신규브랜드.txt', 'w') as f:
    for i in unknownBrand:
      f.write('{}\n'.format(i))



  # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 보리보리 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

  url = 'https://m.boribori.co.kr/home/best/product'
  driver.get(url)
  time.sleep(1)

  items = driver.find_elements(By.CLASS_NAME, 'product__brand')

  for idx, item in enumerate(items):
    try:
      itemTitle = item.text.replace(' ', '')
      for idx, brand in enumerate(brandList):
        if itemTitle.find(brand) != -1:
          boriboriBest.append(brandList[idx])
    except:
      pass
    
  for idx, item in enumerate(items):
    searchCnt = 0
    try:
      itemTitle = item.text.replace(' ', '')
      for brand in brandList:
        if itemTitle.find(brand) != -1:
          searchCnt += 1
      if searchCnt == 0:
        unknownBrand.append(itemTitle)
    except:
      pass  

  if '키즈꼬모' in boriboriBest:
    boriboriRating = boriboriBest.index('키즈꼬모') + 1
  else:
    boriboriRating = '-'
  
  print('ㅡㅡㅡㅡㅡ 보리보리 ㅡㅡㅡㅡㅡ')
  print(boriboriBest)

  with open('./extractedInfo/보리보리_베스트상품.txt', 'w') as f:
    for i in boriboriBest:
      f.write('{}\n'.format(i))

  with open('./extractedInfo/보리보리_신규브랜드.txt', 'w') as f:
    for i in unknownBrand:
      f.write('{}\n'.format(i))



  # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 11번가 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

  url = 'https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=9&dispCtgrNo=1001356'
  driver.get(url)
  time.sleep(1)

  scrollTarget = driver.find_element(By.TAG_NAME, 'body')
  for i in range(3):
    scrollTarget.send_keys(Keys.END)
    time.sleep(1)

  items = driver.find_element(By.ID, 'bestPrdList').find_elements(By.CLASS_NAME, 'pname')

  for idx, item in enumerate(items):
    try:
      itemTitle = item.find_element(By.TAG_NAME, 'p').text.replace(' ', '')
      print(itemTitle)
      for idx, brand in enumerate(brandList):
        if itemTitle.find(brand) != -1:
          elevenStBest.append(brandList[idx])
    except:
      pass
    
  for idx, item in enumerate(items):
    searchCnt = 0
    try:
      itemTitle = item.find_element(By.TAG_NAME, 'p').text.replace(' ', '')
      for brand in brandList:
        if itemTitle.find(brand) != -1:
          searchCnt += 1
      if searchCnt == 0:
        unknownBrand.append(itemTitle)
    except:
      pass
    
  if '키즈꼬모' in elevenStBest:
    elevenStRating = elevenStBest.index('키즈꼬모') + 1
  else:
    elevenStRating = '-'

  print('ㅡㅡㅡㅡㅡ 11번가 ㅡㅡㅡㅡㅡ')
  print(elevenStBest)

  with open('./extractedInfo/11번가_베스트상품.txt', 'w') as f:
    for i in elevenStBest:
      f.write('{}\n'.format(i))

  with open('./extractedInfo/11번가_신규브랜드.txt', 'w') as f:
    for i in unknownBrand:
      f.write('{}\n'.format(i))


  # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 스마트스토어 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

  url = 'https://snxbest.naver.com/product/best/click?categoryId=50000138&sortType=PRODUCT_CLICK&periodType=DAILY&ageType=ALL'
  driver.get(url)
  time.sleep(1)

  items = driver.find_elements(By.CLASS_NAME, 'productCardResponsive_store__GaHMN')

  for idx, item in enumerate(items):
    try:
      itemTitle = item.text.replace(' ', '')
      for idx, brand in enumerate(brandList):
        if itemTitle.find(brand) != -1:
          smartStoreBest.append(brandList[idx])
    except:
      pass
    
  for idx, item in enumerate(items):
    searchCnt = 0
    try:
      itemTitle = item.text.replace(' ', '')
      for brand in brandList:
        if itemTitle.find(brand) != -1:
          searchCnt += 1
      if searchCnt == 0:
        unknownBrand.append(itemTitle)
    except:
      pass  

  if '키즈꼬모' in smartStoreBest:
    smartStoreRating = smartStoreBest.index('키즈꼬모') + 1
  else:
    smartStoreRating = '-'

  print('ㅡㅡㅡㅡㅡ 스마트스토어 ㅡㅡㅡㅡㅡ')
  print(smartStoreBest)

  with open('./extractedInfo/스마트스토어_베스트상품.txt', 'w') as f:
    for i in smartStoreBest:
      f.write('{}\n'.format(i))

  with open('./extractedInfo/스마트스토어_신규브랜드.txt', 'w') as f:
    for i in unknownBrand:
      f.write('{}\n'.format(i))
      
      

  # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 롯데온 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

  url = 'https://www.lotteon.com/p/display/shop/seltDpShop/29675?callType=menu'
  driver.get(url)
  catBtn1 = driver.find_elements(By.CLASS_NAME, 'srchCategoryName')[7]
  catBtn1.click()
  time.sleep(1)
  catBtn2 = driver.find_elements(By.CLASS_NAME, 's-best-middle-category__button')[1]
  catBtn2.click()
  time.sleep(1)

  items = driver.find_elements(By.CLASS_NAME, 's-goods-title__brand')

  for idx, item in enumerate(items):
    try:
      itemTitle = item.text.replace(' ', '')
      for idx, brand in enumerate(brandList):
        if itemTitle.find(brand) != -1:
          lotteOnBest.append(brandList[idx])
    except:
      pass
    
  for idx, item in enumerate(items):
    searchCnt = 0
    try:
      itemTitle = item.text.replace(' ', '')
      for brand in brandList:
        if itemTitle.find(brand) != -1:
          searchCnt += 1
      if searchCnt == 0:
        unknownBrand.append(itemTitle)
    except:
      pass  

  if '키즈꼬모' in lotteOnBest:
    lotteOnRating = lotteOnBest.index('키즈꼬모') + 1
  else:
    lotteOnRating = '-'

  print('ㅡㅡㅡㅡㅡ 롯데온 ㅡㅡㅡㅡㅡ')
  print(lotteOnBest)

  with open('./extractedInfo/롯데온_베스트상품.txt', 'w') as f:
    for i in lotteOnBest:
      f.write('{}\n'.format(i))

  with open('./extractedInfo/롯데온_신규브랜드.txt', 'w') as f:
    for i in unknownBrand:
      f.write('{}\n'.format(i))
      

  # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 키디키디 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

  url = 'https://kidikidi.elandmall.co.kr/u/rank?pageId=1737450657619&preCornerNo=R11300001_gnbMenu'
  driver.get(url)
  time.sleep(1)

  items = driver.find_elements(By.CLASS_NAME, 'brand')

  for idx, item in enumerate(items):
    try:
      itemTitle = item.text.replace(' ', '')
      for idx, brand in enumerate(brandList):
        if itemTitle.find(brand) != -1:
          kidikidiBest.append(brandList[idx])
    except:
      pass
    
  for idx, item in enumerate(items):
    searchCnt = 0
    try:
      itemTitle = item.text.replace(' ', '')
      for brand in brandList:
        if itemTitle.find(brand) != -1:
          searchCnt += 1
      if searchCnt == 0:
        unknownBrand.append(itemTitle)
    except:
      pass  

  if '키즈꼬모' in kidikidiBest:
    kidikidiRating = kidikidiBest.index('키즈꼬모') + 1
  else:
    kidikidiRating = '-'

  print('ㅡㅡㅡㅡㅡ 키디키디 ㅡㅡㅡㅡㅡ')
  print(kidikidiBest)

  with open('./extractedInfo/키디키디_베스트상품.txt', 'w') as f:
    for i in kidikidiBest:
      f.write('{}\n'.format(i))

  with open('./extractedInfo/키디키디_신규브랜드.txt', 'w') as f:
    for i in unknownBrand:
      f.write('{}\n'.format(i))


  # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 톡딜 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

  url = 'https://store.kakao.com/home/best?tab=contProduct&groupId=6&period=HOURLY'
  driver.get(url)
  time.sleep(1)
  for i in range(5):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(1)

  items = driver.find_elements(By.CLASS_NAME, 'tit_store')

  for idx, item in enumerate(items):
    try:
      itemTitle = item.text.replace(' ', '')
      for idx, brand in enumerate(brandList):
        if itemTitle.find(brand) != -1:
          talkdealBest.append(brandList[idx])
    except:
      pass
    
  for idx, item in enumerate(items):
    searchCnt = 0
    try:
      itemTitle = item.text.replace(' ', '')
      for brand in brandList:
        if itemTitle.find(brand) != -1:
          searchCnt += 1
      if searchCnt == 0:
        unknownBrand.append(itemTitle)
    except:
      pass  

  if '키즈꼬모' in talkdealBest:
    talkdealRating = talkdealBest.index('키즈꼬모') + 1
  else:
    talkdealRating = '-'

  print('ㅡㅡㅡㅡㅡ 톡딜 ㅡㅡㅡㅡㅡ')
  print(talkdealBest)

  with open('./extractedInfo/톡딜_베스트상품.txt', 'w') as f:
    for i in talkdealBest:
      f.write('{}\n'.format(i))

  with open('./extractedInfo/톡딜_신규브랜드.txt', 'w') as f:
    for i in unknownBrand:
      f.write('{}\n'.format(i))


  # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ SSG ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

  url = 'https://www.ssg.com/page/pc/ranking.ssg'
  driver.get(url)
  time.sleep(1)

  driver.find_element(By.ID, 'tabs-:R36ljakl8nj6:--tab-8').click()
  time.sleep(1)

  for i in range(5):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
    time.sleep(1)

  items = driver.find_elements(By.CLASS_NAME, 'css-f8xjfi')

  for idx, item in enumerate(items):
    try:
      itemTitle = item.text.replace(' ', '')
      for idx, brand in enumerate(brandList):
        if itemTitle.find(brand) != -1:
          ssgBest.append(brandList[idx])
    except:
      pass
    
  for idx, item in enumerate(items):
    searchCnt = 0
    try:
      itemTitle = item.text.replace(' ', '')
      for brand in brandList:
        if itemTitle.find(brand) != -1:
          searchCnt += 1
      if searchCnt == 0:
        unknownBrand.append(itemTitle)
    except:
      pass

  if '키즈꼬모' in ssgBest:
    ssgRating = ssgBest.index('키즈꼬모') + 1
  else:
    ssgRating = '-'

  print('ㅡㅡㅡㅡㅡ ssg ㅡㅡㅡㅡㅡ')
  print(ssgBest)

  with open('./extractedInfo/SSG_베스트상품.txt', 'w') as f:
    for i in ssgBest:
      f.write('{}\n'.format(i))

  with open('./extractedInfo/SSG_신규브랜드.txt', 'w') as f:
    for i in unknownBrand:
      f.write('{}\n'.format(i))


  # ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ 맘큐 ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

  url = 'https://www.momq.co.kr/shop/best_list.html?page_type=sale_list&type=&xcode=053'
  driver.get(url)
  time.sleep(1)

  items = driver.find_elements(By.CLASS_NAME, 'prd-name')

  for idx, item in enumerate(items):
    try:
      itemTitle = item.text.replace(' ', '')
      for idx, brand in enumerate(brandList):
        if itemTitle.find(brand) != -1:
          momQBest.append(brandList[idx])
    except:
      pass
    
  for idx, item in enumerate(items):
    searchCnt = 0
    try:
      itemTitle = item.text.replace(' ', '')
      for brand in brandList:
        if itemTitle.find(brand) != -1:
          searchCnt += 1
      if searchCnt == 0:
        unknownBrand.append(itemTitle)
    except:
      pass  

  if '키즈꼬모' in momQBest:
    momQRating = momQBest.index('키즈꼬모') + 1
  else:
    momQRating = '-'
  print('ㅡㅡㅡㅡㅡ 맘큐 ㅡㅡㅡㅡㅡ')
  print(momQBest)

  with open('./extractedInfo/맘큐_베스트상품.txt', 'w') as f:
    for i in momQBest:
      f.write('{}\n'.format(i))

  with open('./extractedInfo/맘큐_신규브랜드.txt', 'w') as f:
    for i in unknownBrand:
      f.write('{}\n'.format(i))

  # JSON 파일로 저장
  jsonData = {}
  jsonData['checkTime'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  jsonData['data'] = []

  jsonData['data'].append({
    'channel': '지마켓',
    'bestItems': gmarketBest[:20],
    'url': 'https://www.gmarket.co.kr/n/best?groupCode=100000007',
    'kidscomoRating': gmarketRating
    
  })

  jsonData['data'].append({
    'channel': '옥션',
    'bestItems': auctionBest[:20],
    'url': 'https://corners.auction.co.kr/corner/categorybest.aspx?catetab=5',
    'kidscomoRating': auctionRating
  })

  jsonData['data'].append({
    'channel': '보리보리',
    'bestItems': boriboriBest[:20],
    'url': 'https://m.boribori.co.kr/home/best/product?interval=24&dealYn=N',
    'kidscomoRating': boriboriRating
  })

  jsonData['data'].append({
    'channel': '11번가',
    'bestItems': elevenStBest[:20],
    'url': 'https://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&cornerNo=9&dispCtgrNo=1001356',
    'kidscomoRating': elevenStRating
  })

  jsonData['data'].append({
    'channel': '스마트스토어',
    'bestItems': smartStoreBest[:20],
    'kidscomoRating': smartStoreRating
  })

  jsonData['data'].append({
    'channel': '롯데온',
    'bestItems': lotteOnBest[:20],
    'url': 'https://www.lotteon.com/p/display/shop/seltDpShop/29675?callType=menu',
    'kidscomoRating': lotteOnRating
  })

  jsonData['data'].append({
    'channel': '키디키디',
    'bestItems': kidikidiBest[:20],
    'url': 'https://kidikidi.elandmall.co.kr/u/rank?pageId=1738568719924&preCornerNo=R11300001_gnbMenu',
    'kidscomoRating': kidikidiRating
  })

  jsonData['data'].append({
    'channel': '톡딜',
    'bestItems': talkdealBest[:20],
    'url': 'https://store.kakao.com/home/best?tab=contProduct&groupId=6&period=HOURLY',
    'kidscomoRating': talkdealRating
  })

  jsonData['data'].append({
    'channel': 'SSG',
    'bestItems': ssgBest[:20],
    'url': 'https://www.ssg.com/page/pc/ranking.ssg?trackingId=5000016039',
    'kidscomoRating': ssgRating
  })

  jsonData['data'].append({
    'channel': '맘큐',
    'bestItems': momQBest[:20],
    'url': 'https://www.momq.co.kr/shop/best_list.html?page_type=sale_list&type=&xcode=053',
    'kidscomoRating': momQRating
  })

  with open('./trackingJSON/bestItem.json', 'w', encoding='UTF-8') as outfile:
    json.dump(jsonData, outfile, indent=2, ensure_ascii=False)
    
  # 트래킹 json 파일 복사
  from_jsonFile_path = './trackingJSON/bestItem.json'
  to_jsonFile_path = 'D:/1.업무/10.기타자료/Development/kidscomo/public/data/bestItem.json'
  shutil.copy(from_jsonFile_path, to_jsonFile_path)    

  driver.quit()
  
  
  time.sleep(300)