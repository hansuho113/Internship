# reference : https://somjang.tistory.com/entry/PythonSelenium%EC%9D%84-%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC-%EC%9C%A0%ED%8A%9C%EB%B8%8C-%EB%8C%93%EA%B8%80-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0



from selenium import webdriver as wd
from bs4 import BeautifulSoup
import time
import pandas as pd

path = "C:\\Users\\rectworks\\PycharmProjects\\chromedriver_win32\\chromedriver.exe"
driver = wd.Chrome(path)

url = "https://www.youtube.com/watch?v=5SKQJpk1oXE"
driver.get(url)

last_page_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(3.0)
    new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_page_height == last_page_height:
        break
    last_page_height = new_page_height
html_source = driver.page_source
# driver.close()
soup = BeautifulSoup(html_source, 'lxml')
youtube_user_IDs = soup.select('div#header-author > a > span')
youtube_comments = soup.select('yt-formatted-string#content-text')
str_youtube_userIDs = []
str_youtube_comments = []
for i in range(len(youtube_user_IDs)):
    str_tmp = str(youtube_user_IDs[i].text)
    # print(str_tmp)
    str_tmp = str_tmp.replace('\n', '')
    str_tmp = str_tmp.replace('\t', '')
    str_tmp = str_tmp.replace(' ','')
    str_youtube_userIDs.append(str_tmp)
    str_tmp = str(youtube_comments[i].text)
    str_tmp = str_tmp.replace('\n', '')
    str_tmp = str_tmp.replace('\t', '')
    str_tmp = str_tmp.replace(' ', '')
    str_youtube_comments.append(str_tmp)
for i in range(len(str_youtube_userIDs)):
    # print(str_youtube_userIDs[i], str_youtube_comments[i])
pd_data = {"ID":str_youtube_userIDs, "Comment":str_youtube_comments}
youtube_pd = pd.DataFrame(pd_data)
youtube_pd