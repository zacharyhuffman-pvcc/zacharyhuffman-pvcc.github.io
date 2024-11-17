# Name:Zac Huffman
# Prog Purpose: This program finds the cost of a meal at Palermo Pizza

import datetime

######## define global variables ########
PRICE_SMALL = 9.99
PRICE_MED = 12.99
PRICE_LARGE = 17.99
PRICE_XL = 21.99
PRICE_DRINK = 3.99
PRICE_BREADSTICKS = 6.99
TAX_RATE = 0.055

######## define global variables ########
num_pizzas = 0
num_drinks = 0
num_breadsticks = 0
cost_pizzas = 0
cost_drinks = 0
cost_breadsticks = 0
subtotal = 0
sales_tax = 0
total = 0

######## define program functions ########
def main():
    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("Would you like to order again (Y or N)? ")
        if yesno.upper() == "N":
            more = False
            print("\nThank you for your order. Enjoy your pizza!")

def get_user_data():
    global pizza_size, num_pizzas, num_drinks, num_breadsticks

    print("****** Palermo Pizza ******")
    print(" S Small Pizza $9.99")
    print(" M Medium Pizza $12.99")
    print(" L Large Pizza $17.99")
    print(" X Extra Large Pizza $21.99")

    pizza_size = input("\nWhat size pizza would you like to order? (S, M, L, X): ").upper() 
    num_pizzas = int(input("Number of pizzas: "))
    num_drinks = int(input("Number of drinks: "))
    num_breadsticks = int(input("Number of breadstick orders: "))

def perform_calculations():
    global cost_pizzas, cost_drinks, cost_breadsticks, subtotal, sales_tax, total

    # Pizza calc
    if pizza_size == "S":
        cost_pizzas = num_pizzas * PRICE_SMALL
    elif pizza_size == "M":
        cost_pizzas = num_pizzas * PRICE_MED
    elif pizza_size == "L":
        cost_pizzas = num_pizzas * PRICE_LARGE
    elif pizza_size == "X":
        cost_pizzas = num_pizzas * PRICE_XL
    else:
        cost_pizzas = 0

    # Cost for Items 
    cost_drinks = num_drinks * PRICE_DRINK
    cost_breadsticks = num_breadsticks * PRICE_BREADSTICKS

    # Our totals 
    subtotal = cost_pizzas + cost_drinks + cost_breadsticks
    sales_tax = subtotal * TAX_RATE
    total = subtotal + sales_tax

def display_results():
    currency = "$"
    line = "------------------------------"
    full_date = str(datetime.datetime.now())
    short_date = full_date[0:16]

    print("\n" + line)
    print("****** Palermo Pizza ******")
    print("Date/Time: " + short_date)
    print(line)
    print(f"Number of pizzas ordered: {num_pizzas}")
    print(f"Number of drinks ordered: {num_drinks}")
    print(f"Number of breadsticks ordered: {num_breadsticks}")
    print(line)
    print('Pizzas      $ ' + format(cost_pizzas, '.2f'))
    print('Drinks      $ ' + format(cost_drinks, '.2f'))
    print('Breadsticks $ ' + format(cost_breadsticks, '.2f'))
    print(line)
    print('Subtotal    $ ' + format(subtotal, '.2f'))
    print('Sales Tax   $ ' + format(sales_tax, '.2f'))
    print(line)
    print('Total       $ ' + format(total, '.2f'))
    print(line)

######## call on main program to execute ########
main()
