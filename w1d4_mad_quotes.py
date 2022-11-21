# Return function - Math calculation for Cube
def cube(num):
    return num*num*num
    # No other code can be written after "Return". For example, cannot print on this line.
print("Example 1 - Calculator: Return Cube")
val = input('Please enter a number: ')
result = cube(float(val))
print(result)

# Mad Quotes - User enters a verb and 3 quotes show up.
print("Example 2 - Mad Quotes")
verb = input("Enter a verb with ING ending: ")
print("Quote 1. Each mistake teaches us " + verb + " better")
print("Quote 2. The great pleasure in " + verb + " is doing what people say you cannot do.")
print("Quote 3. Being loved gives you strength, while " + verb + " someone gives you courage.")


# While Loop with Time Count
print("Example 3 - 1 to 10 Count slowed down by 3s Timer")
import time
i = 1
while i <= 10:
    time.sleep(3)
    print(i)
    i +=1
print("Count completed. Loading next Example...")

# 



