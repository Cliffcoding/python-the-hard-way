from sys import argv
script, first, second, third = argv

first_input = input("What was the first argument? ")
second_input = input('What was ther second argument? ')
third_input = input('What was the third argument? ')


print(f'1: You entered {first_input} and the argument was {first}\n 2: You entered {second_input} and the argument was {second} \n 3: You entered {third_input} and the argument was {third}')
