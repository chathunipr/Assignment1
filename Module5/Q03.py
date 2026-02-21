num = int(input("Enter an integer: "))

if num <= 1:
    print(num, "is not a prime number.")
else:
    isPrime = True

    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break

    if isPrime:
        print(num, "is a prime number.")

    else:
        print(num, "is not a prime number.")
