def gallonsToLiters(gallons):
    liters = gallons * 3.785
    return liters

while True:
    gallons = float(input("Enter gasoline amount in gallons(negative value to quit): "))

    if gallons < 0:
        print("Program ended.")
        break

    liters = gallonsToLiters(gallons)
    print("Liters:", liters)