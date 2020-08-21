import pandas as pd
from selenium import webdriver
import time
import tqdm
import pandas as pd

url_str = "https://www.tripadvisor.co.kr/Attraction_Review-g608520-d597358-Reviews"
url_num = str(0)
url_keyword = "-Nami_Island-Chuncheon_Gangwon_do.html"
total_url = url_str + url_num + url_keyword

driver = webdriver.Chrome("C:\\Users\\Rectworks\\PycharmProjects\\chromedriver\\chromedriver.exe")
driver.get(total_url)
# driver.maximize_window()
time.sleep(3)

review_dict = {}

reviewNum = 1
for i in range(2):
    print(i)
    review_window = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[9]/div/div[2]/div/div/div[3]/div")
    reviews = review_window.find_elements_by_css_selector('.Dq9MAugU.T870kzTX.LnVzGwUB')  ## 공백은 클래스가 여러 개 있다는 거임.

    reviews[0].find_element_by_class_name("XUVJZtom").click()  # 리뷰 더보기 클릭

    for review in reviews:  # reviews 는 한 페이지에 있는 리뷰 다섯 개
        content = review.find_element_by_class_name("IRsGHoPm").text
        rating = review.find_element_by_css_selector(".ui_bubble_rating").get_attribute("class")
        rating = rating[-2:]
        review_dict[reviewNum] = {"content": content, "rating": rating}
        reviewNum += 1
    driver.find_element_by_css_selector(".ui_button.nav.next.primary").click()   # 페이지 다음 버튼 클릭
    time.sleep(0.5)

df = pd.DataFrame.from_dict(review_dict)
print(df.T)
'''
pageNumbers Class 는 span -a -a -a  혹은 2페이지라면 a -span -a -a 의 형태로 이루어져있기 때문에
span.text (번호 출력) 번째의  a를 click해주면 됨
'''


# for pageNum in pages:
#     print(pageNum.text)



df = pd.DataFrame.from_dict(review_dict)
# print(df)





'''
review = reviews[0].find_element_by_class_name("IRsGHoPm")
rating = reviews[0].find_element_by_css_selector(".ui_bubble_rating").get_attribute("class")
    # class="ui_bubble_rating bubble_50" 클래스 중간 공백은 클래스가 두 개로 분리돼있다는 것으로 이해하고 get_attribute로 class 가져옴
    # class끝이 평점에 따라서 숫자가 바뀌므로 공백으로 분리된 클래스 앞의 것을 잡아와서 전체 클래스명을 불러오는 과정
'''

