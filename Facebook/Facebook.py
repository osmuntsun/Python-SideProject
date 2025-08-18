from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os 
from DownloadChromedriver import get_chromedriver
import time
import requests
import json


if not os.path.exists("chromedriver.exe"):
    get_chromedriver('139.0.7258.128')

def FristLogin():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/?locale=zh_TW")
    # 登入帳號
    element = driver.find_element('xpath','//*[@id="email"]')
    element.send_keys('osmuntsun900606@gmail.com') # 輸入帳號
    element = driver.find_element('xpath','//*[@id="pass"]')
    element.send_keys('osmunt900606') # 輸入密碼

    time.sleep(2) # 等待2秒
    driver.find_element('xpath','/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click() # 點擊登入按鈕
    WebDriverWait(driver, 50000).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div'))
    )
    cookie = driver.get_cookies() # 獲取cookies
    with open('cookies.txt', 'w') as f: # 將cookies寫入文件
        for c in cookie:
            f.write(f"{c['name']}={c['value']}; \n")
    print("Cookies have been saved to cookies.txt")
    cookies_key = ['datr', 'sb', 'dpr', 'locale', 'c_user', 'xs', 'fr', 'wd', 'presence']

    cookies_1 = {}
    for c in cookie:
        if c['name'] in cookies_key:
            cookies_1[c['name']] = c['value'] # 指定cookies的名稱和值

    with open('cookies.json', 'w', encoding='utf-8') as f:
        json.dump(cookies_1, f, ensure_ascii=False, indent=4)





if not os.path.exists("cookies.json"):
    FristLogin()
else:
    with open('cookies.json', 'r', encoding='utf-8') as f:
        cookies_1 = json.load(f)
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")
    for name, value in cookies_1.items():
        driver.add_cookie({'name': name, 'value': value})
    driver.refresh()
    input("Cookies have been loaded. Press Enter to continue...")

    


