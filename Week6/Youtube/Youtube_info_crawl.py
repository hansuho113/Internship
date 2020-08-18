#Reference  https://shinminyong.tistory.com/2?category=835486
# https://medium.com/@quangnhatnguyenle/how-to-train-yolov3-on-google-colab-to-detect-custom-objects-e-g-gun-detection-d3a1ee43eda1


# Import Library
import requests
from bs4 import BeautifulSoup
import time
import urllib.request
from selenium.webdriver import Chrome
import re
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import datetime as dt

path = "C:\\Users\\Rectworks\\PycharmProjects\\chromedriver\\chromedriver.exe"
delay = 3
browser = Chrome(path)
browser.implicitly_wait(delay)

start_url = "https://www.youtube.com"
browser.get(start_url)
# browser.maximize_window()

browser.find_elements_by_xpath('//*[@id="search-input"]')[0].click()
browser.find_element_by_xpath('//*[@id="search-form"]/div/div/div/div[2]/input').send_keys("Keyword")
browser.find_element_by_xpath('//*[@id="search-form"]/div/div/div/div[2]/input').send_keys(Keys.RETURN)

# 필터 버튼 클릭
browser.find_element_by_xpath('//*[@id="container"]/ytd-toggle-button-renderer/a').click()

# 필터 기준 - 업로드 날짜 - 오늘
upload_date = browser.find_element_by_xpath('//*[@id="collapse-content"]/ytd-search-filter-group-renderer[1]')
click_list_1 = upload_date.find_elements_by_id("endpoint")
click_list_1[1].click()

# 필터 창이 내려가는 속도에 맞추기 위해서 임의로 sleep한 후에 버튼 클릭
time.sleep(delay)
browser.find_element_by_xpath('//*[@id="container"]/ytd-toggle-button-renderer/a').click()

# 필터 기준 - 정렬 기준 - 조회수
sorting_std = browser.find_element_by_xpath('//*[@id="collapse-content"]/ytd-search-filter-group-renderer[5]')
click_list_5 = sorting_std.find_elements_by_id("endpoint")
click_list_5[2].click()
time.sleep(delay)

url = browser.current_url
req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')
print(soup)
all_videos = soup.find_all(id='dismissable')
# print(all_videos)
title_list = []
for video in all_videos:
    title = video.find(id='video-title')
    print(title)
    # if len(title.text.strip()) > 0 :
    #     title_list.append(title.text)


print(len(title_list))
print(title_list)

