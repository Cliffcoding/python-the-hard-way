def add(num1, num2):
    print(f'adding: {num1} + {num2}')
    return num1 + num2

def subtract(num1, num2):
    print(f' subtracting: {num1} - {num2}')
    return num1 - num2

def multiply(num1, num2):
    print(f'Multiplying: {num1} * {num2}')
    return num1 * num2

def divide(num1, num2):
    print(f'Dividing: {num1} / {num2}')
    return num1 / num2

age = multiply(5, 5)
height = subtract(70, 1)
weight = add(125, 110)

print(f'I am {age}, {height} inches tall and {weight} pounds')
