# Imports the argument variable from the system module
from sys import argv
# variable names for the arguments passed into the script. The first argument is the script ran.
script, filename = argv
# turns the file into an an object
txt = open(filename)
# Prints the current file
print(f'Here is your filename: {filename}')
# Reads the file object and interprets it.
print(txt.read())
# # Enter a new filename
# print('Type the filename again:')
# file_again = input('> ')
#
# txt_again = open(file_again)
#
# print(txt_again.read())
txt.close()
