def Inventory(userInput):
    answer = int(input("What Size?"))    
    red = [28, 30, 32, 28, 34, 28, 40]
    blue = [40, 42, 44, 44, 38, 42, 40]
    jeans_colour = [red, blue]
    #thing = jeans_colour[0][0]
    #redCount = jeans_colour[0].count(28)
    #blueCount = jeans_colour[1].count(44)
    all_combined = jeans_colour[0].count(answer) + jeans_colour[1].count(answer)
    return all_combined
answer = int(input("What size would you like? (Between 28-44)"))
result = Inventory(answer)
print("There are " + str(result) + " pairs of jeans of size " + str(answer))