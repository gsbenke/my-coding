# Amound will be given with 2 decimals, using ".2f"
usd = float(input('Please enter USD Conversion rate: '))
nzd = float(input('How many NZD you have? '))
cot = nzd/usd
print(f'You can get {cot:.2f} USD with that amount')