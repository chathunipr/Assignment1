import random

def rollDice():
    return random.randint(1, 6)

result = 0

while result != 6:
    result = rollDice()
    print("Dice roll:", result)