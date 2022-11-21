# Shuffle list of 5 people 

from random import shuffle
n1 = str(input("Person #1: "))
n2 = str(input("Person #2: "))
n3 = str(input("Person #3: "))
n4 = str(input("Person #4: "))
n5 = str(input("Person #5: "))
name_list = [n1, n2, n3, n4, n5]
shuffle(name_list)
print("These were randomized as:") 
print(name_list)
