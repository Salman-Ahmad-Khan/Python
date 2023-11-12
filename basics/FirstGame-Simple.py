import random
generatedNumber = random.randrange(1, 10)
userGuess = int(input("Guess the number in the range 1-10:\n"))
if userGuess == generatedNumber:
    print("You have got it right!")
elif userGuess<generatedNumber:
    print("Your guess is too low")
else:
    print('Your guess is too high')

