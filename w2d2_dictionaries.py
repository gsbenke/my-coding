# Dictionaries (list of 2 things at a time). Format is -> Key:value
my_dict = {
    "Person1" : 50, 
    "Person2" : 100, 
    "Person3" : 44
}
# Part 1. Print dictionary, followed by data type
print("-> Part 1.")
print(my_dict)
print(type(my_dict))

# Part 2. Print keys, then below print values
print("-> Part 2.")
for key in my_dict.keys():
    print(key)
for value in my_dict.values():
    print(value)

# Part 3. Tuple unpacking Example. Two ways of printing the same info
print("-> Part 3.")
for item in my_dict.items():
    print(item)
    print(f"{item[0]} is {item[1]}")
    key, value = item
    print(f"{key} is {value}")

# Part 4. Tuple unpacking. Print 1st keythen , 1st value, then 2nd, 3rd etc
print("-> Part 4.")
for key, value in my_dict.items():
    print(key)
    print(value)

# Part 5.
print("-> Part 5.")

