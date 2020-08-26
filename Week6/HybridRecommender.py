import pandas as pd
import numpy as np
from ast import literal_eval

md = pd.read_csv("Dataset/movies_metadata.csv")

# dictionary안에 담겨있는 Genre 정보를 List 형태로 세팅
md['genres'] = md['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])

# 'release_date'를 split해서 year만 추출
md['year'] = pd.to_datetime(md['release_date'], errors='coerce').apply(lambda x: str(x).split('-')[0] if x != np.nan else np.nan)

links_small = pd.read_csv("links_small")
links_small = links_small[links_small['tmdbId'].notnull()]['tmdbId'].astype('int')

# outlier drop
md = md.drop([19730, 29503, 35587])
md['id'] = md['id'].astype('int')

# small dataset
smd = md[md['id'].isin(links_small)]

smd['tagline'] = smd['tagline'].fillna('')
smd['description'] = smd['overview'] + smd['tagline']
smd['description'] = smd['description'].fillna('')

def convert_int(x):
    try:
        return int(x)
    except:
        return np.nan

id_map = pd.read_csv('../input/links_small.csv')[['movieId', 'tmdbId']]
id_map['tmdbId'] = id_map['tmdbId'].apply(convert_int)
id_map.columns = ['movieId', 'id']
id_map = id_map.merge(smd[['title', 'id']], on='id').set_index('title')

indices_map = id_map.set_index('id')


def hybrid(userId, title):
    idx = indices[title]
    tmdbId = id_map.loc[title]['id']
    movie_id = id_map.loc[title]['movieId']

    sim_scores = list(enumerate(cosine_sim[int(idx)]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:26]
    movie_indices = [i[0] for i in sim_scores]

    movies = smd.iloc[movie_indices][['title', 'vote_count', 'vote_average', 'year', 'id']]
    movies['est'] = movies['id'].apply(lambda x: svd.predict(userId, indices_map.loc[x]['movieId']).est)
    movies = movies.sort_values('est', ascending=False)
    return movies.head(10)

hybrid(1, 'Avatar')