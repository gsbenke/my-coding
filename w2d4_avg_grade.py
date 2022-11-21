# Check your 1st and 2nd semester grades, giving your average.  
n1 = float(input("Type your first semester grade: "))
n2 = float(input("Type your second semester grade: "))
avg = (n1 + n2)/2

# Result with 1 decimal
print("Your average was {:.1f}".format(avg))

# If statement for each average
if 7 > avg >= 5:
    print("You will require a Catch-up Test.")
elif avg < 5:
    print("You have failed this year.")
elif avg >= 7:
    print("Well done! You are approved." )