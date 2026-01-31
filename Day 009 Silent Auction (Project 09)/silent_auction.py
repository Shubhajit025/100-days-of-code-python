from art import logo
print(logo)

silent_bids = {}

def auction_winner(bid_info):
    most_valued_bid = 0
    the_winner = ""

    for al_bidders in bid_info:
        bid_value = bid_info[al_bidders]

        if bid_value > most_valued_bid:
            most_valued_bid = bid_value
            the_winner = al_bidders

    print(f"The Silent Auction winner is {the_winner} with the bid value of {most_valued_bid}")

bidding_continue = True

while bidding_continue:


    # Asking the user for input 👇
    user_name = input("What is your name?:    ")
    bid_amount = int(input("What is your bid?:  $  "))

    # Saving data into dictionary {name: price} 👇
    silent_bids[user_name] = bid_amount
    # Whether if new bids need to be added 👇
    bid_member = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if bid_member == "no":
        bidding_continue = False
        auction_winner(silent_bids)
    else:
        print("\n" * 25)
