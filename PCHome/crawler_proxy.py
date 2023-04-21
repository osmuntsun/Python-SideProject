import requests 
import json
import urllib.request as req
import csv

def crawler_IP():
    IP_cheak=[]
    OK_ip = 0
    fail_ip = 0
    for i in range(1, 11):
        url = f'https://proxylist.geonode.com/api/proxy-list?limit=50&page={i}&sort_by=lastChecked&sort_type=desc'

        request = req.Request(url ,headers={
            'cookie':'mid=WLsL4gAEAAGl0Wjoc8Dv6CH_iYnP; mcd=3; ds_user_id=1926542376; csrftoken=9aasLCq0vb2dUQWY9j1rjP11aejod1wS; sessionid=1926542376%3AG5zq9okSZhBxWx%3A8; ig_did=8675D711-4D34-4DBA-8751-F9E4E3B8FA63; shbid=17721; shbts=1602880097.7694821; rur=VLL; urlgen="{\"61.228.154.31\": 3462}:1kTWVn:7qfV2Cxf3rs1oZ9BUi45bNQ18T4',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win32; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        })

        with req.urlopen(request) as response:
            data = response.read().decode('utf-8')

        data = json.loads(data)
        datas = data['data']

        IP_list = []
        for data in datas:
            str_ip = f"{data['ip']}:{data['port']}"
            IP_list.append(str_ip)

        
        for ip in IP_list:
            try:
                res = requests.get('https://api.ipify.org?format=json',proxies={'http':ip,'https':ip}, timeout=10)
                IP_cheak.append(ip)
                OK_ip +=1
                print( res.json() )
            except:
                fail_ip+=1
                print('FAIL',ip)

    print('OK',OK_ip)
    print('FAIL',fail_ip)

    if OK_ip >= 1:
        with open('./ip_data.csv','a',encoding='utf-8-sig',newline='') as f:
            writer = csv.writer(f)
            for data in IP_cheak:
                writer.writerow([data])


def get_IP():
    try:
        IP_list = []
        with open("./ip_data.csv",mode="r", encoding="utf-8-sig") as f:
            for data in f:
                data = data.replace('\n','')
                IP_list.append(data)
            del IP_list[0]
        return IP_list
    except:
        print('沒有ip_data.csv的檔案請執行crawler_IP來獲取檔案')

if __name__ == "__main__":
    crawler_IP()