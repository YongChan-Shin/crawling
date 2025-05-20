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
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")



url = 'https://www.youtube.com/watch?v=zCrYPk6CL8k'
driver.get(url)

start = input('작업 시작(Enter 입력)')

videoEl = driver.find_element(By.TAG_NAME, 'video')
scriptEls = driver.find_elements(By.TAG_NAME, 'ytd-transcript-segment-renderer')

for idx, el in enumerate(scriptEls):
  try:
    el.click()
    videoEl.screenshot('./img/{}.png'.format(idx + 1))
    time.sleep(1)
  except:
    pass

time.sleep(10000000)
