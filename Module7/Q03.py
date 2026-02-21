airports = {}

while True: 
    print("Choose an option: ")
    print("1 - Enter a new airport")
    print("2 - Enter a new airport")
    print("3 - Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        icao = input("Enter ICAO code: ").upper()
        name = input("Enter airport name: ")
        airports[icao] = name
        print("Airport added.")

    elif choice == "2":
        icao = input("Enter ICAO code: ").upper()

        if icao in airports:
            print("Airport name: ", airports[icao])
        else:
            print("Airport not found.")

    elif choice == "3":
        print("Program ended")
        break

    else:
        print("Invalid choice. Try again.")                    