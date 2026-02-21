import random

count = int(input("How many times do you want to roll? "))

rolls = []

for i in range(count):
    dice = random.randint(1, 6)
    rolls.append(dice)

total = sum(rolls)

print("Dice rolls: ", rolls)
print("Sum of the numbers: ", total)