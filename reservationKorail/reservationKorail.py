from bs4 import BeautifulSoup
import requests
import time
from datetime import datetime

url = 'https://www.letskorail.com/ebizprd/EbizPrdTicketW_pr21190.do?hidOpener=Go&h_menu_id=11&h_run_dt=20240704&h_dpt_dt=20240704&h_trn_no=02551&h_dpt_rs_stn_cd=0104&h_arv_rs_stn_cd=0083&h_seat_att_cd=039&h_req_seat_cnt=3&hidTrain=G'

# url = 'http://127.0.0.1:5500/test.html'

while True:
  now = datetime.now()
  soup = BeautifulSoup(requests.get(url).content, 'html.parser')
  dates = soup.find_all('span', {'class', 'bookable'})
  
  if len(dates) > 0:
    for i in dates:
      print(i)
      f = open('log.txt', 'a', encoding='utf8')
      f.write(str(now.strftime('%Y-%m-%d %H:%M:%S')) + ' / ' + str(dates) + '\n')
      f.close()
      
  print(str(now.strftime('%Y-%m-%d %H:%M:%S')) + ' / ' + str(dates))
  
  
  # TODO 예약 가능 일자 있을 경우 텔레그램 메시지 발송 기능 추가
  
  time.sleep(10)