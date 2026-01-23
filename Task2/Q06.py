import random

firstCode = ""
for i in range(3):
    num = random.randint(0, 9)
    firstCode = firstCode + str(num)

secondCode = ""
for i in range(4):
    num = random.randint(1, 6)
    secondCode = secondCode + str(num)

print("3-digit combination code is: ", firstCode)    
print("4-digit combination code is: ", secondCode)