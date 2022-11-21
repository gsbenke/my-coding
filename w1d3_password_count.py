attempts_left = 3
while True:
    if attempts_left > 0:
        password = input("Please enter your password ")
        if password == "abc123":
            print("Welcome")
        else:
            print("Incorrect password, attempts remaining: " + str(attempts_left))
            attempts_left = attempts_left - 1
    else:
        print("No more attempts, you are locked out")
        break

while attempts_left > 0:
    password = input("Please enter your password ")
    if password == "abc123":
        print("Welcome")
    else:
        print("Incorrect password, attempts remaining: " + str(attempts_left))
        attempts_left = attempts_left - 1
        if attempts_left == 0:
            print("No more attempts, you are locked out")
            break