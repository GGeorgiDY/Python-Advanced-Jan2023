import random


class InvalidLevelError(Exception):
    pass


try:
    level = int(input("Select level: "))
except ValueError:
    raise InvalidLevelError("The level you selected is not valid.")

if level <= 0:
    raise InvalidLevelError("The level you selected is not valid.")


computer_number = random.randint(1, 10 * level)
play = True

while play:
    try:
        player_number = int(input("Guess the number: "))
    except ValueError:
        print("Please enter a number")
        continue

    if player_number == computer_number:
        print('You guessed it!')
        play = True if input("Do you want to play again? [y/n]") == "y" else False
        computer_number = random.randint(1, 10 * level)
    elif player_number < computer_number:
        print('Higher!')
    else:
        print('Lower!')
