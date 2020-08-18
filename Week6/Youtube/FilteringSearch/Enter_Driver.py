def EnterDriver():
    import time
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    kwd = input("검색 키워드 :")
    filter1 = int(input("{ 0: 지난 1시간, 1: 오늘, 2: 이번 주, 3: 이번 달, 4: 올해 } :"))
    filter2 = int(input("{ 0: 관련성, 1: 업로드 날짜, 2: 조회수, 3: 평점 } :"))

    driver_path = "C:\\Users\\Rectworks\\PycharmProjects\\chromedriver\\chromedriver.exe"
    driver = webdriver.Chrome(driver_path)
    driver.implicitly_wait(5)  # or bigger second

    start_url = "https://www.youtube.com"
    driver.get(start_url)
    # browser.maximize_window()

    driver.find_elements_by_xpath('//*[@id="search-input"]')[0].click()
    driver.find_element_by_xpath('//*[@id="search-form"]/div/div/div/div[2]/input').send_keys(kwd)
    driver.find_element_by_xpath('//*[@id="search-form"]/div/div/div/div[2]/input').send_keys(Keys.RETURN)

    # 필터 버튼 클릭
    driver.find_element_by_xpath('//*[@id="container"]/ytd-toggle-button-renderer/a').click()

    # 필터 기준 - 업로드 날짜 - 오늘
    upload_date = driver.find_element_by_xpath('//*[@id="collapse-content"]/ytd-search-filter-group-renderer[1]')
    click_list_1 = upload_date.find_elements_by_id("endpoint")
    click_list_1[filter1].click()

    # 필터 창이 내려가는 속도에 맞추기 위해서 임의로 sleep한 후에 버튼 클릭
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="container"]/ytd-toggle-button-renderer/a').click()

    # 필터 기준 - 정렬 기준 - 조회수
    sorting_std = driver.find_element_by_xpath('//*[@id="collapse-content"]/ytd-search-filter-group-renderer[5]')
    click_list_5 = sorting_std.find_elements_by_id("endpoint")
    click_list_5[filter2].click()
    time.sleep(2)
    return driver