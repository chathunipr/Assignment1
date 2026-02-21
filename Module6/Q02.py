import random

def rollDice(sides):
    return random.randint(1, sides)

sides = int(input("Enter the number of sides on the dice: "))

result = 0

while result != sides:
    result = rollDice(sides)
    print("Dice roll:", result)