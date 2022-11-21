# This is a list with different types of data -> string, float, integer and boolean

myMixedList = [33.3, True, False, "Sentence", 10, "Forty"]
print("-> Part 1.")
print(myMixedList)
print(" ")
print("-> Part 2.")
for item in myMixedList:
    print("{} is data type {}".format(item,type(item)))

