# a=303
# b=3303
# print("a") if a>b else print("=") if a==b else print("b")
# c=9 if a<b else 0
# print(c)


# a=('mango','apple','banana')
# b=list(a)
# b.remove('apple')
# a=tuple(b)
# print(a)



# a=('mango','apple','banana')
# b=('kiwi',)
# a+=b
# print(a)


# colors={
#     'cl1' : 'red',
#     'cl2' : 'blue',
#     'cl3' :  'green',

# }
# a=colors.values()
# print(a)
# colors['cl4']='white'
# print(a)


# colors={
#     'cl1 :' : 'red',
#     'cl2 :' : 'blue',
#     'cl3 :' :  'green',

# }
# for x, y in colors.items():
#     print(x, y)
# sf ={
#     'fruit1':{
#         'Name':'mango',
#         'Date':'7 to 1',
#         'Month':'4 to 6',

#     },
#     'fruit2':{
#         'name':'Watermelon',
#         'Date':'1 to 2',
#         'Month':'4 to 6',
#     } 
# }
# print(sf['fruit1']['Date'])


import math
a=int(input('Enter the valve of A: '))
b=int(input('Enter the valve of B: '))
c=int(input('Enter the valve of C: '))

def qe(a,b,c):
    for1=b**2-4*a*c
    if for1>0:
        root1=(-b+math.sqrt(for1)) /(2*a)
        root2=(-b-math.sqrt(for1)) / (2*a)
        return(root1,root2)
    elif for1==0:
        root=-b/(2*a)
        return(root,)
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-for1) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return (root1, root2)
roots = qe(a, b, c)
print("The roots of the quadratic equation are:", roots)
