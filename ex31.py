print('''You hear some voices, was that someone laughing? You come up on two doorsself.
You have to pick one. Do you pick door 1 or 2?''')

door = input('> ')

if door == '1':
    print(''' There is a clown turned away from you rocking in a chair.
You notice a sign with a flashing exit sign to the right of him.
Do you:
    1. Book it to the exit sign?
    2. Tell your best dad joke to him?''')
    clown = input('> ')

    if clown == '1':
        print('You make it to the door but he notices and drags you into the creepy closet. GAME OVER!')
    elif clown == '2':
        print('''The clown laughs for a second then it gets really quiet.
You notice a creepy smile and his eyes turning red. POP POP POP and away he takes you. GAME OVER!''')
    else:
        print('DUN DUN DUUUUUUUN. You broke the game. Robot kills you')
elif door == '2':
    print('''The room is pitch black and you can't see anything.
Do you:
    1. Go to the left?
    2. Go to the right?''')
    direction = input('> ')
    if direction == '1' or direction == 'left':
        print('You start walking for what feels like forever. You come across a red figure. As you get closer. It notices you and runs away. As you walk closer it reveals itself and takes you through the fiery gates of hell. GAME OVER!')
    elif direction == '2' or direction =='right':
        print('You start to fall. There is no catching yourself now. You are stuck in free fall. Under the map where no man escapes. GAME OVER!')
    else:
        print('error. You died')
else:
    print('Your mistakes actually paid off. You win')
