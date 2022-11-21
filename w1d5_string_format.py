name = "judas" 
hobby1 = "Pottering and Yoga"
hobby2 = "Poledancing into a Pit"

print("Hello " + name + ", your interests are " + hobby1 + ".")

# First name letter in capital, hobbies fully capitalized
print(f"Hello {name.capitalize()}, your interests are {hobby1.upper()} and {hobby2.lower()}\n")

# Output/Formatting exercise
you = input("Your name? ")
color = input("Pick a color: ")
animal = input("Pick an animal: ")

# Multiple variables to format a string
print("{}, how about a {} {}?".format(you,color,animal))

hobby1 = "Pottering and Yoga"

# Print long text with multiple lines -> add 3x" on begin and end of text
print("""Long text here, 
long text here 
etc etc""") 

# Exercises: Print specific parts of a string

print(hobby1[0:10]) # Print from character 0 to 9
print(hobby1[0:10:3]) # Print from character 0 to 9, but only show every 3 characters
print(hobby1.upper()) # Print whole string in Caps
print(hobby1.lower()) # print whole string in Lower case 
print(len(hobby1)) # Print number of characters on the string, including spaces of course

# Sentence "Pottering and Yoga" will save a list with 3 separate words
sentence = hobby1.split() 
# Print the above list defined as "sentence"
print(sentence) 

print(sentence[2][0]) # Print a specific character from a word - Example below is 3rd word 1st character.
print("Yoga" in hobby1) # Check if the word Yoga is part of the string (answer is True/False)
hobby1 = print(hobby1.replace("Yoga", "MMA")) # Replace word Yoga for MMA

