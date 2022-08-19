from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
machine_on = True

while machine_on:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        drink_cost = drink.cost
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink_cost):
                coffee_maker.make_coffee(drink)
