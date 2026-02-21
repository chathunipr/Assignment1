def removeOddNum(numbers):
    evenNum = []

    for num in numbers:
        if num % 2 == 0:
            evenNum.append(num)

    return evenNum

original = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new = removeOddNum(original)

print("Original list: ", original)
print("List without odd numbers: ", new)