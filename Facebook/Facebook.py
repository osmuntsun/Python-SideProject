from selenium import webdriver
import os 
from DownloadChromedriver import get_chromedriver
import time
import requests


if not os.path.exists("chromedriver.exe"):
    get_chromedriver('139.0.7258.128')


driver = webdriver.Chrome()
driver.get("https://www.facebook.com/?locale=zh_TW")
# 登入帳號
element = driver.find_element('xpath','//*[@id="email"]')
element.send_keys('osmuntsun900606@gmail.com') # 輸入帳號
element = driver.find_element('xpath','//*[@id="pass"]')
element.send_keys('osmunt900606') # 輸入密碼

time.sleep(2) # 等待2秒
driver.find_element('xpath','/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click() # 點擊登入按鈕

input("請按Enter鍵繼續...") # 等待使用者按Enter鍵

cookie = driver.get_cookies() # 獲取cookies
print(cookie) # 打印cookies
with open('cookies.txt', 'w') as f: # 將cookies寫入文件
    for c in cookie:
        f.write(f"{c['name']}={c['value']}; ")


cookie_names = [
    "datr", "sb", "dpr", "locale", "ps_l", "ps_n", "c_user", "xs", "fr", "presence", "wd"
]

with open("cookies.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# 合併所有 cookie 字串
cookie_str = "".join(lines).replace("\n", "").replace("\r", "")

# 解析成 dict
cookie_dict = {}
for item in cookie_str.split(";"):
    item = item.strip()
    if "=" in item:
        k, v = item.split("=", 1)
        cookie_dict[k.strip()] = v.strip()

# 按指定順序組合
result = []
for name in cookie_names:
    if name in cookie_dict:
        result.append(f"{name}={cookie_dict[name]}")

final_cookie = "; ".join(result)
print(final_cookie)

'''
datr= 'value': 'UeWhaFwAEjstko2t1smwhO7g'
sb= 'value': 'UeWhaDoLoyGTVClbad8Udd_j'
xs= 'value': '15%3ALhx23MrGqEeS6A%3A2%3A1755440689%3A-1%3A-1'

datr=MPuhaDhKwXKUJA8oUX3e1pJk; sb=MPuhaMtmPpiCiNUnK2uR3rUe; dpr=1.25; locale=zh_TW; ps_l=1; ps_n=1; c_user=100001035739008; xs=14%3AATv4StKkQMqeGg%3A2%3A1755446280%3A-1%3A-1; fr=0avWJNzkh86n5ktow.AWfZmZlOT-wShHnZWIYd2-ZKM_Jy1deYwe9LWpaNkxYqNSxaI9Y.Boofsw..AAA.0.0.BoofwL.AWdSggjE7YlhoXXd7qdyNfyzl2E; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1755446286366%2C%22v%22%3A1%7D; wd=482x651
'''

input("請按Enter鍵繼續...") # 等待使用者按Enter鍵


