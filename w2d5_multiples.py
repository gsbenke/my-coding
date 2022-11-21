# Sum odd numbers from 1 to 500
abc = 0
counter = 1
for n in range (1, 501, 2):
    if n % 3 == 0:
    abc += n
    counter += 1
print(f"Sum of {counter} is {abc}")

