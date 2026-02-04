import random

secretNum = random.randint(1,100)

theGuess = 0

print("Let's Play a Game. Guess a number between 1 and 100")
while theGuess != secretNum:
    guess = int(input("Keep Guessing: "))

    if guess > secretNum:
        print("Too High, Try one more time")
    elif guess < secretNum:
        print("Too Low, Try one more time")
    else:
        print("Congratulations! You are right")