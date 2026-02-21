import math

def unitPrice(diameter_cm, price):
    diameter_m = diameter_cm /100

    radius = diameter_m / 2

    area = math.pi * radius * radius

    price_per_s_meter = price / area

    return price_per_s_meter

diameter1 = float(input("Enter diameter of first pizza(cm): "))
price1 = float(input("Enter price of first pizza(euros): "))

diameter2 = float(input("\nEnter diameter of second pizza(cm): "))
price2 = float(input("Enter price of second pizza(euros): "))

unit1 = unitPrice(diameter1, price1)
unit2 = unitPrice(diameter2, price2)

print("\nUnit price of first pizza: ", unit1, "euors per square meter")
print("Unit price of second pizza: ", unit2, "euors per square meter")

if unit1 < unit2:
    print("The first pizza provides better value for money.")
elif unit2 < unit1:
    print("The second pizza provides better value for money.")    
else:
    print("Both pizzas have the same value for money")
