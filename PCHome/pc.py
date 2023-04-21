import os
import requests
import urllib.request as req
import json
import time
import random
import csv
import urllib
from urllib.parse import quote
import urllib3
import pandas as pd 
from crawler_proxy import get_IP

    

def get_data(total_page,data_urlname,data_name,IP='192.168.1.106'):
    sleep_time = 0
    for i in range(2,total_page+1):
        sleep_time += 1
        if sleep_time % 10 ==0 :
            time.sleep(random.randrange(10))
            url = f'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={data_urlname}&page={i}&sort=prc/ac'

            proxies = {'https': f'http://{IP}'}
            request = requests.get(url,headers={
                'cookie':'mid=WLsL4gAEAAGl0Wjoc8Dv6CH_iYnP; mcd=3; ds_user_id=1926542376; csrftoken=9aasLCq0vb2dUQWY9j1rjP11aejod1wS; sessionid=1926542376%3AG5zq9okSZhBxWx%3A8; ig_did=8675D711-4D34-4DBA-8751-F9E4E3B8FA63; shbid=17721; shbts=1602880097.7694821; rur=VLL; urlgen="{\"61.228.154.31\": 3462}:1kTWVn:7qfV2Cxf3rs1oZ9BUi45bNQ18T4',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            },proxies=proxies,verify=False)
            datas = request.json(request.text)
            datas = datas['prods']

            with open(f'./{data_name}.csv','a',encoding='utf-8-sig',newline="") as f:
                # 建立csv寫入器
                writer = csv.writer(f)
                writer.writerow([f'第{i}頁'])
                for data in datas:
                    # 寫入一列資料
                    writer.writerow([data['name'],data['price']])
        else:
            url = f'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={data_urlname}&page={i}&sort=prc/ac'
            proxies = {'https': f'http://{IP}'}
            request = requests.get(url,headers={
                'cookie':'mid=WLsL4gAEAAGl0Wjoc8Dv6CH_iYnP; mcd=3; ds_user_id=1926542376; csrftoken=9aasLCq0vb2dUQWY9j1rjP11aejod1wS; sessionid=1926542376%3AG5zq9okSZhBxWx%3A8; ig_did=8675D711-4D34-4DBA-8751-F9E4E3B8FA63; shbid=17721; shbts=1602880097.7694821; rur=VLL; urlgen="{\"61.228.154.31\": 3462}:1kTWVn:7qfV2Cxf3rs1oZ9BUi45bNQ18T4',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            },proxies=proxies,verify=False)
            datas = request.json()
            datas = datas['prods']

            with open(f'./{data_name}.csv','a',encoding='utf-8-sig',newline="") as f:
                # 建立csv寫入器
                writer = csv.writer(f)
                writer.writerow([f'第{i}頁'])
                for data in datas:
                    #計算當下獲取的時間
                    localtime = time.localtime() # 獲得當前時間
                    result = time.strftime("%Y-%m-%d %I:%M:%S %p", localtime)
                    # 寫入一列資料
                    writer.writerow([result,data['name'],data['price']])


def first_get_value(IP='192.168.1.106',data_name='尿布',page_number=1):

    # 進行 url 編碼
    data_urlname=quote(data_name,'utf-8')
    url=f'https://ecshweb.pchome.com.tw/search/v3.3/all/results?q={data_urlname}&page={page_number}&sort=prc/ac'


    # proxies = {"http":None,'https': f'http://{IP}'}

    # request = requests.get(url,headers={
    #     'cookie':'mid=WLsL4gAEAAGl0Wjoc8Dv6CH_iYnP; mcd=3; ds_user_id=1926542376; csrftoken=9aasLCq0vb2dUQWY9j1rjP11aejod1wS; sessionid=1926542376%3AG5zq9okSZhBxWx%3A8; ig_did=8675D711-4D34-4DBA-8751-F9E4E3B8FA63; shbid=17721; shbts=1602880097.7694821; rur=VLL; urlgen="{\"61.228.154.31\": 3462}:1kTWVn:7qfV2Cxf3rs1oZ9BUi45bNQ18T4',
    #     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    # },proxies=proxies,verify=False)
    
    request = requests.get(url,headers={
        'cookie':'mid=WLsL4gAEAAGl0Wjoc8Dv6CH_iYnP; mcd=3; ds_user_id=1926542376; csrftoken=9aasLCq0vb2dUQWY9j1rjP11aejod1wS; sessionid=1926542376%3AG5zq9okSZhBxWx%3A8; ig_did=8675D711-4D34-4DBA-8751-F9E4E3B8FA63; shbid=17721; shbts=1602880097.7694821; rur=VLL; urlgen="{\"61.228.154.31\": 3462}:1kTWVn:7qfV2Cxf3rs1oZ9BUi45bNQ18T4',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    },verify=False)

    # print(request.text)
    datas = json.loads(request.text)
    total_page = datas['totalPage']
    datas = datas['prods']

    with open(f'./{data_name}.csv','a',encoding='utf-8-sig',newline="") as f:
        # 建立csv寫入器
        writer = csv.writer(f)
        writer.writerow(['獲取時間','商品名稱','價錢'])
        try:
            for data in datas:
                # 寫入一列資料
                localtime = time.localtime()
                result = time.strftime("%Y-%m-%d %I:%M:%S %p", localtime)
                writer.writerow([result,data['name'],data['price']])
        except:
            return print(f"失敗第1頁")

    if total_page >1:
        get_data(total_page,data_urlname,data_name)


urllib3.disable_warnings()





IP_list = get_IP()


data_name = input( '請輸入想找的商品:' )

first_get_value(data_name)

# over_bol = True
# list_number = 0
# while over_bol == True:
#     for i in range(len(IP_list)):
#         try:
#             first_get_value(IP_list[i],data_name)
#         except:
#             print(f"失敗的:{IP_list[i]}")
#     over_bol = False