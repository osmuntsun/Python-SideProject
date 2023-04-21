# -*- encoding: utf8-*-
import requests
import json
import pandas as pd
import time 
import random
import urllib.parse
import chardet


def google_comment(session):
    url = 'https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&pb=!1m2!1y3588323880321333309!2y6218714981998367227!2m1!2i10!3e2!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1sX9c0ZOW2Opbp-AbHvpzACw!7e81'

    '''
    3e1 = 最相關
    3e2 = 最新
    3e3 = 評分最高
    3e4 = 評分最低
    '''
    params = {
        'authuser': '0',
        'hl': 'zh-TW',
        'gl': 'tw',
        'pb': '!1m2!1y3588323880321333309!2y6218714981998367227!2m1!2i10!3e2!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1snTUuZPrGJZOe-Abii5KYBA!7e81'
    }

    responses = session.get(url,params=params)

    # 刪除掉前綴詞
    data =''.join(list(responses.text)).lstrip(")]}'")
    data = json.loads(data)

    name = []
    text = []
    star = []
    next_pages = []
    n = 0
    for i in data[2]:
        n+=1
        if len(i)-1 == 61:
            text.append(i[3])
            star.append(i[4])
            name.append(i[0][1])
            next_pages.append(i[61])
        else:
            text.append(i[3])
            star.append(i[4])
            name.append(i[0][1])
            next_pages.append('None')

    
    if next_pages[-1] != 'None':
        next_pages_bool=True
        page_id = next_pages[-1]
        while next_pages_bool==True:
            print(next_pages[-1])
            random_number = random.randint(1, 5)
            time.sleep(random_number)
            star,text,name,next_pages_bool,next_pages,n = next_page(star,text,name,next_pages,page_id,n)
            page_id = next_pages[-1]
            next_pages_bool = next_pages_bool


    print(next_pages)

    return star,name , text


def next_page(star,text,name,next_pages,i,n):
    url = f'https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&pb=!1m2!1y3588323880321333309!2y6218714981998367227!2m2!2i10!3s{i}!3e2!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1sX9c0ZOW2Opbp-AbHvpzACw!7e81'
    params = {
        'authuser': 0,
        'hl': 'zh-TW',
        'gl': 'tw',
    }

    responses = session.get(url,params=params)

    # 刪除掉前綴詞
    data =''.join(list(responses.text)).lstrip(")]}'")
    data = json.loads(data)


    for i in data[2]:
        if n != 100:
            n+=1
            if len(i)-1 == 61:
                text.append(i[3])
                star.append(i[4])
                name.append(i[0][1])
                next_pages.append(i[61])
            else:
                text.append(i[3])
                star.append(i[4])
                name.append(i[0][1])
                next_pages.append('None')
        else:
            break


    next_pages_bool =True
    if n != 100:
        if next_pages[-1] != 'None':
            next_pages_bool =True
        else:
            next_pages_bool =False
    else:
        next_pages_bool =False
    
    
    return star,text,name,next_pages_bool,next_pages,n


session = requests.Session()
star,name,text = google_comment(session)

df = pd.DataFrame()
df['評論者名稱'] = name
df['星級'] = star
df['評論'] = text

df.to_csv('./最新評論.csv',index=False,encoding='utf-8-sig')


