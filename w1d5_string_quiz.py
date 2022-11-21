# Ask user for a number from 0 to 9999, then show each digit separately in each line

number = str(input("Please enter number from 0 to 9999 -> ")).strip()
num = f"{number:0>4}"
print(num)
print(f"\n First digit: {num[3]} \n Second digit: {num[2]} \n Third digit: {num[1]} \n Fourth digit: {num[0]}")
