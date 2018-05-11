print('Practicing skills is good. Do it for \'merica the U, S of A')
print('backslash it all \\ backslash this \", oh what about that? \t tabbed out brah. Feels good')
print('\n got my new lines. \t and my tabs')


rhyme = ''' \tTab or dab?
Get this out the lab \n cause its super fab
scratching that beat like an itchy scab.
So here I stand and the whole point was...\n just use tab
\t out!
 '''
print(rhyme)

five = 10 - 2 + 3 - 6
print(five)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 500
    return jelly_beans, jars, crates

start_point = 10000
beans,jars,crates = secret_formula(start_point)

print('We started with: {}'.format(start_point))
print(f'We have {beans} jelly beans, in {jars} jars, that fit in {crates} crates')


start_point /= 10

formula = secret_formula(start_point)

print(formula)
print(f'So we would have {formula[0]} beans, {formula[1]} jars, {formula[2]} crates')
print('{} beans, {} jars, {} crates')
