import random


def roll_dice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)


def sum_dice(dice):
    die1, die2 = dice
    print(f"player rolled {die1} + {die2} = {sum(dice)}")


# print(sum_dice(roll_dice()))
dice_values = roll_dice()
sum_dice(dice_values)
sum_of_dice = sum(dice_values)
print(sum_of_dice)

if sum_of_dice in (7, 11):
    game_status = "WON"

elif sum_of_dice in (2, 3, 12):
    game_status = "LOSE"
else:
    game_status = "CONTINUE"
    my_point = sum_of_dice
    print("Point is", my_point)

while game_status == "CONTINUE":
    dice_values = roll_dice()
    sum_dice(dice_values)
    sum_of_dice = sum(dice_values)

    if sum_of_dice == my_point:
        game_status = "WON"
    elif sum_of_dice == 7:
        game_status = "LOSE"

if game_status == "WON":
    print("Player wins")
elif game_status == "LOSE":
    print("Player loses")
