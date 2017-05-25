#!/usr/bin/python3
#coding:utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
#下面填入京东的用户名以及密码
jd_up={"ue":"****","pd":"****"}

opts = Options()
opts.add_argument("--user-data-dir=C:\Users\mushhi\AppData\Local\Google\Chrome\User Data\Default")#load user data
prefs = {"profile.managed_default_content_settings.images":2} # this will disable image loading in the browser
opts.add_experimental_option("prefs",prefs)  # Added preference into chrome options
opts.add_argument("user-agent="'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')
#added chrome option user-agent
chrome = webdriver.Chrome('chromedriver.exe',chrome_options=opts) # finally add these option as startup option for Google Chrome
chrome.get(url="https://passport.jd.com/new/login.aspx?")
chrome.find_element_by_xpath("//*[@id=\"content\"]/div/div[1]/div/div[2]/a").click()
User=chrome.find_element_by_id("loginname")
User.clear()
User.send_keys(jd_up["ue"])
Passwd=chrome.find_element_by_id("nloginpwd")
Passwd.clear()
Passwd.send_keys(jd_up["pd"])
chrome.find_element_by_id("loginsubmit").click()
while True:
    try:
        chrome.get(url="https://item.jd.com/4099139.html")
        chrome.find_element_by_id("choose-btn-ko").click()
        chrome.find_element_by_id("order-submit").click()
        print("抢购成功并且已下单！！")
        chrome.quit()
    except Exception:
        print("还未开始抢购！！")
        time_stamp = datetime.datetime.now()
        print "现在时间       " + time_stamp.strftime('%Y.%m.%d-%H:%M:%S')
