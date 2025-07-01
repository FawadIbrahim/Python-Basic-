# colors=["Red","Green","Blue","Yellow"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)

# for k in range(0,10,2):
#     print(k+1)



# ui=int(input("Enter the number: "))

# for i in range (1,11):
#     print(f"{ui} X {i} = {ui * i}")




'''number guess game
'''
# import random

# pick=random.randint(1,100)

# attempt=0
# while True:
#   user=int(input("Enter a guess: "))
#   attempt += 1

#   if pick==user:
#     print("Your guess is correct")
#     break
#   elif pick>user:
#     print("Your guess low")
#   else:
#     print("Your Guess is high")


'''even or odd'''
# User=int(input("Enter the number: "))

# if User%2 ==0:
#     print('even')
# else:
#     print('odd')

'''Calculator'''
# num1=int(input('Enter the first number: '))
# num2=int(input('Enter the second number: '))

# print('What type of calculation do you want "+","-","* or "/": ')
# oper=input('Enter the operator: ')
# reuse=0



# if oper=='+':
#     print(f'The answer is {num1 + num2}')
# elif oper=='-':
#     print(f'The answer is {num1 - num2}')
# elif oper=='*':
#     print(f'The answer is {num1 * num2}')
# elif oper=='/':
#     print(f'The answer is {num1 / num2}')
# else:
#     print('Invalid operator ')

'''Monthly spend calculator'''
# rent=int(input("Enter the rent of Flat/Room: "))
# total_food_order = 0
# while True:
#     food_input = input("Enter the amount of a food order (or type 'done' if finished): ")
#     if food_input.lower() == 'done':
#         break
#     try:
#         food_amount = int(food_input)
#         total_food_order += food_amount
#     except ValueError:
#         print("Invalid input. Please enter a number or 'done'.")
# ele_bill=int(input("Enter the unit spent: "))
# ele_unit=int(input("Enter the price of unit: "))
# persons=int(input("Enter the number of person living in Flat/Room: "))



# total_ele_bill=ele_bill*ele_unit
# output=(rent + total_food_order + total_ele_bill)/persons
# print(f'Per person will pay: {output}')
    
'''rock paper scissor
'''
import random
choice_list=['Rock','Paper','Scissor']
user_input=input('Enter the choice from the list "Rock , Paper , Scissor":')
comp_choice=random.choice(choice_list)

print(f'Your choice={user_input} and computer choice={comp_choice}')

if user_input==comp_choice:
    print("Both chooses same so match is tie")
elif user_input=='Rock':
    if comp_choice=='Paper':
        print('Paper covers the rock : Computer wins')
    else:
        print('Rock Smashes the Scissor')
elif user_input=='Paper':
    if comp_choice=='Scissor':
        print('Scissor cuts the Paper : Computer wins')
    else:
        print('Paper covers the rock : You win')
elif user_input=='Scissor':
    if comp_choice=='Paper':
        print('Scissor cuts the Paper : Computer wins')
    else:
        print('Rock Smashes the Scissor')






