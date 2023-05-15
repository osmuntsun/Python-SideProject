import json
import requests
import os
import traceback
import datetime
import time

req = requests.Session()
def create_threads(titles,Videos,watchs,Videos_url,keyword_ID,keyword_all_name,quarterly,keyword='語風'):
    # 設定 Discord Webhook URL
    webhook_url = f"https://discord.com/api/v9/channels/1095535060964360232/threads"

    bot_token = 'MTA5NzQ0MDAwODQ1NTA4MTk4NA.G0NRvQ.kI4sPFPVx4PpaGezcUBZ5YI4xjF49go9XykztU'
    now = datetime.datetime.now().strftime(f'%Y-%m-%d %H:%M:%S')
    message_now = datetime.datetime.now().strftime(f'%Y-%m-%d')
    # 建立 payload
    payload = {
        'message':{
        #內文
        "content": f'標題：{titles} \n\n影片時間：{Videos} \n\n在{now}擷取時\n\n{watchs} \n\n{Videos_url}'
        },
        'auto_archive_duration':4320,
        'name':f"{quarterly}/{keyword_all_name} ({message_now}) - BotUpdate",#標題
        'applied_tags':keyword_ID,# 標籤
        }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bot {bot_token}"
    }

    # 發送 POST 請求

    response = req.post(webhook_url,json=payload,headers = headers)

    # 檢查是否成功
    if response.status_code == 204 or response.status_code == 201 or response.status_code == 200:
        print("已成功傳送資料至 Discord。")
        now = datetime.datetime.now().strftime(f'%Y-%m-%d %H:%M')
        with open('./Reportdata.txt','a',encoding="utf-8-sig") as data:
            data.write('-'*90)
            data.write(f'\n{now}有新的文章!')
            print(f"目前版本：{quarterly}")
    else:
        print(f"傳送資料至 Discord 失敗。{response.status_code}")
        print(f"目前版本：{quarterly}")

def Get_channel_ID(youtube_user_name):
    search_url  = 'https://www.youtube.com/youtubei/v1/search?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false'

    payload = {
    "context": {
        "client": {
        "hl": "zh-TW",
        "gl": "TW",
        "remoteHost": "2402:7500:4e5:a81a:7d95:1fb8:2efd:bb3e",
        "deviceMake": "",
        "deviceModel": "",
        "visitorData": "Cgt3dzFqX2M0dDlSQSj13PKiBg%3D%3D",
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36,gzip(gfe)",
        "clientName": "WEB",
        "clientVersion": "2.20230509.07.00",
        "osName": "Windows",
        "osVersion": "10.0",
        "screenPixelDensity": 1,
        "platform": "DESKTOP",
        "clientFormFactor": "UNKNOWN_FORM_FACTOR",
        "configInfo": {
            "appInstallData": "CPXc8qIGEP7urgUQ1KyvBRCi7K4FEOSz_hIQpZmvBRC9tq4FEMyu_hIQw7f-EhDbm68FEOf3rgUQ4tSuBRCvn68FEIGdrwUQga6vBRC4i64FEO6irwUQ1KGvBRDM364FEKC3_hIQ1_-uBRCJ6K4FEPOorwUQqrL-EhDMt_4SEKXC_hIQysD-EhCtq68F"
        },
        "screenDensityFloat": 1.25,
        "timeZone": "Asia/Taipei",
        "browserName": "Chrome",
        "browserVersion": "112.0.0.0",
        "acceptHeader": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "deviceExperimentId": "ChxOekU0T1RneU1qQXdPVGc1TmpNeU5ETTVNUT09EPXc8qIGGIbCnZ4G",
        "screenWidthPoints": 346,
        "screenHeightPoints": 746,
        "utcOffsetMinutes": 480,
        "userInterfaceTheme": "USER_INTERFACE_THEME_LIGHT",
        "memoryTotalKbytes": "8000000",
        "mainAppWebInfo": {
            "graftUrl": "/results?search_query=%E5%AE%89%E9%9D%9C%E8%B2%93",
            "pwaInstallabilityStatus": "PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED",
            "webDisplayMode": "WEB_DISPLAY_MODE_BROWSER",
            "isWebNativeShareAvailable": True
        }
        },
        "user": {
        "lockedSafetyMode": False
        },
        "request": {
        "useSsl": True,
        "internalExperimentFlags": [],
        "consistencyTokenJars": []
        },
        "clickTracking": {
        "clickTrackingParams": "CBMQ7VAiEwi51cie4e7-AhXX7EwCHZ3OBrM="
        },
        "adSignalsInfo": {
        "params": [
            {
            "key": "dt",
            "value": "1683795573502"
            },
            {
            "key": "flash",
            "value": "0"
            },
            {
            "key": "frm",
            "value": "0"
            },
            {
            "key": "u_tz",
            "value": "480"
            },
            {
            "key": "u_his",
            "value": "32"
            },
            {
            "key": "u_h",
            "value": "864"
            },
            {
            "key": "u_w",
            "value": "1536"
            },
            {
            "key": "u_ah",
            "value": "816"
            },
            {
            "key": "u_aw",
            "value": "1536"
            },
            {
            "key": "u_cd",
            "value": "24"
            },
            {
            "key": "bc",
            "value": "31"
            },
            {
            "key": "bih",
            "value": "729"
            },
            {
            "key": "biw",
            "value": "330"
            },
            {
            "key": "brdim",
            "value": "0,0,0,0,1536,0,1536,816,346,746"
            },
            {
            "key": "vis",
            "value": "1"
            },
            {
            "key": "wgl",
            "value": "true"
            },
            {
            "key": "ca_type",
            "value": "image"
            }
        ],
        "bid": "ANyPxKo5qXf6M4grCGwwPP6eAZ0Yw9T82_P5u4hEd58jGxF4ItYv6asSAde3s1XeO68WsPgrkf6ugjSNQ-F6Fjj9M-Z4FXni8g"
        }
    },
    "query": f"{youtube_user_name}",
    "webSearchboxStatsUrl": f"/search?oq={youtube_user_name}&gs_l=youtube.12..0i512k1.185004.185004.4.191318.1.1.0.0.0.0.212.212.2-1.1.0.ytne5p_e,ytpo-bo-vo-ntt=EXP,ytposo-bo-vo-ntt=EXP,ytpo-bo-vo-bis=1,ytposo-bo-vo-bis=1,ytpo-bo-vo-isb=10,ytposo-bo-vo-isb=10...0...1ac..64.youtube..0.1.212....0.62pJMnGrqG4"
    }
    json_payload = json.dumps(payload)
    search_data = req.post(search_url,data=json_payload)
    channel_data = json.loads(search_data.text)

    channel_datas = channel_data['contents']['twoColumnSearchResultsRenderer']['primaryContents']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']


    for data in channel_datas:
        if 'channelRenderer' in data:
            data = data['channelRenderer']
            if data['title']['simpleText'] == youtube_user_name:
                channel_ID = data['channelId']
                break
    return channel_ID

def condition_Tag(titles,Videos,watchs,Videos_url,keyword_all_name,Channelname,quarterly,keyword):
    if titles==None and Videos==None and watchs==None and Videos_url==None and keyword==None:
        print(f'{Channelname} - 目前沒有新影片')
        print(f"目前版本：{quarterly}")
    else:
        for i in tag_profession:
            if keyword in i :
                keyword = tag_profession[tag_profession.index(i)]
                keyword_ID = [Tag_ID[keyword],Tag_ID['影片']]
                create_threads(titles,Videos,watchs,Videos_url,keyword_ID,keyword_all_name,quarterly,keyword)
            elif keyword == 'None':
                keyword_ID = Tag_ID['影片']
                create_threads(titles,Videos,watchs,Videos_url,keyword_ID,keyword_all_name,quarterly,keyword) 

def Json_information(Channelname,titles,Videos,watchs,Videos_url,keyword,quarterly='遙久學園'):
    new_CheckJson = {
            Channelname:{
            'quarterly':quarterly,
            'Titles':titles,
            'Videotime':Videos,
            'Watchs':watchs,
            'Videos_url':Videos_url,
            'keyword':keyword,
            }
        }
    return new_CheckJson

def condition_title(Channelname,titles,Videos,watchs,Videos_url,json_data,profession,quarterly):
    if Channelname == '語風薯薯撿到貓 Kazeimo Ch. 【終焉理想庭】':
        keyword = ''
        for i in titles.split('➧')[1][:8]:
            text_str = titles.split('➧')[1][:8]
            keyword_all_name = text_str[:text_str.index('T')+2]
            if i in profession:
                keyword = i
                break
        if keyword == '':
            keyword = 'None'

        new_CheckJson=Json_information(Channelname,titles,Videos,watchs,Videos_url,keyword,quarterly)
        json_data.update(new_CheckJson)
        CheckJson = json.dumps(json_data)
        with open('./CheckVideo.json','w',encoding="utf-8-sig") as data:
            data.write(CheckJson)
        return titles,Videos,watchs,Videos_url,keyword,keyword_all_name,quarterly
    elif Channelname == '安靜貓':
        keyword = ''
        quarterly =titles.split('｜')[-1].split('/ ')[-1]
        keyword_all_name =titles.split('｜')[0]
        print(keyword_all_name)
        for i in titles.split('｜')[0]:
            if i in profession:
                keyword = i
                break
        if keyword == '':
            keyword = 'None'

        print(keyword)

        new_CheckJson=Json_information(Channelname,titles,Videos,watchs,Videos_url,keyword,quarterly)
        json_data.update(new_CheckJson)
        CheckJson = json.dumps(json_data)
        with open('./CheckVideo.json','w',encoding="utf-8-sig") as data:
            data.write(CheckJson)
        return titles,Videos,watchs,Videos_url,keyword,keyword_all_name,quarterly
    else:
        return None,None,None,None,None,None

def check_title_name(dat,Before_Titles,titles,profession,Channelname,json_data,quarterly):
    if Before_Titles != titles and ('闇影詩章' in titles or 'Shadowverse' in titles or 'shadowverse' in titles or '影之詩' in titles):
        # 影片時間
        Videos = dat['lengthText']['accessibility']['accessibilityData']['label']
        # 觀看人數
        watchs = dat['shortViewCountText']['accessibility']['accessibilityData']['label']
        # 影片網址
        Videos_url = "https://www.youtube.com{}".format(dat['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url'])

        titles,Videos,watchs,Videos_url,keyword,keyword_all_name,quarterly=condition_title(Channelname,titles,Videos,watchs,Videos_url,json_data,profession,quarterly)
        return titles,Videos,watchs,Videos_url,keyword,keyword_all_name,quarterly
    else:
        now = datetime.datetime.now().strftime(f'%Y-%m-%d %H:%M')
        with open('./Reportdata.txt','a',encoding="utf-8-sig") as data:
            data.write('-'*90)
            data.write(f'\n{Channelname}\n{now}並無PO新的文章!')
        return None,None,None,None,None,None,quarterly
        
def create_youtube(profession,channel_ID,Channelname):
    Before_Titles = ''
    json_data = {}
    quarterly = '遙久學園'
    if os.path.isfile('./CheckVideo.json'):
        with open("./CheckVideo.json", "r",encoding="utf-8-sig") as f:
            f_list = f.read()
            json_data = json.loads(f_list)
            if Channelname in json_data:
                Before_Titles=json_data[Channelname]['Titles']
                quarterly = json_data['安靜貓']['quarterly']

    yt_url = 'https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false'

    payload = {
        "context": {
            "client": {
            "remoteHost": "2402:7500:4e5:a81a:7d95:1fb8:2efd:bb3e",
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36,gzip(gfe)",
            "clientName": "WEB",
            "clientVersion": "2.20230509.07.00",
            },
        },
        "browseId": f"{channel_ID}",
        "params": "EgZ2aWRlb3PyBgQKAjoA"
    }
    payloads = json.dumps(payload)
    data = req.post(yt_url,data=payloads)
    data =json.loads(data.text)
    datas = data['contents']['twoColumnBrowseResultsRenderer']['tabs']
    datas = datas[1]['tabRenderer']['content']['richGridRenderer']['contents']
    dat = datas[0]['richItemRenderer']['content']['videoRenderer']
    # 影片標題
    titles = dat['title']['runs'][0]['text']
    titles, Videos, watchs, Videos_url, keyword, keyword_all_name,quarterly=check_title_name(dat,Before_Titles,titles,profession,Channelname,json_data,quarterly)
    return titles, Videos, watchs, Videos_url, keyword, keyword_all_name,quarterly

profession = ['精', '靈', '妖', '精', '皇', '家', '吸', '血', '鬼', '龍', '族', '死', '靈', '主', '教', '復', '仇', '者', '巫', '師']
tag_profession = [
    '精靈',"妖精",'皇家','吸血鬼','龍族','死靈','主教','復仇者','巫師'
]

Tag_ID = {
    '精靈': '1095535748658253844',
    '皇家': '1095535790924243055',
    '吸血鬼': '1095535820892545167',
    '龍族': '1095535877524049930',
    '死靈': '1095535912433229906',
    '主教': '1095536064535478382',
    '復仇者': '1095536136841084970',
    '巫師': '1095536576051810385',
    '精華': '1095536885083947009',
    '更新': '1095536971000053890',
    '牌組': '1095537041393061989',
    '影片': '1095537123177812068',
    '連結': '1096445014126641253'
}

channel_names = ['安靜貓','語風薯薯撿到貓 Kazeimo Ch. 【終焉理想庭】']
while True:
    try:
        for Channelname in channel_names:
            print('-'*90)
            channel_ID = Get_channel_ID(Channelname)
            titles, Videos, watchs, Videos_url, keyword, keyword_all_name, quarterly = create_youtube(profession,channel_ID,Channelname)
            condition_Tag(titles,Videos,watchs,Videos_url,keyword_all_name,Channelname,quarterly,keyword=keyword)
    except Exception as e:
        # 將錯誤信息寫入到一個檔案中
        now = datetime.datetime.now().strftime(f'%Y-%m-%d')
        with open("./Error.txt", "a") as f:
            spilt_str = '-'*90
            f.write(now+'\n'+spilt_str)
            traceback.print_exc(file=f)
    time.sleep(3600)


