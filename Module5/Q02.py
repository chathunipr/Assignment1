num = []

while True:
    user_input = input("Enter a number (Press enter to stop): ")

    if user_input == "":
        break

    number = float(user_input)
    num.append(number)

num.sort(reverse=True)

print("The five greatest numbers are: ")

topFive = num[:5]

for n in topFive:
    print(n)