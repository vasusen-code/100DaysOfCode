# number guess game 

import random

list_of_numbers = [10, 12, 15, 20, 24, 28, 30, 35, 40, 43, 46, 50]

random_number = random.choice(list_of_numbers)

def choose_level():
    chosen_level = input("choose the difficulty level from 'easy'  or 'hard'\n").lower()
    if chosen_level == "easy":
        return 10
    if chosen_level == "hard":
        return 5
    else: 
        print("incorrect entry!")
        choose_level()

lifes = choose_level()

print("Hint: The number will be between 10 and 50\n\n")
def game():
    global lifes
    guess = int(input(f"You have {lifes} chances to guess, guess your number.\n"))
    if guess == random_number:
        print("Correct guess, you win!")
        return True
    elif guess > random_number:
        lifes -= 1
        if lifes == 0:
            print("You lost all your chances, restart the game.")
            return True
        print(f"Wrong guess, {guess} is too high")
        game()
    else:
        lifes -= 1
        if lifes == 0:
            print("You lost all your chances, restart the game.")
            return True
        print(f"Wrong guess, {guess} is too low")
        game()

game_over = game()
if game_over:
    print("Game over.")
        

        
