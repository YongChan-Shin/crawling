# from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os
from PIL import Image

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.instagram.com/")

# 로그인
inputID = driver.find_elements(By.TAG_NAME, 'input')[0]
inputID.send_keys(os.environ.get("INSTA_ID"))
time.sleep(3)
inputPW = driver.find_elements(By.TAG_NAME, 'input')[1]
inputPW.send_keys(os.environ.get('INSTA_PW'))
time.sleep(3)
inputPW.send_keys(Keys.ENTER)
time.sleep(5)

try:
  btn = driver.find_element(By.CLASS_NAME, 'x1yc6y37')
  btn.click()
except:
  time.sleep(5)
  btn = driver.find_element(By.CLASS_NAME, 'x1yc6y37')
  btn.click()

with open('./followIDs.txt') as f:
  lines = f.readlines()
  lines = [line.strip() for line in lines]
  
  for id in lines:
    try:
      url = "https://www.instagram.com/{}".format(id)
      driver.get(url)
      time.sleep(3)

      # 팔로워 수 추출
      followerCnt = driver.find_elements(By.CLASS_NAME, 'x1vvkbs')[2].text
      
      # 메인페이지 상단 이미지 저장 
      mainTag = driver.find_element(By.TAG_NAME, "main")
      mainTag.screenshot('1.jpg')

      # 메인페이지 중단 이미지 저장 
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      time.sleep(3)
      mainTag.screenshot('2.jpg')

      # 메인페이지 하단 이미지 저장 
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      time.sleep(3)
      mainTag.screenshot('3.jpg')

      # 추출이미지 통합 저장
      image1 = Image.open('1.jpg')
      image2 = Image.open('2.jpg')
      image3 = Image.open('3.jpg')

      new_image = Image.new('RGB', (image1.width, image1.height + image2.height + image3.height), color=(255, 255, 255))
      new_image.paste(image1, (0, 0))
      new_image.paste(image2, (0, image1.height))
      new_image.paste(image3, (0, image1.height + image2.height))

      new_image.save('./img/{}_{}.jpg'.format(id, followerCnt), 'JPEG', quality=100, subsampling=0)
      
      time.sleep(3)
      
      for i in range(1, 4):
        os.remove('./{}.jpg'.format(i))
        
    except Exception as e:
      print(e)

time.sleep(100000000)