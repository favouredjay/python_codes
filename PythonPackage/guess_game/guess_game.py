# import random
#
#
# class Guess_Game(object):
#     player_one_is_right = False
#     player_two_is_right = False
#     player_three_is_right = False
#
#
# def start_game(self):
#     correct_number = random.randrange(1, 10, 2)
#
#
# while True:
#     player_one_guess = int(input("Enter a number"))
#     player_two_guess = int(input("Enter a number"))
#     player_three_guess = int(input("Enter a number"))
#     if player_one_guess.__eq__(correct_number):
#         player_one_is_right = True
#     if player_two_guess == correct_number:
#         player_two_is_right = True
#     if player_three_guess == correct_number:
#         player_three_is_right = True
#
#     if player_one_is_right | player_two_is_right | player_three_is_right:
#         print("We have a Winner")
#         print("Player One is Correct ", player_one_is_right)
#         print("Player Two is correct ", player_two_is_right)
#         print("Player Three is correct", player_three_is_right)
#         print("Game is over")
#         break
#     else:
#         print("Players will have to try again")
#
# if __name__ == '__main__':
#     Guess_Game.start_game()
