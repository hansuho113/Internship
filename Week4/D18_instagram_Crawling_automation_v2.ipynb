### Import Library

import pandas as pd
import numpy as np

import selenium
from selenium import webdriver

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen, Request
from urllib.parse import quote_plus

import time
from datetime import datetime

import warnings
warnings.filterwarnings('ignore')

from urllib.error import HTTPError

SCROLL_PAUSE_TIME = 2.0

post_link = []
popularPost_len = []   # 검색어마다 다른 인기게시물 개수를 담은 리스트, 대부분 9개
id_list = []
like_list = []
tag_list = []
link_list = []
date_list = []
month_list = []
day_list = []

### Login
def instagram_login(id, pw):
    driver.get(url)
    driver.implicitly_wait(5)
    driver.find_element_by_name('username').send_keys(id)  # id 입력
    elem_pw = driver.find_element_by_name('password')  # pw 입력
    elem_pw.send_keys(pw)
    elem_pw.submit()

    driver.implicitly_wait(5)  # 파싱될 때까지 5초 기다림 (미리 완료되면 waiting 종료됨)
    driver.find_element_by_class_name('cmbtv').click()  # 비밀번호 저장하지 않음

    driver.implicitly_wait(5)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()  # 알림설정 무시


### Search
def main_search(keyword):
    search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    search.clear()
    search.send_keys(keyword)
    search_list1 = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]')
    search_list1.click()

### To tiemstamp
def to_timestamp(std_date):
    date_string = std_date
    date =datetime.strptime(date_string, "%Y.%m.%d %H:%M")
    time_tuple = date.timetuple()
    std_timestamp = time.mktime(time_tuple)
    return int(std_timestamp)

### popularPostSum
def popularPostSum():
    popularPost = 0
    for i in range(3):
        popularPost += popularPost_len[i]
    return popularPost

### Scroll Page and post link Crawling
def scroll_crawling(date1, date2):
    post_link.clear()
    popularPost_len.clear()    # 이전 작업기록이 남아있을 수 있으므로 clear해줌
    timestamp_1 = to_timestamp(date1)
    timestamp_2 = to_timestamp(date2)   # 크롤링된 게시물과의 날짜 비교를 위해서 기준날짜 설정
    periods = range(int(timestamp_1), int(timestamp_2))  # 크롤링 기간 설정
    start = time.time()
    while True:
        pageString = driver.page_source
        bsObj = bs(pageString, 'lxml')

        temp_postlink = []
        for postline in bsObj.find_all(name='div', attrs={"class":"Nnq7C weEfm"}):
            a_len = len(postline.select('a'))
            popularPost_len.append(a_len)
            # 인스타그램 게시물은 행별로 최대 3개까지 확인할 수 있는데, 최근게시물이나 마지막 게시물은 1,2개가 나올 수도 있어서 len 지정
            for post in range(a_len):
                item = postline.select('a')[post]
                link = item.attrs['href']
                if link not in post_link:   # 스크롤을 내리고 중복된 것을 제거하지 않고 누적시키기 때문에 없는 것만 추가
                    post_link.append(link)
                    temp_postlink.append(link)
        count = len(temp_postlink)

        break_point = True
        for i in range(count):
            req = Request("https://www.instagram.com" + temp_postlink[i], headers={'User-Agent': 'Mozila/5.0'})
            try:
                postpage = urlopen(req).read()
            except HTTPError:
                pass
            post_body = bs(postpage, 'lxml', from_encoding='utf-8')
            post_core = post_body.find('meta', attrs={'property': "og:description"})
            contents = post_core['content']

            posttxt = str(postpage)
            timestamp = int(posttxt[posttxt.find('taken_at_timestamp')+20 : posttxt.find('taken_at_timestamp')+30])

            if timestamp in periods:
                # 시간
                date_list.append(datetime.fromtimestamp(timestamp).strftime('%Y.%m.%d %H:%M'))
                month_list.append(datetime.fromtimestamp(timestamp).strftime("%m"))
                day_list.append(datetime.fromtimestamp(timestamp).strftime("%d"))

                # 개별 링크 리스트
                link_list.append("https://www.instagram.com" + temp_postlink[i])

                # 좋아요
                try:
                    likes = int(contents[: contents.find(' Likes, ')])  # Likes 문자열 앞에 있는 좋아요 개수 추출
                except:
                    likes = 0  # 좋아요 가 아니라 조회수로 표시되는 경우도 있어 이런 경우는 0으로 표시
                like_list.append(likes)

                # 개별 계정
                if "@" and ")" in contents:
                    personal_id = contents[contents.find("@") + 1: contents.find(")")]
                elif "shared a post on Instagram" in contents:
                    personal_id = contents[contents.find("@") + 1: contents.find('shared a post on Instagram')]
                elif "shared a photo on Instagram" in contents:
                    personal_id = contents[contents.find("@") + 1: contents.find('shared a photo on Instagram')]
                elif "@" and ")" not in contents and "on Instagram" in contents:
                    personal_id = contents[contents.find("@") + 1: contents.find('on Instagram')]
                else:
                    personal_id = contents[1: contents.find(' posted on')]
                id_list.append(personal_id)
                '''    
                (@personal_id) on instagram, @persoanlid posted on instagram, personal_id on instgram 등의 형태로 meta 데이터에 표시되기
                때문에 여러 형식별 id 추출 if문 수행
                '''
                # 해시태그
                tag_list.append([])
                for tag_content in post_body.find_all('meta', attrs={'property': "instapp:hashtags"}):
                    hashtags = tag_content['content'].rstrip(',')
                    tag_list[-1].append(hashtags)
            else:
                count -= 1
                if count == 0:
                    print(time.time() - start)
                    break_point = False
                    break
        if break_point == False:
            break

        last_height = driver.execute_script('return document.body.scrollHeight')  # 자바스크림트로 스크롤 길이를 넘겨줌
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # selenium에서 scroll 기능 사용
        time.sleep(SCROLL_PAUSE_TIME)
        # 프로세스 자체를 지정시간동안 기다려줌(무조건 지연)
        # driver.implicitly_wait(SCROLL_PAUSE_TIME)
        # 브라우저 엔진에서 파싱되는 시간을 기다려줌(요소가 존재하면 지연없이 코드 실행)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)
            # driver.implicitly_wait(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")

            if new_height == last_height:
                break
            else:
                last_height = new_height
                continue

### DataFrame
def To_df():
    insta_dict = {'날짜':date_list,'월':month_list,'일':day_list,'계정':id_list,
          '좋아요':like_list,'해시태그':tag_list,'링크':link_list}
    df = pd.DataFrame(insta_dict)
    return print(df)

### DataFrame Sorting
def sorted_df(column):
    insta_dict = {'date':date_list,'month':month_list,'day':day_list,'id':id_list,
          'likes':like_list,'hashtag':tag_list,'link':link_list}
    df = pd.DataFrame(insta_dict)
    sorted_df = df.sort_values(by=[column], axis=0, ascending=False)
    print(sorted_df)




def all(id, pw, kwd, sorting,date1,latest_date2 = (datetime.now()).strftime("%Y.%m.%d %H:%M")):
    ### Basic Setting

    ID = id
    PW = pw
    if latest_date2 == '':
        latest_date2 = (datetime.now()).strftime("%Y.%m.%d %H:%M")
    instagram_login(ID, PW)
    main_search(kwd)

    scroll_crawling(date1, latest_date2)
    sorted_df(sorting)

if __name__ == "__main__":
    id = input("ID : ")
    pw = input("PW : ")
    kwd = input("Keyword : ")
    sorting = input("Sorting Criterion(date, likes) : ")
    date1 = input("End date [format(YYYY.mm.dd HH:MM)] : ")
    latest_date2 = input("Start data [To start 'Crawling' from now, just press enter]: ")

    url = 'http://www.instagram.com'
    path = 'C:\\Users\\rectworks\\Downloads\\chromedriver_win32\\chromedriver.exe'
    driver = webdriver.Chrome(path)
    all(id, pw, kwd, sorting, date1, latest_date2)
