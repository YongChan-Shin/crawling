from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

baseUrl = 'http://office.safetykorea.kr/fileData/certInfo/'

with open('./kcNumbers.txt') as f:
  lines = f.readlines()
  lines = [line.strip() for line in lines]
  idx = 1
  
  for number in lines:
    try:
      driver.set_page_load_timeout(3)
      print(idx, number)
      driver.get('http://office.safetykorea.kr/fileData/certInfo/2025/03/{}_1.jpg'.format(number))
      print(driver.current_url)
      body = driver.find_element(By.TAG_NAME, 'body')
      body.screenshot('./img/{}.jpg'.format(number))
      idx += 1
      time.sleep(2)
    except:
      pass
    
time.sleep(100000000)