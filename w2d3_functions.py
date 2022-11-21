# Functions

# Part 1. Simple function
def my_func():
    print("Hello")
my_func()

# Part 2. Returns values inside of the function
def my_func1(name):
    print(name)
my_func1("Mary")

def my_func2(firstname, lastname):
    print(firstname, lastname)
my_func2("Mary", "Teller")

def my_func3(*name):
    print(name)
my_func3("Robert", "Steph", "Will")

# Part 3. Adds numbers sequentially: 0+10 (=10), then +20 (=30), then +30 (=60)...
def add_numbers(*numbers):
    total = 0
    for number in numbers:
        total = total + number
        print(total)
    return total
add_numbers(10,20,30,40)

# Part 4. Keyword argument (key:value)
def list_properties(**car):
    input1 = car
    # Access only the maker (the "key" side), ignoring the "value" side
    print(f"This is a {car['maker']}")
    for i in car.items():
        print(i)
list_properties(maker = "Toyota", year = 2008, model = "Corolla", color = "White")

# Part 5. Name change. First it will show original name inside "func", then change it
def my_default_func(name = "William"):
    print(name)
my_default_func()
my_default_func("Rick")

# Part 6. Keyword arguments
def dic_maker(**kwargs):
    return kwargs
cars = dic_maker(maker = "Toyota", year = 2008, model = "Corolla", color = "White")

# Part 7. 
def morning():
    return "Good Morning"
def afternoon():
    return "Good Afternoon"
def greeter(time):
    if time == "sunrise":
        return morning()
    elif time == "sunset":
        return afternoon()
    else:
        return "Unknown time."
#greeter("sunset")
def greeter2(fn):
    print("Running Function")
    print(fn())
    print("Finished Running Function")
# Callback function
greeter2()