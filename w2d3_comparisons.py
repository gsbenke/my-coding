# Part 1. Set Lists basics
print("Part 1.")
my_list = [1, 1, 5, 6, 7, 4]
my_set = set(my_list)

# Repeated items will only show once, all in order.
my_unique_list = list(my_set)
print(my_unique_list)

# Part 2. Color comparison 
print("Part 2.")
your_colors = {"red", "white", "orange", "blue"}
my_colors = {"red", "purple", "orange"}
their_colors = {"red", "orange", "brown", "purple", "blue"}

# Find colors in common between "your" + "my", using "intersection" function
our_colors = your_colors.intersection(my_colors)
print(our_colors)

# Part 3. Find colors in common for "your" + "my" + "their". 3 ways of coding:
print("Part 3.")
all_colors = your_colors.intersection(my_colors.intersection(their_colors))
print(all_colors)
all_colors2 = your_colors & my_colors & their_colors
print(all_colors2)
all_colors3 = your_colors.intersection(my_colors, their_colors)
print(all_colors3)

# Part 4. Using the "pipe", also known as "OR"
print("Part 4.")
combine_colors = my_colors | your_colors | their_colors
combine_colors2 = my_colors.union(your_colors, their_colors)


# Part 5. Tuple with a single item -> add a comma after the item
print("Part 5.")
my_tuple = ("Holden", )
print = type(my_tuple)


