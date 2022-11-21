# items_purchased = ['milk','bread','eggs', ['apples','chicken'], 'soap'] 
# items_purchased.extend(['bananas','cereal',]) 
# items_purchased.insert(0, 'oranges') 
# extra_items = items_purchased[4] 
# essential_items = items_purchased.copy() 
# essential_items.pop(4) 

shopping_list = ["milk", "bread", "eggs", "soap", "butter", "apple", "chicken"]
items_needed = shopping_list[0].capitalize()
shopping_list.extend(["banana","cereal"])
items_forgotten = shopping_list
new_list = [item.capitalize() for item in shopping_list ]
print("This is your current Shopping List: ")
print(new_list)
var = "N"
while (var == "N"):
        var = input('Are you happy with your list (Y/N)? ')
        shopping_list
if var == ("Y"):
    print(f"Here is your final list: {new_list}")
else: 
    var == ("N")
    print("Ok, we will start again.")


