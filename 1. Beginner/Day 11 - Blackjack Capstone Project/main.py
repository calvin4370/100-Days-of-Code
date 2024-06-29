import random
"""
Day 11: Blackjack Capstone Project
This is a simple implementation of Blackjack, with no regard for the suits.
"""

def main():
    print("Blackjack\n")
    FACES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["HEARTS", "DIAMONDS", "CLUBS", "SPADES"]
    INITIAL_MONEY = 1000
    global wallet
    wallet = INITIAL_MONEY
    round = 1
    
    # The deck is a list of dicts, where each dict is a {face:face, suit:suit}
    deck = []
    for suit in SUITS:
        for face in FACES:
            card = {}
            card["face"] = face
            card["suit"] = suit
            card["hidden"] = False
            deck.append(card)
    random.shuffle(deck)

    # Main Game Loop
    while True:
        # 0th step: Show player's wallet, get bet
        print(f"\nRound: {round}")
        print(f"Money: ${wallet}")
        global bet
        bet = get_bet(wallet)

        # 1st step: Deal 2 cards to player and 2 cards to dealer (1 face down, 1 face up), print to screen
        player_hand = []
        dealer_hand = []
        draw(player_hand, 2, deck)
        draw(dealer_hand, 1, deck, hidden=True)
        draw(dealer_hand, 1, deck)

        show_hand(player_hand, "Player")
        show_hand(dealer_hand, "Dealer")

        # Cycling Loop
        # 2nd Step: Cycle: Allow player to choose whether to (H)it until satisfied or bust, or (S)tand
        # 3rd step: If player (S)tands, check winner, announce. or if player has gone bust, prompt whether to continue
        while True:
            move = get_move()
            if move == "H":
                draw(player_hand, 1, deck)
                show_hand(player_hand, "Player")
                show_hand(dealer_hand, "Dealer")
                if check_bust(player_hand):
                    dealer_turn_results = "player_busts_first"
                    break
            elif move == "S": # Time for dealer to play their turn
                show_hand(player_hand, "Player")
                show_hand(dealer_hand, "Dealer")
                print("") # Newline before dealer plays their turn
                print("Dealer's Turn")
                print("-------------")
                dealer_turn_results = dealer_turn(dealer_hand, deck)
                break
        
        decide_winner(dealer_turn_results, player_hand, dealer_hand)
        prompt_continue(wallet)
        round += 1

# Draw a card from the deck into a character's hand
def draw(hand, times, deck, hidden=False):
    for i in range(times):
        card = deck.pop()
        card["hidden"] = hidden
        hand.append(card)

# Return's a card's value(11 for Aces)
def card_value(card):
    if card["face"] == "A":
        return 11
    elif card["face"] in ["J", "Q", "K"]:
        return 10
    else:
        return int(card["face"])

# Shows a character's hands and it's value
def show_hand(hand, character):
    cards = []
    for card in hand:
        if card["hidden"]:
            cards.append("X")
        else:
            cards.append(card["face"])
    
    print(f"{character}'s hand: {cards} --- Value: {count_value(hand)["shown_value"]}")

# Returns a dict: {"actual_value", "shown_value"}
def count_value(hand):
    cards = []
    actual_value = 0
    shown_value = 0
    aces = 0
    for card in hand:
        if card["face"] == "A":
            aces += 1
        if card["hidden"]:
            pass
        else:
            shown_value += card_value(card)
        actual_value += card_value(card)
    for i in range(aces):
        if actual_value > 21:
            actual_value -= 10
        if shown_value > 21:
            shown_value -= 10
    values = {}
    values["actual_value"] = actual_value
    values["shown_value"] = shown_value
    return values

# Return's player's bet
def get_bet(wallet):
    while True:
        bet = input("\nYour bet: ")
        if bet.isdigit():
            if int(bet) > wallet:
                continue
            else:
                break
    return int(bet)

# Prompts player for a valid move and returns it
def get_move():
    valid = ["H", "S"]
    while True:
        move = input("\nDo you want to (H)it or (S)tand? ")
        move = move[0].upper()
        if move not in valid:
            continue
        else:
            break
    return move

# Check's whether a hand has gone bust
def check_bust(hand):
    return count_value(hand)["actual_value"] > 21

# Dealer plays their turn, returns results on whether dealer stops (reached 17) or busts (exceeds 21)
def dealer_turn(dealer_hand, deck):
    # dealer_turn_results = ["dealer_stops", "dealer_busts"]
    dealer_value = count_value(dealer_hand)["actual_value"]

    for card in dealer_hand:
        card["hidden"] = False
    
    while True:
        if check_bust(dealer_hand):
            return "dealer_busts"
        elif count_value(dealer_hand)["actual_value"] >= 17:
            return "dealer_stops"
        else:
            print("\nThe Dealer draws a card")
            draw(dealer_hand, 1, deck)
            show_hand(dealer_hand, "Dealer")
            print("")

# Decide winner at the end of dealer's turn
def decide_winner(dealer_turn_results, player_hand, dealer_hand):
    global bet
    global wallet
    if dealer_turn_results == "dealer_busts":
        print("\nDealer busts! You win!")
        print(f"You get ${bet}")
        wallet += bet
    elif dealer_turn_results == "dealer_stops":
        show_hand(player_hand, "Player")
        show_hand(dealer_hand, "Dealer")
        player_value = count_value(player_hand)["actual_value"]
        dealer_value = count_value(dealer_hand)["actual_value"]
        if player_value > dealer_value:
            print("You win!")
            print(f"You get ${bet}")
            wallet += bet
        elif dealer_value > player_value:
            print("You lose!")
            print(f"You lose ${bet}")
            wallet -= bet
        else:
            print("Push!")
            print("Your bet is returned")
    elif dealer_turn_results == "player_busts_first":
        print("\nYou bust!")
        print(f"You lose ${bet}")
        wallet -= bet

# Prompt player to continue if money is positive, if no money, end game also
def prompt_continue(money):
    if money == 0:
        print("\nYou have no money left. Game Over!")
        quit()
    else:
        print(f"\nYour money: ${money}")
        choice = input("Do you want to continue (y/n)? ")
    if choice[0].upper() == "Y":
        pass
    else:
        print("Game ended. Thank you for playing.")
        quit()

if __name__ == "__main__":
    main()