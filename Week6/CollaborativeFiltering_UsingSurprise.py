

from surprise import Reader, Dataset, SVD, accuracy
import pandas as pd
from surprise.model_selection import KFold
reader = Reader()

# Read DataSet
ratings = pd.read_csv("Dataset/ratings_small.csv")

data = Dataset.load_from_df(ratings[['userId', 'attractionId','rating']], reader)
algo = SVD()

trainset = data.build_full_trainset()
testset = trainset.build_testset()
algo.fit(trainset)

temp = ratings[ratings['userId'] == 1]

a = algo.predict(1, 2968, 2)
df = pd.DataFrame(a).T
df.columns = ['User Id', 'Attraction Id', 'Actual Rating', 'Predicted Rating','etc']
df.index = ['Recommendation']
df_partial = df[['User Id', 'Attraction Id', 'Actual Rating', 'Predicted Rating']]

print(temp)
print(df_partial)

# predict(uid, iid, r_ui=None, clip=True, verbose=False)
# uid – (Raw) id of the user.
# iid – (Raw) id of the item.
# r_ui (float) – The true rating rui
    # 실제 매겨진 평점이 있을 경우 주는 파라미터.
    # 즉 1번이 110번에 3점을 줬는데, 이것의 예측 평점을 구하면 r_ui는 3이고 est 값에 따라 추천 여부를 판단
