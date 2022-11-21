# Part 1. Print list and class type down below
print("Part 1.")
myFruitList = ["apple", "pear", "strawberry", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

# Part 2. Pick items from list. Syntax examples: position 0 (first one) then position 3 (fourth item)
print("Part 2.")
print(f"First item is: {myFruitList[0]}")
print(myFruitList[3])

# Part 3. Changing list. Example: changing item at position 2 (third item), then print revised list
print("Part 3.")
myFruitList[2] = "persimmon"
print(myFruitList)

# Part 4. Tuples are immutable Lists. Use () for tuples, instead of []
print("Part 4.")
myFruitTuple = ("apple", "pear", "strawberry", "banana", "cherry")
print(myFruitTuple)
print(type(myFruitTuple))
