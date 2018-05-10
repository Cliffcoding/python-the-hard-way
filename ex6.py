people_stuff = 10

x = f'Formatting is like magic, check out this stuff {people_stuff} it is cool.'

binary = 'binary'
do_not = 'don\'t'

y = f'Those who know {binary} those who {do_not}.'


print(x)
print(y)

print(f'I said: {x}')
print(f'I also said: {y}')
# This takes a string with an empty expression and then evaluates it with the .format
hilarious = False
truthy = True
joke_evaluation = 'Well that is so funny? {} {}'
print(joke_evaluation.format(hilarious, truthy))


w = 'This is a string one'

e = 'this is the second string'

print(w + e)
