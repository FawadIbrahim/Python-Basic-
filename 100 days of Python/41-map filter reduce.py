# def cube(x):
#     return x*x*x
# print (cube(2))
# l=[1,2,3,4,5]
# # newlist=[]
# # for item in l:
# #     newlist.append(cube(item))
# newlist=list(map(cube,l))
# print (newlist)

# def filter_1(a):
#     return a>2
# newlist2=list(filter(filter_1, l))
# print(newlist2)

import functools
list=[1,2,3,4,5,6,7,8]
newlist=functools.reduce(lambda x,y: x+y , list)
print(newlist)
print("The maximun value of the list is : ",)    
print(functools.reduce(lambda a, b: a if a > b else b, list))

