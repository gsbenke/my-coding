# Payment calculator with Afterpay, Interest or Discount

# Cash payment = 10% discount
# Debit Card = Standard price
# Afterpay = Standard price in 3 installments
# Credit Card = 20% interest with user input for X installments 

# Format Receipt 
print("{:=^40}".format(" SHOE STORE Receipt "))
price = float(input("->>> Total: NZD "))
print(''' Choose how you would like to pay:
[1] Cash
[2] Debit Card
[3] Afterpay Fortnightly
[4] Credit Card (20pc interest)''')
opt = int(input("Enter your choice: "))

if opt == 1:
    total = price - (price * 10 /100)
elif opt == 2:
    total = price 
elif opt == 3:
    total = price
    partials = total / 3
    print("Only pay ${:.2f} today + 2 more fortnighly installments.".format(partials))
elif opt ==4:
    total = price + (price * 20/100)
    tt_partials = int(input("How many installments? "))   
    partials = total / tt_partials 
    print("You will pay in {} installments of ${:.2f} each.".format(tt_partials, partials))
else:
    print("Invalid option, sorry. Try again.")
print("== TOTAL ${:.2f} ==".format(total))
