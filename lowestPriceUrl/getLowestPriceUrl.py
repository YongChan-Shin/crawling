from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from openpyxl import load_workbook

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

wb = load_workbook('data.xlsx')
ws = wb.active

firstRow = 2
lastRow = ws.max_row + 1
idx = 1

for i in range(firstRow, lastRow):
  try:
    prd = '키즈꼬모 ' + ws.cell(i, 1).value
    print('{} / {}'.format(idx, prd))
    driver.get('https://search.shopping.naver.com/search/all?query={}&sort=price_asc&fo=true'.format(prd))
    time.sleep(1)
    ws.cell(i, 2).value = driver.current_url
    ws.cell(i, 3).value = ' '
    idx += 1
  except:
    pass
  
wb.save('data_네이버 최저가 URL 추출본.xlsx')