from Youtube.FilteringSearch.Scroll_SkipAds import ScrollSkipAds
def ToDataframe():
    import pandas as pd
    channel_list = []
    title_list = []
    viewCnt_list = []
    time_list = []

    AllVideoList = ScrollSkipAds()

    renderer_lists = []
    for i in range(len(AllVideoList)):
        renderers = AllVideoList[i].find_elements_by_tag_name("ytd-video-renderer")
        renderer_lists.append(renderers)

    for i in range(len(AllVideoList)):
        for video in range(len(renderer_lists[i])):
            video_title = renderer_lists[i][video].find_element_by_id("video-title").text
            channel_id = renderer_lists[i][video].find_element_by_id("text").text
            metatxt = renderer_lists[i][video].find_element_by_id("metadata-line").text
            viewCnt = metatxt[:metatxt.find("\n")]
            date = metatxt[metatxt.find("\n") + 1:]

            channel_list.append(channel_id)
            time_list.append(date)
            viewCnt_list.append(viewCnt)
            title_list.append(video_title)

    youtube_dict = {'채널':channel_list,
                  '조회수':viewCnt_list,
                  '시간':time_list,
                 '제목':title_list}

    df = pd.DataFrame(youtube_dict)
    print(df)