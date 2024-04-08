from replit import clear
from art import logo

def get_name():
    get_name = str(input("\nWelcome, bidder. Enter your full name here: "))
    return get_name

def get_bid_price():
    bid_price = int(input("\nEnter your bid here: $"))
    return bid_price

def ask_to_go_again():
    go_again_ans = str(input("\nAre there other users who want to continue the bid? [YES / NO]: ").lower())    
    return go_again_ans

def determine_highest_bid(custom_name_and_bid):
    stored_bid = 0
    highest_bid = 0

    for key in custom_name_and_bid:

        stored_bidder = key
        stored_bid = custom_name_and_bid[key]

        if stored_bid > highest_bid:
            highest_bidder = stored_bidder
            highest_bid = stored_bid

    print(f"\nAt the highest bid tonight of ${highest_bid}, {highest_bidder} has won the auction. Congratulations!")

def main():

    print(logo)
    bid_ended = False
    name_and_bid = {}

    while not bid_ended:

        bidder_name = get_name()
        bidder_price = get_bid_price()
        name_and_bid[bidder_name] = bidder_price
        
        questioning_ended = False
        while not questioning_ended:
            go_again_ans = ask_to_go_again()
            if go_again_ans == "no" or go_again_ans == "n":
                bid_ended = True
                questioning_ended = True
            elif go_again_ans == "yes" or go_again_ans == "ye" or go_again_ans == "y":
                clear()
                questioning_ended = True
            else:
                print("\nWhat? Come on. Answer right, fool.")

        if bid_ended == True:
            determine_highest_bid(name_and_bid)
             
if __name__ == "__main__":
    main()
