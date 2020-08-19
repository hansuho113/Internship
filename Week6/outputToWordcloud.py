import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize


df = pd.read_csv("output2.csv")

# Extract Column
tagCol = df["hashtag"].copy()
for i in range(len(tagCol)):
    processed = ' '.join(tagCol[i].split("', '"))
    tagCol[i] = processed[2:-2]

tagList = tagCol.tolist()   #len 1370


# Konlpy
# tfidf_vectorizer = TfidfVectorizer()
# tfidf_matrix_okt = tfidf_vectorizer.fit_transform(tagList)
# print(tagList)
eachTagList = []
for i in range(len(tagList)):
    words = tagList[i].split(' ')
    for word in words:
        eachTagList.append(word)
for i in range(len(eachTagList)):
    if '춘천여행' in eachTagList:
        eachTagList.remove('춘천여행')
for i in range(len(eachTagList)):
    if '춘천' in eachTagList:
        eachTagList.remove('춘천')
for i in range(len(eachTagList)):
    if '춘천맛집' in eachTagList:
        eachTagList.remove('춘천맛집')
for i in range(len(eachTagList)):
    if '춘천카페' in eachTagList:
        eachTagList.remove('춘천카페')
tagCount = Counter(eachTagList)
print(Counter(tagCount))
top100= tagCount.most_common(100)
words = dict(top100)


wordcloud = WordCloud(font_path = 'C:\\Program Files\\JetBrains\\PyCharm 2020.2\\jbr\\lib\\fonts\\D2CodingBold-Ver1.3.2-20180524-ligature.ttf',
                      background_color='white',colormap = "winter_r", width=1500, height=1000).generate_from_frequencies(words)
plt.figure(figsize=(10,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

# print(tagCount)

# eachTagList = []
# for i in range(len(tagList)):
#     eachTag = ', '.join(tagList[i].split(" "))
#     eachTagList.append(eachTag)
# print(eachTagList)
#
# tagCount = Counter(eachTagList)
# print(tagCount)

