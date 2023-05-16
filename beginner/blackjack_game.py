# lesson learnt: Don't assign same name for local variable and global variable. 

# Black jack game 

# managing the betting amounts by global varirables
remaining_amount = 1000
bet = 0

import random 

print("Welcome to the BlackJack game, Hope you know the rules.\n\n")
# Making 4 sets of cards
# Ace is 11 
# jack, queen and king are 10
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 
         11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
         11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
         11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]

# shuffle the cards (Just for interface, no actual shuffling since picking of cards is random)
print("Shuffling the cards...\n\n")

# dictionary to maintain the card details of dealer and player
set = {}

# pick cards for dealer and player
def pick_cards(n):
    chosen_cards = []
    for i in range(n):
        card = random.choice(cards)
        chosen_cards.append(card) 
    return chosen_cards

game_end = False

# placing the bet of player
def place_bet():
    global remaining_amount, bet
    try:
        bet = int(input(f"place your bet, you have $ {remaining_amount}\n"))
    except ValueError:
        print("Please only enter integers.")
        place_bet()
    if bet == 0:
        print("You cannnot play here for free you beggar.")
        place_bet()
    if bet < remaining_amount or bet == remaining_amount:
        print(f"A bet of $ {bet} is placed, Best of luck!\n\n")
        return bet
    else:
        print(f"You cannot place bet amount more than or equal to remaining amount.")
        place_bet()

# sum of cards
def sum(set, person):
    total = 0
    for card in set[person]:
        total += card
    return total

# making a move
def move():
    global set, remaining_amount, bet
    dealer = 0
    player = 0
    next_move = input("Do you want to 'hit' or 'stand' ?").lower()

    if next_move == "hit":
        new_card = pick_cards(1)
        print(f"You got a card of {new_card[0]}.")
        set["player"].append(new_card[0])
        if sum(set, "player") > 21:
            print(f"You lost $ {bet}")
            remaining_amount -= bet
        else:
            move()

    elif next_move == "stand":
        player = sum(set, "player")
        dealer = sum(set, "dealer")
        print(f"The dealer has a sum of {dealer}")
        if dealer >= 17:
            if dealer > 21:
                print(f"Congrats, you won $ {bet}!")
                remaining_amount += bet
                return remaining_amount
            player = 21 - player
            dealer = 21 - dealer
            if player < dealer:
                print(f"Congrats, you won $ {bet}!")
                remaining_amount += bet
            else:
                print(f"You lost $ {bet}")
                remaining_amount -= bet
        elif dealer == player:
            print("It is a draw.")
            remaining_amount += bet
            move()
        else:
            new_card = pick_cards(1)
            set["dealer"].append(new_card[0])
            dealer = sum(set, "dealer")
            print(f"The dealer got a new card of {new_card}")
            if dealer > 21:
                print(f"Congrats, you won $ {bet}!")
                remaining_amount += bet
                return remaining_amount
            player = 21 - player
            dealer = 21 - dealer
            if player < dealer:
                print(f"Congrats, you won $ {bet}!")
                remaining_amount += bet
            else:
                print(f"You lost $ {bet}")
                remaining_amount -= bet
    else:
        print("Incorrect entry.")
        move()

    return remaining_amount
    
# looping the game
while not game_end:
    bet = place_bet()
    cards_ = pick_cards(4)
    set["dealer"] = [cards_[0], cards_[1]]
    set["player"] = [cards_[2], cards_[3]]
    print(f'''Your cards are {set["player"][0]} and {set["player"][1]},
    while the dealer has two cards out of which one is {set["dealer"][0]}''')
    remaining_amount = move()
    if remaining_amount == 0:
        remaining_amount = 1000
        game_end = True

# the end
print("You have lost all the money, restart the game.")
