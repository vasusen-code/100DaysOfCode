# silent bidding program

bids = {}

def check_winer(bids_):
    highest_bid = 0
    winner = ""
    for bid in bids_:
        if bids[bid] > highest_bid:
            highest_bid = bids[bid]
            winner = bid
    return winner, highest_bid

bidding_finished = False

while not bidding_finished:
    bidder = input("Input your name:\n")
    bidding_amount = input("Input your bidding amount:\n$ ")
    bids[bidder] = int(bidding_amount)
    next_person = input("Is there anyone else left for bidding? yes/no\n").lower()
    if next_person == "yes":
        continue
    elif next_person == "no":
        winner, highest_bid = check_winer()
        print(f"{winner} wins this bidding contest by an bidding amount of $ {highest_bid}")
        bidding_finished = True
    else:
        print("Incorrect entry! Finding the winner among the bidders.")
        winner, highest_bid = check_winer(bids)
        print(f"{winner} wins this bidding contest by an bidding amount of $ {highest_bid}")
        bidding_finished = True

        
