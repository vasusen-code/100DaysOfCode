import random
from data import data

score = 0

def random_person():
    a = random.choice(data)
    b = random.choice(data)
    if a == b:
        random_person()
    return a, b

def format_string(a: dict, b: dict):
    # a and b are dicts storing data of induvidual
    return f"""
    Comparison A: {a["name"]} is a {a["description"]} from {a["country"]}

    VS 

    Comparison B: {b["name"]} is a {b["description"]} from {b["country"]}

Enter 'a' or 'b':
    """

def ask_for_guess(person_a, person_b):
    guess = input(format_string(person_a, person_b)).lower()
    if guess != "a" and guess != "b":
        print("invalid entry!")
        ask_for_guess(person_a, person_b)
    else:
        return guess

game_end = False

print("Guess who has higher followers.\n\n")

while not game_end:
    A, B = random_person()
    guess = ask_for_guess(A, B)
    if guess == "a":
        if A["follower_count"] > B["follower_count"]:
            score += 1
            print(f"correct guess, Your score : {score}")
        else:
            print(f"Incorrect guess, Your score : {score}")
            score = 0
            game_end = True
    if guess == "b":
        if B["follower_count"] > A["follower_count"]:
            score += 1
            print(f"correct guess, Your score : {score}")
        else:
            print(f"Incorrect guess, Your score : {score}")
            score = 0
            game_end = True

