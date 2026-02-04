number = input("Enter a number (Press enter to quit): ")

if number == "":
    print("No numbers entered.")
else:
    number = float(number)
    min = number
    max = number

    while True:
        userInput = input("Enter a number (press Enter to quit): ")

        if userInput == "":
            break

        number = float(userInput)

        if number < min:
            min = number

        if number > max:
            max = number

    print("Smallest number:", min)
    print("Largest number:", max)


