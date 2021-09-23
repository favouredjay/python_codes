import random

number = int(input("Guess my number between 1 and 1000"))

correct_number = random.randrange(1, 1000)
while number != 0:
    if number != correct_number:
        if number > correct_number:
            print("Number is too big")
        elif number < correct_number:
            print("Number is too low")
    else:
        print("Congratulations, You guessed the right number")
