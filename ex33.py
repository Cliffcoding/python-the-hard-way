i = 0
numbers = []

while i < 100:
    print(f'At {i}')
    numbers.append(i)
    i +=1
    print(f'numbers is now {numbers}')

for num in numbers:
    print(num)
