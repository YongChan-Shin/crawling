from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://www.safetykorea.kr/release/itemSearch/')

kcNumbers = []

time.sleep(3)
itemMenu = driver.find_element(By.CLASS_NAME, 'left')
childCertMenu = itemMenu.find_element(By.CSS_SELECTOR, 'li:nth-last-child(1)')
childCertMenu.click()
time.sleep(3)
targetItemDiv = driver.find_element(By.CLASS_NAME, 'right')
targetItemUl = targetItemDiv.find_element(By.ID, 'right')
targetItemDivEl = targetItemUl.find_element(By.CSS_SELECTOR, 'li:nth-child(1) > a')
targetItemDivEl.click()
time.sleep(5)

for page in range(10):
  for i in range(10):
    try:
      number = driver.find_element(By.ID, "certNum_{}".format(i))
      kcNumbers.append(number.text)
    except:
      pass
    
  nextBtn = driver.find_element(By.CSS_SELECTOR, "div.page > ul > li:nth-last-child(2) > a")
  nextBtn.click()
  
  time.sleep(3)
  
for i in kcNumbers:
  f = open('kcNumbers.txt', 'a')
  f.write('{}\n'.format(i))

print(kcNumbers)

time.sleep(100000000)