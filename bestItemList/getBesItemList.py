from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# 브랜드 리스트
brandList = [
  '키즈꼬모',
  '밀리밤',
  '베베쥬',
  '압소바',
  'MLB키즈',
  '이랜드키즈',
  '바브키즈',
  '더사랑이',
  '인디고키즈',
  '모다아울렛',
  '휠라키즈',
  '다쿠',
  '버블트리',
  '래핑차일드',
  '코디아이',
  '스트옐',
  '오르시떼',
  '뉴에라키즈',
  '노스페이스키즈',
  '네파',
  '스파오키즈',
  '더데이걸',
  '더사랑이',
  '초코몽',
  '월튼키즈',
  '뽀송이',
  '로엠걸즈',
  '유솔',
  '베베드피노',
  '멜리코코',
  '삠뽀요',
  '나로',
  '젤리스푼',
  '젤리스튜디오',
  '코코비',
  '밀크마일',
  '베리메이',
  '스투키',
  '아디다스',
  '나이키키즈',
  '뉴발란스키즈',
  '탑텐키즈',
  '행텐틴즈',
  '행텐주니어',
  '알럽키즈',
  '에뜨와',
  'BAY-B',
  '아임제이',
  '폴햄키즈',
  '앙쥬봉봉',
  '모이몰른',
  '닥스',
  '닥스리틀',
  '케어베어',
  '헤이미니',
  '콩알키즈',
  '로토토베베',
  '아가방',
  '해피버스',
  '해피프린스',
  '유니프랜드',
  '팬콧키즈',
  '앤디애플',
  '디스커버리키즈',
  '아이라인키즈',
  '아이스샌드',
  '키스포',
  '로아앤제인',
  '블루독',
  '블루독베이비',
  '베네통키즈',
  '리틀밥독',
  '코코리따',
  '알로봇',
  '치크',
  '레노마키즈',
  '레베끌레',
  '몰리멜리',
  '밀크베이비',
  '컬럼비아키즈',
  '비버리힐스',
  '지오다노',
  '그림아이',
  '헤지스키즈',
  '토토헤로스',
  '키즈레시피',
  '더미누',
  '키키스토리',
  '올리반',
  '릴리푸리',
  '로로샤',
  '프롬쥬니',
  '베베코지',
  '두나세나',
  '삼소니',
  '밍크뮤',
  '블랙야크키즈',
  '라코스테키즈브랜드',
  '캉골키즈',
  '빈폴키즈',
  '지프키즈',
  '예일키즈',
  '코코하니',
  '무누',
  '빌리키즈',
  '내셔널지오그래픽키즈',
  '로아앤제인',
  '코튼클럽',
  '디즈니베이비',
  '테스트',
  '테스트',
  '테스트',
  '테스트',
  '테스트',
  '테스트',
  '테스트',
  '테스트',
]

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
  
print(gmarketBest)

with open('./지마켓베스트상품.txt', 'w') as f:
  for i in gmarketBest:
    f.write('{}\n'.format(i))

with open('./지마켓신규브랜드.txt', 'w') as f:
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
  
print(auctionBest)

with open('./옥션_베스트상품.txt', 'w') as f:
  for i in auctionBest:
    f.write('{}\n'.format(i))

with open('./옥션_신규브랜드.txt', 'w') as f:
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
  
print(boriboriBest)

with open('./보리보리_베스트상품.txt', 'w') as f:
  for i in boriboriBest:
    f.write('{}\n'.format(i))

with open('./보리보리_신규브랜드.txt', 'w') as f:
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
  
print(elevenStBest)

with open('./11번가_베스트상품.txt', 'w') as f:
  for i in elevenStBest:
    f.write('{}\n'.format(i))

with open('./11번가_신규브랜드.txt', 'w') as f:
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
  
print(smartStoreBest)

with open('./스마트스토어_베스트상품.txt', 'w') as f:
  for i in smartStoreBest:
    f.write('{}\n'.format(i))

with open('./스마트스토어_신규브랜드.txt', 'w') as f:
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
  
print(lotteOnBest)

with open('./롯데온_베스트상품.txt', 'w') as f:
  for i in lotteOnBest:
    f.write('{}\n'.format(i))

with open('./롯데온_신규브랜드.txt', 'w') as f:
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
  
print(kidikidiBest)

with open('./키디키디_베스트상품.txt', 'w') as f:
  for i in kidikidiBest:
    f.write('{}\n'.format(i))

with open('./키디키디_신규브랜드.txt', 'w') as f:
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
  
print(talkdealBest)

with open('./톡딜_베스트상품.txt', 'w') as f:
  for i in talkdealBest:
    f.write('{}\n'.format(i))

with open('./톡딜_신규브랜드.txt', 'w') as f:
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
  
print(ssgBest)

with open('./SSG_베스트상품.txt', 'w') as f:
  for i in ssgBest:
    f.write('{}\n'.format(i))

with open('./SSG_신규브랜드.txt', 'w') as f:
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
  
print(momQBest)

with open('./맘큐_베스트상품.txt', 'w') as f:
  for i in momQBest:
    f.write('{}\n'.format(i))

with open('./맘큐_신규브랜드.txt', 'w') as f:
  for i in unknownBrand:
    f.write('{}\n'.format(i))


    
time.sleep(10000000)