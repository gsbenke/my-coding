# Math chart - Two ways of achieving the same result.
# Example 1
n1 = int(input('Welcome to Math Chart! Type a number from 1 to 10: '))
print(f'Multiplication chart for number {n1} is: ')
print(f'{n1} x 1 = {n1 * 1}')
print(f'{n1} x 2 = {n1 * 2}')
print(f'{n1} x 3 = {n1 * 3}')
print(f'{n1} x 4 = {n1 * 4}')
print(f'{n1} x 5 = {n1 * 5}')
print(f'{n1} x 6 = {n1 * 6}')
print(f'{n1} x 7 = {n1 * 7}')
print(f'{n1} x 8 = {n1 * 8}')
print(f'{n1} x 9 = {n1 * 9}')
print(f'{n1} x 10 = {n1 * 10}')
print('Done!')

# Example 2
z = int(input('Multiplication chart: '))
for a in range(z, z+1):
    print('--'*5)
    for b in range(1, 11):
        print('{}X{} = {}'.format(a, b, (a*b)))
print('--'*5)

