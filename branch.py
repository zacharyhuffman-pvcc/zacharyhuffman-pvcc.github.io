# Name: Zac Huffman
# Prog Purpose: This program finds the cost of a meal at Branch Barbeque Buffet
#   Price for an adult meal: $19.95
#   Price for a child meal: $11.95
#   Service fee: 10%
#   Sales tax rate: 6.2%

import datetime

############## define global variables ##############
# define tax rate, service fee, and prices
ADULT_MEAL = 19.95
CHILD_MEAL = 11.95

SERVICE_FEE_RATE = 0.10
SALES_TAX_RATE = 0.062

# define global variables
num_adult_meals = 0
num_child_meals = 0
subtotal = 0
subtotal1 = 0 
subtotal2 = 0
service_fee = 0
sales_tax = 0
total = 0

############## define program functions ##############
def main():
    more_meals = True

    while more_meals:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to order again (Y or N)? ")
        if yesno.lower() == "n":
            more_meals = False
            print("Thank you for your order. Enjoy your meal!")

def get_user_data():
    global num_adult_meals, num_child_meals
    num_adult_meals = int(input("How many adults are in your party? "))
    num_child_meals = int(input("How many children are in your party? "))

def perform_calculations():
    global subtotal, subtotal1, subtotal2, service_fee, sales_tax, total
    
    # Individual subtotals for adults and children
    subtotal1 = num_adult_meals * ADULT_MEAL
    subtotal2 = num_child_meals * CHILD_MEAL
    
    # Sum up the subtotals to get overall subtotal
    subtotal = subtotal1 + subtotal2
    
    service_fee = subtotal * SERVICE_FEE_RATE
    sales_tax = subtotal * SALES_TAX_RATE
    
    # Calculate total
    total = subtotal + service_fee + sales_tax

#Final Receipt Function
def display_results():
    print('----------------------------------------')
    print('**** Branch Barbeque Buffet ****')
    print('----------------------------------------')
    print('Adult Meals      $' + format(subtotal1, '8.2f'))
    print('Child Meals      $' + format(subtotal2, '8.2f'))
    print('Subtotal         $' + format(subtotal, '8.2f'))
    print('Service Fee      $' + format(service_fee, '8.2f'))
    print('Sales Tax        $' + format(sales_tax, '8.2f'))
    print('Total            $' + format(total, '8.2f'))
    print('----------------------------------------')
    print(str(datetime.datetime.now()))

########## call on main program to execute ##########
main()
