# My first OOP program!!!
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import random
run_count = 0
is_on = True

# Objects
main_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


# Key functions
def code():
    refill_code = ""
    while len(refill_code) < 7:
        refill_code += str(random.randint(0, 9))
    return refill_code


def menu_item(name):
    for item in main_menu.menu:
        if item.name == name:
            return item
    return None


def make(coffee):
    if coffee_maker.is_resource_sufficient(coffee):
        money_machine.make_payment(coffee.cost)
        if money_machine.money_received != 0:
            coffee_maker.make_coffee(coffee)


refill_code = code()

refill = input("Do you want to know the refill code for the Coffee Machine? (y/n)\n")

if refill == "y":
    print(f"Refill_Code: {refill_code}")

choices = ["off", "report", "latte", "espresso", "cappuccino", refill_code]

coffee = input(f"What would you like; ({main_menu.get_items()}report/off)?\n")
while coffee not in choices:
    coffee = input(f"Invalid response.\nWhat would you like; ({main_menu.get_items()}report/off)?\n")

if coffee == "off":
    print("Why did you bother running the program? -_-")
    is_on = False

while is_on:
    if coffee == "off":
        print("Hope to see you soon!")
        break
    elif coffee == "report":
        coffee_maker.report()
        money_machine.report()

    elif coffee == refill_code:
        if money_machine.profit == 0:
            print("No refill needed.")
        else:
            coffee_maker.refill()
            print("Refill complete.")

    else:
        make(menu_item(coffee))
        run_count += 1

        if run_count == 10:
            print("You are ordering too much coffee.")
            is_on = False

    coffee = input(f"What would you like; ({main_menu.get_items()}report/off)?\n")

    while coffee not in choices:
        coffee = input(f"Invalid response.\nWhat would you like; ({main_menu.get_items()}report/off)?\n")


