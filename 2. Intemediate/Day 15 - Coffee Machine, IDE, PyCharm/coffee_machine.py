"""Coffee Machine"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def get_command():
    response = input("What would you like (espresso/latte/cappuccino)? ")

    if response == "espresso":
        enough_resources = True
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry, not enough water")
            enough_resources = False
        if resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry, not enough milk")
            enough_resources = False

        if enough_resources:
            money_given = get_money()

            if money_given < MENU["espresso"]["cost"]:
                print(f"Sorry, you don't have enough money, the espresso costs ${MENU["espresso"]["cost"]}")
            else:
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
                resources["money"] += MENU["espresso"]["cost"]

                if money_given > MENU["espresso"]["cost"]:
                    print(f"Here is your espresso, enjoy! You are returned ${(money_given-MENU["espresso"]["cost"]):.2f} in change.")
                else:
                    print("Here is your espresso, enjoy!")


    elif response == "latte":
        enough_resources = True
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry, not enough water")
            enough_resources = False
        if resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry, not enough milk")
            enough_resources = False
        if resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry, not enough coffee")
            enough_resources = False
        
        if enough_resources:
            money_given = get_money()

            if money_given < MENU["latte"]["cost"]:
                print(f"Sorry, you don't have enough money, the latte costs ${MENU["latte"]["cost"]}")
            else:
                resources["water"] -= MENU["latte"]["ingredients"]["water"]
                resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                resources["money"] += MENU["latte"]["cost"]

                if money_given > MENU["latte"]["cost"]:
                    print(f"Here is your latte, enjoy! You are returned ${(money_given-MENU["latte"]["cost"]):.2f} in change.")
                else:
                    print("Here is your latte, enjoy!")
        
    elif response == "cappuccino":
        enough_resources = True
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry, not enough water")
            enough_resources = False
        if resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry, not enough milk")
            enough_resources = False
        if resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry, not enough coffee")
            enough_resources = False
        
        if enough_resources:
            money_given = get_money()

            if money_given < MENU["cappuccino"]["cost"]:
                print(f"Sorry, you don't have enough money, the cappuccino costs ${MENU["cappucino"]["cost"]}")
            else:
                resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                resources["money"] += MENU["cappuccino"]["cost"]

                if money_given > MENU["cappuccino"]["cost"]:
                    print(f"Here is your cappuccino, enjoy! You are returned ${(money_given-MENU["cappuccino"]["cost"]):.2f} in change.")
                else:
                    print("Here is your cappuccino, enjoy!")

    elif response == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${resources["money"]:.2f}")

    elif response == "off":
        quit()

    else:
        get_command()

def get_money():
    pennies = input("Number of pennies ($0.01): ")
    nickels = input("Number of nickels ($0.05): ")
    dimes = input("Number of dimes ($0.10): ")
    quarters = input("Number of quarters ($0.25): ")
    money = float(pennies) * 0.01 + float(nickels) * 0.05 + float(dimes) * 0.10 + float(quarters) * 0.25

    return money

# Main game loop
while True:
    get_command()
