from Youtube.FilteringSearch.Enter_Driver import EnterDriver
# 상대경로로 불러오기

def ScrollSkipAds():
    import time
    driver = EnterDriver()

    # Scroll
    last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(3.0)
        new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_page_height == last_page_height:
            break
        last_page_height = new_page_height

    AllVideoList = driver.find_elements_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer')

    ### 필터링 광고창 넘어서 영상창으로 이동
    ### 필터링하면 상단에 광고가 생기는 경우가 있음.
    pageidx = 1
    for ad in range(5):
        contents = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer['+str(pageidx)+']/div[3]')
        renderer_list = contents.find_elements_by_tag_name("ytd-video-renderer")
        if len(renderer_list) < 2:
            pageidx += 1
        else:
            break
    return AllVideoList