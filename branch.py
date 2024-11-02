# Name: your name here
# Prog Purpose: This program finds the cost of a meal at Branch Barbeque Buffet
#   Price for an adult meal: $19.95
#   Price for a child meal: $11.95
#   Service fee: 10%
#   Sales tax rate: 6.2%

import datetime

############## define global variables ##############
# define tax rate, service fee, and prices
ADULT_MEAL = 19.95

SALES_TAX_RATE = 0.62

# define global variables
num_adult_meals = 0

############## define program functions ##############
def main():
    more_meals = True

    while more_meals:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to order again (Y or N)? ")
        if yesno == "N" or yesno == "n":
            more_meals = False
            print("Thank you for your order. Enjoy your meal!")

def get_user_data():
    global num_adult_meals

def perform_calculations():
    global subtotal, service_fee, sales_tax, total

def display_results():
    print('----------------------------------------')
    print('**** Branch Barbeque Buffet ****')
    print('----------------------------------------')

########## call on main program to execute ##########
main()
