from logo import logo

print(logo)

bids = {}
start = True


def clean():
    print('\n' * 50)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while start:
    name = input("What is your name?:\n")
    price = int(input("What is your bid?:\n$"))
    bids[name] = price
    restart = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if restart == "no":
        start = False
        find_highest_bidder(bids)
    elif restart == "yes":
        clean()
        print(logo)
