from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv

options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

url = 'https://youtubetranscript.com/?v=rrlfsORwMGI'
driver.get(url)

start = input('작업 시작(Enter 입력)')

markers = driver.find_elements(By.CLASS_NAME, 'youtube-marker')
for idx, el in enumerate(markers):
  el.click()
  driver.find_element(By.ID, 'player').screenshot('./img/{}.jpg'.format(idx))

time.sleep(10000000)