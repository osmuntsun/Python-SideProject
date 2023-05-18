import json
import requests
import os
import traceback
import datetime
import time

req = requests.Session()
def create_threads(titles,Videos,watchs,Videos_url,keyword_ID,keyword_all_name,quarterly,keyword='語風'):
    # 設定 Discord Webhook URL
    webhook_url = f"It's My Discord Forum Channel Webhook URL"

    bot_token = 'It's My Discord bot token'
    now = datetime.datetime.now().strftime(f'%Y-%m-%d %H:%M:%S')
    message_now = datetime.datetime.now().strftime(f'%Y-%m-%d')
    # 建立 payload
    if len(f"{quarterly}/{keyword_all_name} ({message_now}) - BotUpdate") > 100 :
        name_test=f"{quarterly}/{keyword_all_name} ({message_now}) - BotUpdate"
        names = name_test[:100]
        payload = {
            'message':{
            #內文
            "content": f'---BotUpdate--- \n\n 標題：{titles} \n\n 影片時間：{Videos} \n\n 在 {now} 擷取時 \n\n {watchs} \n\n {Videos_url}'
            },
            'auto_archive_duration':4320,
            'name':names, #標題
            'applied_tags':[keyword_ID], # 標籤
            }
    else:
        payload = {
            'message':{
            #內文
            "content": f'---BotUpdate---\n\n 標題：{titles} \n\n 影片時間：{Videos} \n\n 在 {now} 擷取時 \n\n {watchs} \n\n {Videos_url}'
            },
            'auto_archive_duration':4320,
            'name':f"{quarterly}/{keyword_all_name} ({message_now}) - BotUpdate",#標題
            'applied_tags':[keyword_ID],# 標籤
            }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bot {bot_token}"
    }
    json_payload = json.dumps(payload)
    # 發送 POST 請求

    response = req.post(webhook_url,json=payload,headers = headers)
    # 檢查是否成功
    if response.status_code == 204 or response.status_code == 201 or response.status_code == 200:
        print("已成功傳送資料至 Discord。")
        now = datetime.datetime.now().strftime(f'%Y-%m-%d %H:%M')
        with open('./Reportdata.txt','a',encoding="utf-8-sig") as data:
            data.write('-'*90)
            data.write(f'\n{now}有新的文章!\n')
            print(f"目前版本：{quarterly}")
    else:
        print(f"傳送資料至 Discord 失敗。{response.status_code}")
        print(f"目前版本：{quarterly}")

def Get_channel_ID(youtube_user_name):
    search_url  = 'It's My Youtube search URL'

    payload = {'It's My Youtube payload'}
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
        if keyword == 'None' or keyword == None:
            keyword_ID = Tag_ID['影片']
            create_threads(titles,Videos,watchs,Videos_url,keyword_ID,keyword_all_name,quarterly,keyword) 
        else:
            for i in tag_profession:
                print(keyword in i)
                if keyword in i :
                    keyword = tag_profession[tag_profession.index(i)]
                    keyword_ID = [Tag_ID[keyword],Tag_ID['影片']]
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
        if '➧' in titles:
            for i in titles.split('➧')[1][:-1]:
                text_str = titles.split('➧')[1][:-1]
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
        else:
            keyword_all_name = titles
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
        return None,None,None,None,None,None,None

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
            data.write(f'\n{Channelname}\n{now}並無PO新的文章!\n')
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
                if '安靜貓' in json_data:
                    print("4123asdf")
                    quarterly = json_data['安靜貓']['quarterly']


    yt_url = 'It's My Youtube date URL'

    payload = {
        'It's My payload search URL'
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


