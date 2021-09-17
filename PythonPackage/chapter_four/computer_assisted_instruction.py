import random

correct_answer = 0
wrong_answer = 0


def random_number_generator():
    global correct_answer, wrong_answer
    first_number = random.randrange(1, 10, 1)
    second_number = random.randint(1, 10)
    result = first_number * second_number
    for random_counter in range(1, 11):
        print(first_number, "*", second_number)
        answer = int(input("input answer"))
        if answer == result:
            print("Correct")
            correct_answer +=1
        else:
            print("Not Correct")
            wrong_answer +=1

    if correct_answer > 7:
        print("Bonus to the instructor")
    else:
        print("Better luck next time")
    print("You scored", correct_answer, " over 10")
    print("You failed ", wrong_answer, " answers")


random_number_generator()
