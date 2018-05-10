
def print_two(*args):
    arg1, arg2 = args
    print(f'arg1: {arg1}, arg2: {arg2}')

def print_two_again(arg1, arg2):
    print(f'arg1: {arg1}, arg2: {arg2}')

def print_one(arg):
    print(f'The arg is: {arg}')

def print_none():
    print('No args. sad face')



print_two_again('Me', 'Maaa')
print_two('he', 'saw')
print_one('she')
print_none()
