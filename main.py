from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


c_machine = CoffeeMaker()
m_machine = MoneyMachine()
menu = Menu()


c_machine.report()
m_machine.report()


is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like to drink?{options}")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(c_machine.report())
        print(m_machine.report())
    else:
        drink = menu.find_drink(choice)
        if c_machine.is_resource_sufficient(drink) and m_machine.make_payment(drink.cost):
            c_machine.make_coffee(drink)
        else:
            print("Sorry that's not enough money. Money refunded.")