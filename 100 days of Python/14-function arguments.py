# def average(a=1,b=9):
#     print("The average is:",(a+b)/2)

# # average(10,20)    
# average(b=5)
# def name(fname,mname="john",lname="watson"):
#     print("hello",fname,mname,lname)

# name("amy","fawad")



def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("average is :",sum/len(numbers))    