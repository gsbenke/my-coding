# Base converter

num = int(input("Type an integer number: "))
print('''Choose which base you would like to convert to: 
[1] Binary  [2] Octal  [3] Hexadecimal''')
opt = int(input("You selected: "))

# Note [2:] to avoid "0x" prefix  
if opt == 1:
    print("-> {} converted to Binary is {}".format(num, bin(num)[2:]))
elif opt == 2:
    print("-> {} converted to Octal is {}".format(num, oct(num)[2:]))
elif opt == 3:
    print("-> {} converted to Hex is {}".format(num, hex(num)[2:]))
else:
    print("Invalid option, please try again.") 