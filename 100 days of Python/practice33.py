# l1=['fawad','sameer','ali','shami', 'maaz']
# l1.sort()
# print(l1)
# l1.reverse()
# print(l1)
# l1.insert(2,'zain')
# print(l1)
# l1=('fawad','sameer','ali','shami', 'maaz')
# i=l1.index('sameer')
# print(i)



# fr=[]

# f1=input('Enter the fruit 1')
# fr.append(f1)
# f2=input('Enter the fruit 2')
# fr.append(f2)
# f3=input('Enter the fruit 3')
# fr.append(f3)
# f4=input('Enter the fruit 4')
# fr.append(f4)

# print(fr)

# marks=[]

# f1=int(input('Enter marks 1:'))
# marks.append(f1)
# f2=int(input('Enter the marks 2:'))
# marks.append(f2)
# f3=int(input('Enter the marks 3:'))
# marks.append(f3)
# f4=int(input('Enter the marks 4:'))
# marks.append(f4)

# marks.sort()

# print(marks)



# i=1
# while (i<51):
#     print(i)
#     i += 1

# li=['fawad','harry',]





# print(movies.head(5))
# print(movies.info())
# print(movies['title'])
# print(movies.columns)
# movies=movies.drop(['original_language', 'popularity', 'release_date', 'vote_average', 'vote_count'], axis=1)
# movies=movies['title']+'-'+movies['overview']
# print(movies)



import pandas as pd

# pd.options.display.max_rows = 999


df=pd.read_csv('data.csv')
print(df.corr())
# df.loc[7, 'Duration']=45
# df.drop_duplicates(inplace=True)
# print (df.info())

# print(df)










