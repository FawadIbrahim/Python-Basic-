# a = input("Enter the number: ")
# print(f"Multiplication table of {a} is: ")
# try:
#   for i in range(1, 11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
# except:
#   print("Invalid  Input!")

# print("Some imp lines of code")
# print("End of program")

try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
    
except IndexError:
 print("Index Error")
# i=0
# while(i<=100):
#     print(i)
#     i+= 1


# a=input("enter a number:")
# print(f"Multiplication of {a} is:")
# for i in range (1,11):
#     print(f"{int(a)}x{i}={int(a)*i}")

# e1=['fawad','sameer','kamran','shamo','vigo']
# e2=[]
# for name in e1:
#     if 'a' in name:
#         e2.append(name)

# print(e2)