correctUser = "chathunp"
correctPass = "1234"

attempts = 0

while attempts < 5:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correctUser and password == correctPass:
        print("Welcome !")
        break
    else:
        print("Incorrect username or password. Please try again")
        attempts += 1
        print(5 - attempts, "Attempts left")
if attempts == 5:
    print("Access denied")        