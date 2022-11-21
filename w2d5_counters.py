# Example 1. Count from number A to Z, jumping N numbers defined by you.
begin = int(input("First number: "))
end = int(input("Last number: "))
jump = int(input("Number jump: "))
for counter in range(begin, end+1, jump):
    print(counter)
print("Done.\n")

# Example 2. Ask user for 3 numbers, add them all, then print it.
adding = 0
for count in range (0, 3):
    n = int(input("Type a number "))
    adding += n
print("Sum of the above equals to {}.\n".format(adding))

# Example 3. Count from 10 to 1, adding sleep function for 1 second each time.
from time import sleep
for counter in range (11, 1, -1):
    counter = counter-1 
    print(counter)
    sleep(1)
print("Boom!")

# Example 4. Ask user to enter number, then show numbers before and after.
numb = int(input("Type an integer number: "))
print("Your number ({}) is in between {} and {}.".format(numb, numb-1, numb+1))


