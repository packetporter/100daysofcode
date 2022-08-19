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
}


# Check resources are enough to make the type of coffee
def resources_check(reserve, order_ingredients):
    for item in order_ingredients:
        if reserve[item] >= order_ingredients[item]:
            return True
        else:
            print(f"Sorry there is not enough {item}")
            return False


# Function to count value of coins inserted in dollars.
def user_money():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    return quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01


# Check if the cash given by the user is enough
def cash_check(cash_tendered, coffee_price, coffee_t):
    """expects total coins inserted, price of coffee and coffee type"""
    if cash_tendered > coffee_price:
        print(f"Here is ${round(total_money - coffee_cost, 2)} in change.")
        print(f"Here is your {coffee_t}. Enjoy")
        return True
    elif cash_tendered == coffee_price:
        print(f"Here is your {coffee_t}. Enjoy")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# Calculate resources remaining after dispensing coffee
def resource_remaining(ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    return resources


revenue = 0
machine_on = True
while machine_on:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_type == "off":
        machine_on = False
    elif coffee_type == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${revenue}")
    else:
        drink = MENU[coffee_type]
        if resources_check(resources, drink["ingredients"]):
            coffee_cost = MENU[coffee_type]["cost"]
            total_money = user_money()
            drink = MENU[coffee_type]
            if cash_check(total_money, coffee_cost, coffee_type):
                revenue += coffee_cost
                resource_remaining(drink["ingredients"])
