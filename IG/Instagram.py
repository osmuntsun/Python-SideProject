import urllib.request as req
import requests
import json
import datetime
from os import environ,path,mkdir
import base64
import sqlite3
from win32.win32crypt import CryptUnprotectData
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def get_string(local_state):
    with open(local_state, 'r', encoding='utf-8') as f:
        s = json.load(f)['os_crypt']['encrypted_key']
    return s

def pull_the_key(base64_encrypted_key):
    encrypted_key_with_header = base64.b64decode(base64_encrypted_key)
    encrypted_key = encrypted_key_with_header[5:]
    key = CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
    return key

def decrypt_string(key, data):
    nonce, cipherbytes = data[3:15], data[15:]
    aesgcm = AESGCM(key)
    plainbytes = aesgcm.decrypt(nonce, cipherbytes, None)
    plaintext = plainbytes.decode('utf-8')
    return plaintext


def get_cookie_from_chrome(host: '.oschina.net'):
    local_state = environ['LOCALAPPDATA'] + r'\Google\Chrome\User Data\Local State'
    cookie_path = environ['LOCALAPPDATA'] + r"\Google\Chrome\User Data\Default\Network\Cookies"
    
    sql = "select host_key,name,encrypted_value from 'cookies' where host_key='%s'" % host

    with sqlite3.connect(cookie_path) as conn:
        cu = conn.cursor()
        res = cu.execute(sql).fetchall()
        cu.close()
        cookies = {}
        key = pull_the_key(get_string(local_state))
        for host_key, name, encrypted_value in res:
            if encrypted_value[0:3] == b'v10':
                cookies[name] = decrypt_string(key, encrypted_value)
            else:
                cookies[name] = CryptUnprotectData(encrypted_value)[1].decode()

        return cookies


cookies = get_cookie_from_chrome('.instagram.com')

cookies1 = f"cookie':'mid={cookies['mid']}; mcd=3; ds_user_id={cookies['ds_user_id']}; csrftoken={cookies['csrftoken']}; sessionid={cookies['sessionid']}; ig_did={cookies['ig_did']}; shbid={cookies['shbid']}; shbts={cookies['shbts']};"
cookies2 =  b'rur=VLL; urlgen="{\"61.228.154.31\": 3462}:1kTWVn:7qfV2Cxf3rs1oZ9BUi45bNQ18T4'
cookies = cookies1+cookies2.decode('utf-8')

def vid(url,username,i):
    r = requests.get(url)
    if path.isdir(f'./{username}'):
        if path.isdir(f'./{username}/posts'):
            if path.isdir(f'./{username}/posts/Videos'):
                with open(f'./{username}/posts/Videos/vid{i}.mp4', "wb") as code:
                    code.write(r.content)
            else:
                mkdir(f"./{username}/posts/Videos")
                with open(f'./{username}/posts/Videos/vid{i}.mp4', "wb") as code:
                    code.write(r.content)
        else:
            mkdir(f"./{username}/posts")
            if path.isdir(f'./{username}/posts/Videos'):
                with open(f'./{username}/posts/Videos/vid{i}.mp4', "wb") as code:
                    code.write(r.content)
            else:
                mkdir(f"./{username}/posts/Videos")
                with open(f'./{username}/posts/Videos/vid{i}.mp4', "wb") as code:
                    code.write(r.content)
    else:
        mkdir(f"./{username}")
        if path.isdir(f'./{username}/posts'):
            if path.isdir(f'./{username}/posts/Videos'):
                with open(f'./{username}/posts/Videos/vid{i}.mp4', "wb") as code:
                    code.write(r.content)
            else:
                mkdir(f"./{username}/posts/Videos")
                with open(f'./{username}/posts/Videos/vid{i}.mp4', "wb") as code:
                    code.write(r.content)
        else:
            mkdir(f"./{username}/posts")
            if path.isdir(f'./{username}/posts/Videos'):
                with open(f'./{username}/posts/Videos/vid{i}.mp4', "wb") as code:
                    code.write(r.content)
            else:
                mkdir(f"./{username}/posts/Videos")
                with open(f'./{username}/posts/Videos/vid{i}.mp4', "wb") as code:
                    code.write(r.content)


def img(url,username,i):
    r = requests.get(url)
    if path.isdir(f'./{username}'):
        if path.isdir(f'./{username}/posts'):
            if path.isdir(f'./{username}/posts/Images'):
                with open(f'./{username}/posts/Images/image{i}.jpg', "wb") as code:
                    code.write(r.content)
            else:
                mkdir(f"./{username}/posts/Images")
                with open(f'./{username}/posts/Images/image{i}.jpg', "wb") as code:
                    code.write(r.content)
        else:
            mkdir(f"./{username}/posts")
            if path.isdir(f'./{username}/posts/Images'):
                with open(f'./{username}/posts/Images/image{i}.jpg', "wb") as code:
                    code.write(r.content)
            else:
                mkdir(f"./{username}/posts/Images")
                with open(f'./{username}/posts/Images/image{i}.jpg', "wb") as code:
                    code.write(r.content)
    else:
        mkdir(f"./{username}")
        if path.isdir(f'./{username}/posts'):
            if path.isdir(f'./{username}/posts/Images'):
                with open(f'./{username}/posts/Images/image{i}.jpg', "wb") as code:
                    code.write(r.content)
            else:
                mkdir(f"./{username}/posts/Images")
                with open(f'./{username}/posts/Images/image{i}.jpg', "wb") as code:
                    code.write(r.content)
        else:
            mkdir(f"./{username}/posts")
            if path.isdir(f'./{username}/posts/Images'):
                with open(f'./{username}/posts/Images/image{i}.jpg', "wb") as code:
                    code.write(r.content)
            else:
                mkdir(f"./{username}/posts/Images")
                with open(f'./{username}/posts/Images/image{i}.jpg', "wb") as code:
                    code.write(r.content)
    

def next_url(url_key,user_id):
    url_key = url_key.replace('==','')
    next_url=f'https://www.instagram.com/graphql/query/?query_hash=69cba40317214236af40e7efa697781d&variables=%7B%22id%22%3A%22{user_id}%22%2C%22first%22%3A12%2C%22after%22%3A%22{url_key}%3D%3D%22%7D'
    next_url = requests.get(next_url, headers={
        # 'cookie':'mid=WLsL4gAEAAGl0Wjoc8Dv6CH_iYnP; mcd=3; ds_user_id=1926542376; csrftoken=9aasLCq0vb2dUQWY9j1rjP11aejod1wS; sessionid=1926542376%3AG5zq9okSZhBxWx%3A8; ig_did=8675D711-4D34-4DBA-8751-F9E4E3B8FA63; shbid=17721; shbts=1602880097.7694821; rur=VLL; urlgen="{\"61.228.154.31\": 3462}:1kTWVn:7qfV2Cxf3rs1oZ9BUi45bNQ18T4',
        'cookie':cookies,
        'User-Agent':'Instagram 219.0.0.12.117 Android',
    })
    next_url = json.loads(next_url.text)
    return next_url

def DownloadSOP(i,TF,user,img_sum,vid_sum):
    if TF == 'GraphSidecar':
        posts = i['node']['edge_sidecar_to_children']['edges']
        for post in posts:
            if post['node']['is_video'] == True:
                vid_sum+=1
                vid(post['node']['video_url'],user,vid_sum)
            else:
                img_sum+=1
                img(post['node']['display_url'],user,img_sum)
    elif TF == 'GraphVideo':
        vid_sum+=1
        vid(i['node']['video_url'],user,vid_sum)
    elif TF == 'GraphImage':
        img_sum+=1
        img(i['node']['display_url'],user,img_sum)
    return img_sum,vid_sum

def for_page(datas,user,img_sum ,vid_sum):

    users = ''
    for i in datas:
        users = i['node']['owner']['username']
        TF = i['node']['__typename']
        if os.path.exists("./%s"%user) and user==users:
            img_sum ,vid_sum = DownloadSOP(i,TF,user,img_sum ,vid_sum)
        elif user==users:
            os.mkdir("./%s"%user)
            img_sum ,vid_sum = DownloadSOP(i,TF,user,img_sum ,vid_sum)
        else:
            print('抓錯了')
            return users,img_sum ,vid_sum
    return users,img_sum ,vid_sum

def igcrawler(user,cookies):
    url = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={user}'

    request = requests.get(url, headers={
        # 'cookie':'mid=WLsL4gAEAAGl0Wjoc8Dv6CH_iYnP; mcd=3; ds_user_id=1926542376; csrftoken=9aasLCq0vb2dUQWY9j1rjP11aejod1wS; sessionid=1926542376%3AG5zq9okSZhBxWx%3A8; ig_did=8675D711-4D34-4DBA-8751-F9E4E3B8FA63; shbid=17721; shbts=1602880097.7694821; rur=VLL; urlgen="{\"61.228.154.31\": 3462}:1kTWVn:7qfV2Cxf3rs1oZ9BUi45bNQ18T4',
        'cookie':cookies,
        'User-Agent':'Instagram 219.0.0.12.117 Android',
    })
    data = json.loads(request.text)
    datas = data['data']['user']['edge_owner_to_timeline_media']['edges']
    frist_determine = data['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
    frist_next_page = data['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
    frist_users = data['data']['user']['username']
    user_id = data['data']['user']['id']

    img_sum=0
    vid_sum=0
    print(user_id)
    for i in datas:
        TF = i['node']['__typename']
        if path.exists("./%s"%user):
            img_sum ,vid_sum= DownloadSOP(i,TF,user,img_sum,vid_sum)
        else:
            mkdir("./%s"%user)
            img_sum ,vid_sum = DownloadSOP(i,TF,user,img_sum,vid_sum)


    if frist_determine == True and frist_users==user :
        url = next_url(frist_next_page,user_id)
        next_page=url['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
        ws = url['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
        range_total = 0
        users = user
        while next_page and user == users:
            range_total += 1
            url = next_url(ws,user_id)
            users ,img_sum ,vid_sum = for_page(url['data']['user']['edge_owner_to_timeline_media']['edges'],user,img_sum ,vid_sum)
            ws = url['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
            next_page = url['data']['user']['edge_owner_to_timeline_media']['page_info']['has_next_page']
            print(f'跑完第{range_total}輪(每輪12則貼文)')
    
    print(f'{user}的帳號裡    照片　　總共有 {img_sum} 個檔案')
    print(f'{user}的帳號裡    影片　　總共有 {vid_sum} 個檔案')
    print(f'{user}的帳號裡 影片、照片 總共有 {img_sum + vid_sum} 個檔案')

def highlight_Download(url,title,number,types_str):
    r = requests.get(url)
    if '/' in title:
        title = str(title).replace('/','-')
    if path.isdir(f'./{username}'):
        if path.isdir(f'./{username}/{title}'):
            with open(f'./{username}/{title}/{number}-highlight.{types_str}', "wb") as code:
                code.write(r.content)
        else:
            mkdir(f"./{username}/{title}")
            with open(f'./{username}/{title}/{number}-highlight.{types_str}', "wb") as code:
                code.write(r.content)
    else:
        mkdir(f"./{username}")
        if path.isdir(f'./{username}/{title}'):
            with open(f'./{username}/{title}/{number}-highlight.{types_str}', "wb") as code:
                code.write(r.content)
        else:
            mkdir(f"./{username}/{title}")
            with open(f'./{username}/{title}/{number}-highlight.{types_str}', "wb") as code:
                code.write(r.content)


def crawler_highlight(username,cookies):
    url = f'https://www.instagram.com/graphql/query/?query_hash=d4d88dc1500312af6f937f7b804c68c3&variables=%7B%22user_id%22%3A%22{username}%22%2C%22include_chaining%22%3Atrue%2C%22include_reel%22%3Afalse%2C%22include_suggested_users%22%3Afalse%2C%22include_logged_out_extras%22%3Afalse%2C%22include_highlight_reels%22%3Atrue%2C%22include_live_status%22%3Atrue%7D'
    request = requests.get(url, headers={
        'cookie':cookies,
        'User-Agent':'Instagram 219.0.0.12.117 Android',
    })
    data = json.loads(request.text)
    highlights_ID = data['data']['user']['edge_highlight_reels']['edges']
    for i in highlights_ID:
        numbers = 0
        highlight_ID = i['node']['id']
        highlight_title = i['node']['title']
        highlight_url = f'https://i.instagram.com/api/v1/feed/reels_media/?reel_ids=highlight%3A{highlight_ID}'
        request = requests.get(highlight_url, headers={
            'cookie':cookies,
            'User-Agent':'Instagram 219.0.0.12.117 Android',
        })
        highlights_alldata = json.loads(request.text)
        highlights_datas = highlights_alldata['reels'][f'highlight:{highlight_ID}']['items']
        for j in highlights_datas:
            numbers += 1
            data_keys = j.keys()
            if 'video_versions' in data_keys:
                vid_url = j['video_versions'][0]['url']
                highlight_Download(vid_url,highlight_title,numbers,'mp4')
            else:
                jpg_url = j['image_versions2']['candidates'][0]['url']
                highlight_Download(jpg_url,highlight_title,numbers,'jpg')

def Timelimited_Download(url,now,number,types_str):
    r = requests.get(url)
    if '/' in now:
        now = str(now).replace('/','-')
    if path.isdir(f'./{username}'):
        if path.isdir(f'./{username}/限時'):
            if path.isdir(f'./{username}/限時/{now}'):
                with open(f'./{username}/限時/{now}/{number}-Timelimited.{types_str}', "wb") as code:
                    code.write(r.content)
            else:
                mkdir(f"./{username}/限時/{now}")
                with open(f'./{username}/限時/{now}/{number}-Timelimited.{types_str}', "wb") as code:
                    code.write(r.content)
        else:
            mkdir(f"./{username}/限時")
            if path.isdir(f'./{username}/限時/{now}'):
                with open(f'./{username}/限時/{now}/{number}-Timelimited.{types_str}', "wb") as code:
                    code.write(r.content)
            else:
                mkdir(f"./{username}/限時/{now}")
                with open(f'./{username}/限時/{now}/{number}-Timelimited.{types_str}', "wb") as code:
                    code.write(r.content)
    else:
        mkdir(f"./{username}")
        if path.isdir(f'./{username}/限時'):
            if path.isdir(f'./{username}/限時/{now}'):
                with open(f'./{username}/限時/{now}/{number}-Timelimited.{types_str}', "wb") as code:
                    code.write(r.content)
            else:
                mkdir(f"./{username}/限時/{now}")
                with open(f'./{username}/限時/{now}/{number}-Timelimited.{types_str}', "wb") as code:
                    code.write(r.content)
        else:
            mkdir(f"./{username}/限時")
            if path.isdir(f'./{username}/限時/{now}'):
                with open(f'./{username}/限時/{now}/{number}-Timelimited.{types_str}', "wb") as code:
                    code.write(r.content)
            else:
                mkdir(f"./{username}/限時/{now}")
                with open(f'./{username}/限時/{now}/{number}-Timelimited.{types_str}', "wb") as code:
                    code.write(r.content)

def crawler_Timelimited(ID,cookies):
    url = f'https://www.instagram.com/api/v1/feed/reels_media/?reel_ids={ID}'
    request = requests.get(url, headers={
        'cookie':cookies,
        'User-Agent':'Instagram 219.0.0.12.117 Android',
    })
    data = json.loads(request.text)
    Timelimited_data = data['reels'][f'{ID}']['items']
    numbers = 0
    now = datetime.datetime.now()
    now_date = now.strftime(f'%Y%m%d')
    for j in Timelimited_data:
        numbers += 1
        data_keys = j.keys()
        if 'video_versions' in data_keys:
            vid_url = j['video_versions'][0]['url']
            Timelimited_Download(vid_url,now_date,numbers,'mp4')
        else:
            jpg_url = j['image_versions2']['candidates'][0]['url']
            Timelimited_Download(jpg_url,now_date,numbers,'jpg')


def get_userID(username,cookies):
    url = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={username}'

    request = requests.get(url, headers={
        # 'cookie':'mid=WLsL4gAEAAGl0Wjoc8Dv6CH_iYnP; mcd=3; ds_user_id=1926542376; csrftoken=9aasLCq0vb2dUQWY9j1rjP11aejod1wS; sessionid=1926542376%3AG5zq9okSZhBxWx%3A8; ig_did=8675D711-4D34-4DBA-8751-F9E4E3B8FA63; shbid=17721; shbts=1602880097.7694821; rur=VLL; urlgen="{\"61.228.154.31\": 3462}:1kTWVn:7qfV2Cxf3rs1oZ9BUi45bNQ18T4',
        'cookie':cookies,
        'User-Agent':'Instagram 219.0.0.12.117 Android',
    })
    data = json.loads(request.text)
    user_id = data['data']['user']['id']
    return user_id

choose = int(input('請選擇需要哪些功能：\n1 - 只抓取貼文\n2 - 只抓取精選\n3 - 只抓限動\n4 - 我全部都要!\n請輸入1、2、3、4：'))
if choose == 1:
    try:
        igcrawler(input("請輸入要抓取的IG名稱："),cookies)
        input('請輸入任意鍵結束:')
    except:
        print('沒有貼文')
        input('請輸入任意鍵結束:')
elif choose == 2:
    try:
        username = input("請輸入要抓取的IG名稱：")
        userID = get_userID(username,cookies)
        crawler_highlight(userID,cookies)
        input('請輸入任意鍵結束:')
    except:
        print("沒有精選動態")
        input('請輸入任意鍵結束:')
elif choose == 3:
    try:
        username = input("請輸入要抓取的IG名稱：")
        userID = get_userID(username,cookies)
        crawler_Timelimited(userID,cookies)
        input('請輸入任意鍵結束:')
    except:
        print("沒有限時動態")
        input('請輸入任意鍵結束:')
elif choose == 4:
    username = input("請輸入要抓取的IG名稱：")
    userID = get_userID(username,cookies)
    try:
        igcrawler(input("請輸入要抓取的IG名稱："),cookies)
        input('請輸入任意鍵結束:')
    except:
        print('沒有貼文')
        input('請輸入任意鍵結束:')
    try:
        crawler_highlight(userID,cookies)
        input('請輸入任意鍵結束:')
    except:
        print("沒有精選動態")
        input('請輸入任意鍵結束:')
    try:
        crawler_Timelimited(userID,cookies)
        input('請輸入任意鍵結束:')
    except:
        print("沒有限時動態")
        input('請輸入任意鍵結束:')
    input('請輸入任意鍵結束:')
