import random
print('Guessing game:')
list = [*range(0, 21, 1)]
number = int(input("Type a number from 1 to 20: "))
luck = random.choice(list)
correct = False

while correct == False:
    if number > 20:
        print('This number is out of range!')
    elif number < 1:
        print('This number is out of range!')
    elif number > luck and number < 21:
        print('Too high... ')
    elif number < luck and number > 0:
        print('Too low!')
    elif number == luck:
        correct = True
        print('WELL DONE! Correct number is {}!'.format(luck))
        break 
    
    number = int(input("Try again. Type a number from 1 to 20: "))



""" while correct == False:
    a = randint(1,10)
    c = int(input('Pick a number from 1 to 10: '))
if c > a:
    print('Too high... keep trying...')
elif c < a:
    print('Too low, try again!')
elif c == a:
    correct = True
    print('YES, YOU GOT IT!') """