from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os 
from DownloadChromedriver import get_chromedriver
import time
import requests
import json

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # 全螢幕
options.add_argument("--disable-notifications")  # 關閉通知

if not os.path.exists("chromedriver.exe"):
    get_chromedriver('139.0.7258.128')


def scroll_to_bottom(driver, pause_time=2):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def Getcomunity():
    time.sleep(2) # 等待2秒
    # 全部社團
    scroll_to_bottom(driver)
    comunity = driver.find_element('xpath','/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div[3]')
    comunity_list = comunity.find_elements(By.TAG_NAME, 'a')
    groups = {}
    for i in comunity_list:
        comunity_name = i.text
        comunity_url = i.get_attribute('href')
        if '查看社團' not in comunity_name:
            groups[comunity_url] = comunity_name
    with open('groups.txt', 'w', encoding='utf-8') as f:
        f.write(f"總社團數量: {len(groups)}\n")
        for url, name in groups.items():
            f.write(f"{name} : {url}\n")


def FristLogin_getCookie():
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
    FristLogin_getCookie()
else:
    with open('cookies.json', 'r', encoding='utf-8') as f:
        cookies_1 = json.load(f)
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.facebook.com/")
    for name, value in cookies_1.items():
        driver.add_cookie({'name': name, 'value': value})
    driver.refresh()
    time.sleep(2)
    driver.get("https://www.facebook.com/groups/joins/?nav_source=tab&ordering=viewer_added")
    Getcomunity()
    input("Cookies have been loaded. Press Enter to continue...")

    


