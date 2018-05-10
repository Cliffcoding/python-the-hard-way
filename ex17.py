from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f'copying from {from_file} to {to_file}')

in_file = open(from_file).read()

print(f'The length of the input from {from_file} is {len(in_file)}')

print(f'Does the other file exist? {exists(to_file)}')

# print('Okay let\'s do this. Press return to continie or ctrl-c to quit')
# input()

out_file = open(to_file, 'w')
out_file.write(in_file)
print('Done did it.')
out_file.close()
