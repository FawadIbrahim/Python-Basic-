import pandas as pd

# pd.options.display.max_rows = 9999

movies=pd.read_csv('dataset.csv')
# print(movies.head())
# print(movies)
# print(movies.describe())
# print(movies['id'].head())
# print(movies[['id','title']].head())
# print(movies.iloc[0])
# print(movies.dropna())
# print(movies.fillna(0))
# print(movies.rename(columns={"vote_average":'VA',"vote_count":'VC'}))
movies=movies.drop(['original_language', 'popularity', 'release_date', 'vote_average', 'vote_count'], axis=1)
movies=movies['title']+'_'+movies['overview']
# print(movies.info())

