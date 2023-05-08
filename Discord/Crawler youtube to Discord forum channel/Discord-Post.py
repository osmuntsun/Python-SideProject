import json
import requests
import os
import traceback
import datetime
import time


print()

req = requests.Session()
def create_threads(titles,Videos,watchs,Videos_url,keyword_ID,keyword):
    # 設定 Discord Webhook URL
    webhook_url = f"https://discord.com/api/v9/channels/1095535060964360232/threads"

    bot_token = 'MTA5NzQ0MDAwODQ1NTA4MTk4NA.GsIWjk.d_xaiM7F8Hb9fpEyKL2fI-CuUwaoi0xF2fAs8E'
    now = datetime.datetime.now().strftime(f'%Y-%m-%d %H:%M:%S')
    # 建立 payload
    payload = {
        'message':{
        #內文
        "content": f'標題：{titles} \n\n影片時間：{Videos} \n\n在{now}擷取時\n\n{watchs} \n\n{Videos_url}'
        },
        'auto_archive_duration':4320,
        'name':f"遙久學園/{keyword}影片- BotUpdate",#標題
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
    else:
        print(f"傳送資料至 Discord 失敗。{response.status_code}")

def create_youtube(profession):
    Before_Titles = ''
    if os.path.isfile('./CheckVideo.json'):
        with open("./CheckVideo.json", "r",encoding="utf-8-sig") as f:
            f_list = f.read()
            json_data = json.loads(f_list)
            Before_Titles=json_data['Titles']


    yt_url = 'https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false'

    payload = {"context":{"client":{"hl":"zh-TW","gl":"TW","remoteHost":"2402:7500:5e6:2ab6:38d9:9b9a:2adb:8424","deviceMake":"","deviceModel":"","visitorData":"Cgt3dzFqX2M0dDlSQSj1ztKiBg%3D%3D","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36,gzip(gfe)","clientName":"WEB","clientVersion":"2.20230504.01.00","osName":"Windows","osVersion":"10.0","originalUrl":"https://www.youtube.com/@Kazeimo/videos","screenPixelDensity":1,"platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","configInfo":{"appInstallData":"CPXO0qIGELiLrgUQzK7-EhDuoq8FENf_rgUQzLf-EhCi7K4FEMO3_hIQ4tSuBRCgt_4SEL22rgUQpcL-EhDM9a4FEKqy_hIQ5LP-EhDzqK8FEK-frwUQpZmvBRCJ6K4FENShrwUQ25uvBRD-7q4FELenrwUQ5_euBRDM364FEK2rrwUQysD-Eg%3D%3D"},"screenDensityFloat":1.25,"timeZone":"Asia/Taipei","browserName":"Chrome","browserVersion":"112.0.0.0","acceptHeader":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","deviceExperimentId":"ChxOekU0T1RneU1qQXdPVGc1TmpNeU5ETTVNUT09EPXO0qIGGIbCnZ4G","screenWidthPoints":434,"screenHeightPoints":746,"utcOffsetMinutes":480,"userInterfaceTheme":"USER_INTERFACE_THEME_LIGHT","memoryTotalKbytes":"8000000","mainAppWebInfo":{"graftUrl":"/@Kazeimo/videos","pwaInstallabilityStatus":"PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED","webDisplayMode":"WEB_DISPLAY_MODE_BROWSER","isWebNativeShareAvailable":True}},"user":{"lockedSafetyMode":False},"request":{"useSsl":True,"internalExperimentFlags":[],"consistencyTokenJars":[]},"clickTracking":{"clickTrackingParams":"CC0Q8JMBGA4iEwiq7-rBy93-AhWLwUwCHR3fAts="},"adSignalsInfo":{"params":[{"key":"dt","value":"1683269494054"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"480"},{"key":"u_his","value":"6"},{"key":"u_h","value":"864"},{"key":"u_w","value":"1536"},{"key":"u_ah","value":"816"},{"key":"u_aw","value":"1536"},{"key":"u_cd","value":"24"},{"key":"bc","value":"31"},{"key":"bih","value":"729"},{"key":"biw","value":"417"},{"key":"brdim","value":"0,0,0,0,1536,0,1536,816,434,746"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}],"bid":"ANyPxKpmUxASBR45bt9W5ss7sVx-6jz-_TgQWAeJysn3OkRnWFVIHCfYu3sDQm-M3TXgrLHyE6HMV3a_YA0V8Bz8bkbtoMbj3Q"}},"browseId":"UCLHSj-ZnzmpQlZuUcnXMoVg","params":"EgZ2aWRlb3PyBgQKAjoA"}

    data = req.post(yt_url,json=payload)
    data =json.loads(data.text)
    datas = data['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]

    datas = datas['tabRenderer']['content']['richGridRenderer']['contents']
    dat = datas[0]['richItemRenderer']['content']['videoRenderer']

    titles = dat['title']['runs'][0]['text']
    print(titles)
    if Before_Titles != titles and ('闇影詩章' in titles or 'Shadowverse' in titles or 'shadowverse' in titles or '影之詩' in titles):
        Videos = dat['lengthText']['accessibility']['accessibilityData']['label']
        watchs = dat['shortViewCountText']['accessibility']['accessibilityData']['label']
        Videos_url = "https://www.youtube.com{}".format(dat['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url'])
        
        keyword = ''
        for i in titles.split('➧')[1][:8]:
            if i in profession:
                keyword = i
                break
        if keyword == '':
            keyword = 'None'

        CheckJson = {
            'Titles':titles,
            'Videotime':Videos,
            'Watchs':watchs,
            'Videos_url':Videos_url,
            'keyword':keyword,
        }
        CheckJson = json.dumps(CheckJson)
        with open('./CheckVideo.json','w',encoding="utf-8-sig") as data:
            data.write(CheckJson)

        return titles,Videos,watchs,Videos_url,keyword
    else:
        now = datetime.datetime.now().strftime(f'%Y-%m-%d %H:%M')
        with open('./Reportdata.txt','a',encoding="utf-8-sig") as data:
            data.write('-'*90)
            data.write(f'\n{now}並無PO新的文章!')
        return None,None,None,None,None,
        




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

while True:
    
    try:
        titles,Videos,watchs,Videos_url,keyword = create_youtube(profession)
        if titles==None and Videos==None and watchs==None and Videos_url==None and keyword==None:
            print('None')
        else:
            for i in tag_profession:
                if keyword in i :
                    keyword = tag_profession[tag_profession.index(i)]
                    keyword_ID = [Tag_ID[keyword],Tag_ID['影片']]
                    create_threads(titles,Videos,watchs,Videos_url,keyword_ID,keyword)
                elif keyword == 'None':
                    keyword_ID = Tag_ID['影片']
                    create_threads(titles,Videos,watchs,Videos_url,keyword) 
    except Exception as e:
        # 將錯誤信息寫入到一個檔案中
        now = datetime.datetime.now().strftime(f'%Y-%m-%d')
        with open("./Error.txt", "a") as f:
            spilt_str = '-'*90
            f.write(now+spilt_str)
            traceback.print_exc(file=f)
    time.sleep(3600)


