from sys import argv

script, filename1 = argv

print(f'We are going to erase {filename1}')
print('If you did not want to Erase press control-c')
print('If you did want to erase the file, press Return')

input('? ')


print('Opening the file...')
target = open(filename1, 'w')

print('Truncating the file. Hasta La vista... Baby!')
# target.truncate()

print('Now spit me three bars')

line1=input('Line 1: ')
line2=input('Line 2: ')
line3=input('Line 3: ')

print('Lets see that fire in action.')

target.write(f'''
{line1}
{line2}
{line3}
''')
# target.write('\n')
# target.write(line2)
# target.write('\n')
# target.write(line3)

target.close()
new_target = open(filename1)
print(new_target.read())
print('now lets get that on the radio')
new_target.close()
