# TODO 1: Import Menu and resources from main
from requirements import MENU,resources,coffee
money = 0
# Part 2 of TODO 5:
def coins():
    print("Please insert coins:")
    quarters = int(input("Number of quarters: "))
    dimes = int(input("Number of dimes: "))
    nickels = int(input("Number of nickels: "))
    pennies = int(input("Number of pennies: "))
    return (quarters*0.25)+(dimes*0.1)+(nickels*0.05)+(pennies*0.01)
# Part 2 of TODO 4:
def stock_checker(resource,beverage):
    not_in_stock = 0
    for key in resource:
        if resource[key] < beverage["ingredients"][key]:
            print(f"Sorry there is not enough {key}")
            not_in_stock += 1
    return not_in_stock
def coin_checker(given_price,actual_price):
    if given_price < actual_price:
        print("Sorry that's not enough money. Money Refunded")
        return None
    else:
        balance = (given_price - actual_price)
        balance = round(balance, 2)
        return balance
make_coffee = True

while make_coffee:
    # TODO 2: Ask the user about the drink of their choice
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()


    #TODO 3: What if the input is off or report?
    if user_choice == "report":
        for key in resources:
            print(f"{key} : {resources[key]}")
        print(f"money: {money}")
    elif user_choice == "off":
        print("Machine turned off")
        make_coffee = False
    elif user_choice in MENU:
        drink = MENU[user_choice]
        cost = drink["cost"]
    # TODO 4: If the drink is on the menu, then, first, check if the resources are available. Part 2: Create a function for the same.
        unavailable = stock_checker(resources,drink)

        if unavailable == 0:
            # TODO 5: Create variables named Pennies, Nickels, Dimes and Quarters which take the number of each coin as a input. Part 2: Make this as a function that returns the total amount.
            #Part 2 is in execution

            # TODO 6: Calculate the total amount.
            given_amount = coins()
            #TODO 7: If the given amount is less than the cost, let the user know and then refund the given amount, else add the cost to the profit and give the required change and when resources are unavailable then ask for the user's choice again whereas if the resources available, then deduct the required resources from the available resources and give the coffee. - Part 2: Create a function for the same and also another function that delivers the coffee and returns the money.
            change = coin_checker(given_amount,cost)
            if change != None:
                if change!=0:
                    print(f"Here's ${change} in change.")
                print(coffee)
                print(f"Here's your {user_choice}. Enjoy!")
                money += cost
                for key in resources:
                    resources[key] -= drink["ingredients"][key]

        # TODO 8: Put a while loop to repeat the code again and again.(DONE!)
