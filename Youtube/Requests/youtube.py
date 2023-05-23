import requests
import json
import time

req = requests.Session()
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

    channel_ID = ''
    for data in channel_datas:
        if 'channelRenderer' in data:
            data = data['channelRenderer']
            if data['title']['simpleText'] == youtube_user_name:
                channel_ID = data['channelId']
                break
    
    return channel_ID


def frist_page(channel_ID):

    url = 'https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false'
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

    payload = json.dumps(payload)
    datas = req.post(url,data=payload)
    datas = json.loads(datas.text)
    url_list = {}
    datas = datas['contents']['twoColumnBrowseResultsRenderer']['tabs'][1]['tabRenderer']['content']['richGridRenderer']['contents']
    number_sum=0
    for data in datas:
        if 'richItemRenderer' in data:
            url_id = data['richItemRenderer']['content']['videoRenderer']['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
            title = data['richItemRenderer']['content']['videoRenderer']['title']['runs'][0]['text']
            video_url = f'https://www.youtube.com{url_id}'
            url_list[title] = video_url
            number_sum+=1
            print(number_sum)
        elif 'continuationItemRenderer' in data:
            next_token = data['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']
            return next_token,url_list,number_sum
        else:
            next_token = None
            return next_token,url_list


def next_page(token,url_list,number_sum):
    url = 'https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false'
    payload = {
    "context": {
        "client": {
        "remoteHost": "2402:7500:4e5:a81a:7d95:1fb8:2efd:bb3e",
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36,gzip(gfe)",
        "clientName": "WEB",
        "clientVersion": "2.20230509.07.00",
        },
    },
    'continuation':token
    }
    json_payload = json.dumps(payload)
    datas = req.post(url,data=json_payload)
    datas = json.loads(datas.text)

    datas = datas['onResponseReceivedActions'][0]['appendContinuationItemsAction']['continuationItems']
    for data in datas:
        if 'richItemRenderer' in data:
            url_ID = data['richItemRenderer']['content']['videoRenderer']['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
            title = data['richItemRenderer']['content']['videoRenderer']['title']['runs'][0]['text']
            video_url = f'https://www.youtube.com{url_ID}'
            url_list[title] = video_url
            number_sum += 1
            print(number_sum)
    
        elif 'continuationItemRenderer' in data:
            token = data['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']
            condition_bool = True
            return url_list,token,condition_bool,number_sum
        else:
            condition_bool = False
            token=''
            return url_list,token,condition_bool,number_sum
    condition_bool = False
    token=''
    return url_list,token,condition_bool,number_sum

def Playlist(channel_ID):
    
    url = 'https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false'
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
    "params": "EglwbGF5bGlzdHPyBgQKAkIA"
    }
    payload = json.dumps(payload)
    datas = req.post(url,data=payload)
    datas = json.loads(datas.text)
    datas = datas['contents']['twoColumnBrowseResultsRenderer']['tabs']
    for i in datas:
        if i['tabRenderer']['title'] == 'Playlists':
            datas = i['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['gridRenderer']['items']
            break


    playlist_url = []
    for data in datas:
        playlistId = data['gridPlaylistRenderer']['viewPlaylistText']['runs'][0]['navigationEndpoint']['browseEndpoint']['browseId']
        playlist_url.append(playlistId)
    
    return playlist_url

def Playlist_video(playlist_url,play_url):
    url = 'https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false'
    payload = {
    "context": {
        "client": {
        "remoteHost": "2402:7500:4e5:a81a:7d95:1fb8:2efd:bb3e",
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36,gzip(gfe)",
        "clientName": "WEB",
        "clientVersion": "2.20230509.07.00",
        },
    },
    "browseId": f"{playlist_url}",
    }
    
    payload = json.dumps(payload)
    datas = req.post(url,data=payload)
    datas = json.loads(datas.text)
    datas = datas['contents']['twoColumnBrowseResultsRenderer']['tabs'][0]['tabRenderer']['content']['sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents'][0]['playlistVideoListRenderer']['contents']
    playlist_token=''
    for data in datas:
        try:
        # if 'playlistVideoRenderer' in data:
            url_ID = data['playlistVideoRenderer']['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
            title = data['playlistVideoRenderer']['title']['runs'][0]['text']
            url = f'https://www.youtube.com{url_ID}'
            play_url[title] = url
        except:
            playlist_token = data['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']
    
    
    return play_url,playlist_token

def Playlist_video_next(play_url,playlist_token):
    url = 'https://www.youtube.com/youtubei/v1/browse?key=AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8&prettyPrint=false'
    payload = {
    "context": {
        "client": {
        "remoteHost": "2402:7500:4e5:a81a:7d95:1fb8:2efd:bb3e",
        "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36,gzip(gfe)",
        "clientName": "WEB",
        "clientVersion": "2.20230509.07.00",
        },
    },
    'continuation':playlist_token
    }
    json_payload = json.dumps(payload)
    datas = req.post(url,data=json_payload)
    datas = json.loads(datas.text)
    datas = datas['onResponseReceivedActions'][0]['appendContinuationItemsAction']['continuationItems']
    playlist_token = ''
    for data in datas:
        if 'playlistVideoRenderer' in data:
            url_id = data['playlistVideoRenderer']['navigationEndpoint']['commandMetadata']['webCommandMetadata']['url']
            title = data['playlistVideoRenderer']['title']['runs'][0]['text']
            url = f'https://www.youtube.com{url_id}'
            play_url[title] = url
        else:
            playlist_token = data['continuationItemRenderer']['continuationEndpoint']['continuationCommand']['token']
    
    if playlist_token == '':
        bol=False
        return play_url,playlist_token,bol
    else:
        bol=True
        return play_url,playlist_token,bol

    


channelname = '⚡Apex頂尖裂開者'

channel_IDs = Get_channel_ID(channelname)

token,url_list,number_sum = frist_page(channel_IDs)
if token!=None:
    condition_bool = True

while condition_bool == True:
    url_list,token,condition_bool,number_sum = next_page(token,url_list,number_sum)


allurl_list = url_list
print("--- 抓取 播放清單 作業 ---")


playlist_url = Playlist(channel_IDs)


play_url={}
for i in playlist_url:
    play_url,playlist_token = Playlist_video(i,play_url)
    if playlist_token !="":
        bol = True
        while bol==True:
            play_url,playlist_token,bol = Playlist_video_next(play_url,playlist_token)

key_play_url = set(play_url.keys())
key_url_list = set(url_list.keys())

result = {key: url_list[key] for key in key_url_list - key_play_url}




with open(f'./Youtube-{channelname}全部影片連結.txt','a',encoding="utf-8-sig") as f:
    for i in allurl_list.keys():
        f.write(allurl_list[i]+"\n")
with open(f'./Youtube-{channelname}去掉播放清單影片連結.txt','a',encoding="utf-8-sig") as f:
    for i in result.keys():
        f.write(result[i]+"\n")

print(f'完成{channelname}')