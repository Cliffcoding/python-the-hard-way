print('How old are you?', end=' ')
age=input()
print('How much do you weigh?', end=' ')
weight=int(input())
print('How tall are you?', end=' ')
height=input()
kilo= round(weight * 0.4535924)
print(f'So you are {age}, weigh {kilo} kilograms, and {height} tall')