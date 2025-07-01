# f=open('practice.py')
# text=f.read()
# print(text)
# f.close()



# f=open('txt1.py','x')
# text=open('txt1.py','a')
# text.write("Hey I am FAWAD")
# text.close()

# f=open("txt1.py","r")
# print (f.read())


# f = open("txt1", "a")
# f.write("Now the file has more content!")
# f.close()

# #open and read the file after the appending:
# f = open("txt1", "r")
# print(f.read())

# import os
# if os.path.exists("txt2"):
#   os.remove("txt2")
# else:
#   print('The file doesnot exist') 
# 
# 
#  
# f=open('txt2.py','r')
# i=0
# while True:
#     i=i+1
#     line=f.readline()
#     if not line:
#         break
#     m1=line.split(",")[0]
#     m2=line.split(",")[1]
#     m3=line.split(",")[2]
#     print(f"Marks of student {i} in Maths is {m1}")
#     print(f"Marks of student {i} in English is {m2}")
#     print(f"Marks of student {i} in OOP is {m3}")
#     print(line)



# f=open('txt3','w')
# lines=['line 1\n','line 2\n','line 3\n']
# f.truncate(5)
# f.writelines(lines)
# f.close()



# with open('txt3','r')as f:
#     f.seek(5)
#     print(f.tell())
#     data=f.read(5)
# print(data)