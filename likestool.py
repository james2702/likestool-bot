# LikesTool Bot Auther: James Adams License: MIT
# Modules
import os
import time
from splinter import Browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configuration
likestool_email = "your_likestool_user_here"
likestool_password = "Your_likestool_password_here"

google_email = "Your_google_email_here"
google_password = "Your_google_email_password"

instagram_username = "your_instagram_user"
instagram_password = "Your_instagram_password"

actions_per_module = "20"

chrome_options = Options()
chrome_options.add_extension('ublock_origin.crx')

total_points = "0"

# Chrome Driver
browser = Browser('chrome', options=chrome_options)
os.system('cls' if os.name == 'nt' else 'clear')
print("Welcome to LikesTool Bot")
print("auther James Adams")
print("license MIT")
print("[+] Starting...")
print("[+] Importing Modules...")

# Google Account Login
print("[+] Logging in Google...")
browser.visit("https://www.youtube.com/account")
browser.find_by_xpath("//*[@id='identifierId']").fill(google_email)
browser.find_by_xpath("//*[@id='identifierNext']").click()
time.sleep(3)
browser.find_by_xpath("//*[@id='password']/div[1]/div/div[1]/input").fill(google_password)
browser.find_by_xpath("//*[@id='passwordNext']").click()
time.sleep(5)

# Instagram Login
print("[+] Loggin in Instagram...")
browser.visit("https://www.instagram.com/accounts/login/?source=auth_switcher")
time.sleep(5)
browser.find_by_name("username").fill(instagram_username)
browser.find_by_name("password").fill(instagram_password)
browser.find_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button").click()
time.sleep(5)

# Likestool Login
print("[+] Loggin in KingdomLikes...")
browser.visit("https://likestool.com/site/login")
browser.find_by_xpath("//*[@id='input-1']").fill(likestool_email)
browser.find_by_xpath("//*[@id='input-2']").fill(likestool_password)
browser.find_by_xpath("//*[@id='login_form']/div[4]/input").click()
time.sleep(7)

# YouTube Views
print("[+] Starting YouTube Views...")
for x in range(0, int(actions_per_module)):
    browser.visit("https://likestool.com/campaign/YOUTUBE_VIEWS")
    time.sleep(5)
    browser.find_by_xpath("//*[@id='campaign-container']/div[1]/div/div[2]/a").click()
    time.sleep(50)
    points = browser.find_by_css('#coins').text
    print("[+] You earned " + points + "points...")
    total_points = total_points + points

# YouTube likes
print("[+] Starting YouTube Likes...")
for x in range(0, int(15)):
    browser.visit("https://likestool.com/campaign/YOUTUBE_VIDEO_LIKES")
    time.sleep(5)
    browser.find_by_xpath("//*[@id='campaign-container']/div[1]/div/div/a").click()
    browser.windows.current = browser.windows[1]
    time.sleep(5)
    browser.find_by_xpath("//*[@id='top-level-buttons']/ytd-toggle-button-renderer[1]/a").click()
    time.sleep(5)
    browser.windows.current = browser.windows[0]
    time.sleep(30)
    points = browser.find_by_css("#coins").text
    print("[+] You earned " + points + "points...")
    total_points = total_points + points

# YouTube Subscribers
print("[+] Starting YouTube Subscribers...")
for x in range(0, int(10)):
    browser.visit("https://likestool.com/campaign/YOUTUBE_SUBSCRIBE")
    time.sleep(5)
    browser.find_by_xpath("//*[@id='campaign-container']/div[1]/div/div/a").click()
    browser.windows.current = browser.windows[1]
    time.sleep(5)
    browser.find_by_xpath("//*[@id='subscribe-button']").click()
    time.sleep(5)
    browser.windows.current = browser.windows[0]
    time.sleep(30)
    points = browser.find_by_css("#coins").text
    print("[+] You earned " + points + " points...")
    total_points = total_points + points

# Dailymotion Views
print("[+] Starting YouTube Views...")
for x in range(0, int(actions_per_module)):
    browser.visit("https://likestool.com/campaign/DAILYMOTION_VIEWS")
    time.sleep(5)
    browser.find_by_xpath("//*[@id='campaign-container']/div[1]/div/div[2]/a").click()
    browser.windows.current = browser.windows[1]
    browser.execute_script("document.getElementsById('dmp_Video')[0].pause();")
    browser.windows.current = browser.windows[0]
    time.sleep(47)
    points = browser.find_by_css('#coins').text
    print("[+] You earned " + points + "points...")
    total_points = total_points + points

# Instagram Followers
print("[+] Starting Instagram Followers...")
for x in range(0, int(15)):
    browser.visit("https://likestool.com/campaign/INSTAGRAM_FOLLOWERS")
    time.sleep(5)
    browser.find_by_xpath("//*[@id='campaign-container']/div[1]/div/div/a").click()
    browser.windows.current = browser.windows[1]
    time.sleep(5)
    browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/span/span[1]/button").click()
    time.sleep(5)
    browser.windows.current = browser.windows[0]
    time.sleep(30)
    points = browser.find_by_class_css("#coins").text
    print("[+] You earned " + points + " points...")
    total_points = total_points + points

# Instagram likes
print("[+] Starting Instagram Likes...")
for x in range(0, int(15)):
    browser.visit("https://likestool.com/campaign/INSTAGRAM_LIKES")
    time.sleep(5)
    browser.find_by_xpath("//*[@id='campaign-container']/div[1]/div/div/a").click()
    browser.windows.current = browser.windows[1]
    time.sleep(5)
    browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/article/div[2]/section[1]/span[1]/button").click()
    time.sleep(5)
    browser.windows.current = browser.windows[0]
    time.sleep(30)
    points = browser.find_by_css("#coins").text
    print("[+] You earned " + points + " points...")
    total_points = total_points + points

# Soundcloud Views
print("[+] Starting YouTube Views...")
for x in range(0, int(actions_per_module)):
    browser.visit("https://likestool.com/campaign/SOUNDCLOUD_LISTEN")
    time.sleep(5)
    browser.find_by_xpath("//*[@id='campaign-container']/div[1]/div/div/a").click()
    time.sleep(40)
    points = browser.find_by_css('#coins').text
    print("[+] You earned " + points + "points...")
    total_points = total_points + points
print("Total Points Earned: " + total_points)