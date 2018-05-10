tester= 'String test'
formatter= '{} {} {} {} {}'

print(formatter.format(tester, 4, 6, 8, ' '))
print(formatter.format(formatter,formatter,formatter,formatter,formatter))
print(formatter.format(
    'Can I use diffent types here?',
    True,
    'And numbers as well?',
    15,
    not 15
))
