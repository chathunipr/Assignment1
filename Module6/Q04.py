def sumOfList(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total

myNum = [5, 10, 15, 20]

result = sumOfList(myNum)
print("The sum of the numbers is:", result)