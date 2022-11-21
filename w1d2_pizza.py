welcome = ('Welcome to AWS Pizza!')
print(welcome)
var = "N"
while (var == "N"):
    size = input('What size would you like? ')
    if size == 'Large':
        print('Great choice!')
    else:
        print('Got it!')
    base = input('What base would you like? ')
    if base == 'Classic':
        print('It is our best-seller, you will love it!')
    else:
        print('Got it!')
    topping = input('What flavour would you like? ')
    if topping == 'Avocado':
        print('Sorry! We are all out. ')
        topping = input('Please choose another flavour: ' )
    else:
        print('No worries')
    print('Please confirm your order:')
    print(size)
    print(base)
    print(topping)
    var = input('Is this correct (Y/N)? ')
    if var == ("Y"):
        print('Thank you! It will be ready in 10 minutes.')
    else: 
        var == ("N")
        print("Ok, we will start again.")
