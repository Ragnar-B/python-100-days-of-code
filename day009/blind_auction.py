import os

auction = []
running = True

while running:
    name = input("What is your name?\n")
    bid = int(input("What's your bid?\n"))

    bidding = {}
    bidding["name"] = name
    bidding["bid"] = bid
    auction.append(bidding)

    continue_bid = input("Will there be another bid? Yes or No?\n").lower()

    if continue_bid == "yes":
        running = True
    else:
        running = False

    os.system('clear')

highest_bid = 0
person_bid = ""
for auction_bid in auction:
    if auction_bid["bid"] > highest_bid:
        highest_bid = auction_bid["bid"]
        person_bid = auction_bid["name"]

print(f"The highest bid of {highest_bid} is placed by {person_bid}!")