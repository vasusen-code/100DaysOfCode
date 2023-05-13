#Hangman game
import random

lives = ["❤️", "❤️", "❤️", "❤️", "❤️"] 

word_list = ["apple", "baloon", "camel", "donkey"]

chosen_word = random.choice(word_list)
 
letters = []
word = ""
for i in range(len(chosen_word)):
    letters.append("_ ")

for i in range(len(letters)):
    word += letters[i]

game_end = False
while not game_end:
    guess = input(f"Choose a letter for\n{word}\n")
    if guess in chosen_word:
        for letter in range(len(chosen_word)):
            if guess == chosen_word[letter]:
                letters[letter] = f"{guess} "
        word = ""
        for i in range(len(letters)):  
            word += letters[i]
    else:
        lives.pop(0)
        print("Oops!! Wrong guess, you lost a life.")
        if not len(lives) > 0:
            print("Game over.")
            game_end = True

    if not "_ " in letters:
        print("You won.")
        game_end = True




