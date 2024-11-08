#Name: Zac Huffman
#Prog Purpose: This program computes PVCC college tuition & fees based on the number of credits
#PVCC Fee Rates are from: https://www.pvcc.edu/tuition-and-fees

import datetime

"""This defines our rates and fees"""

#These will display in dollar amounts

RATE_TUITION_IN = 164.40          # In-state tuition / per credit
RATE_TUITION_OUT = 353.00          # Out-of-state tuition / per credit
RATE_CAPITAL_FEE = 26.00          # Capital fee for out-of-state students 
RATE_INSTITUTION_FEE = 1.75     # Institution fee / per credit 
RATE_ACTIVITY_FEE = 2.90        # Activity fee / per credit 

"""Global Variables For Our Functions"""

inout = 1                      # 1 means in-state, 2 means out-of-state --- but really any number other than 1 will work :)
numcredits = 0                 
scholarship_amt = 0           

tuition_amt = 0                
inst_fee = 0                   
cap_fee = 0                    
act_fee = 0                    
total = 0                      
total2 = 0                    

########### Define program functions ###########

def main():
    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()
        
        yesno = input("Would you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno == "n" or yesno == "N":
            more = False
            print("Thank you for enrolling at PVCC. Enjoy the semester!")

def get_user_data():
    global inout, numcredits, scholarship_amt
    print("\n***** PIEDMONT VIRGINIA COMM COLLEGE Tuition & Fees *****")
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: ")) 
    numcredits = int(input("Number of credits registered for: "))
    scholarship_input = input("Scholarship amount received: ")  # Allow comma-separated input for scholarship amount, I just learned about this and .split in my other class and thought 
    scholarship_amt = float(scholarship_input.replace(",", ""))  # this would be a neat addition since I found myself enter commas by habit


def perform_calculations():
    global tuition_amt, inst_fee, cap_fee, act_fee, numcredits, scholarship_amt, total, total2
    
    """In-state vs Out-of-state tuition"""

    if inout == 1:
        tuition_amt = numcredits * RATE_TUITION_IN #Moved global variable cap_fee up with others since it'll be zero for input "1" anyways
    else:
        tuition_amt = numcredits * RATE_TUITION_OUT
        cap_fee = numcredits * RATE_CAPITAL_FEE  #cap_fee only included in calc out-of-state tuiton

    inst_fee = numcredits * RATE_INSTITUTION_FEE #Total Inst. Fee Due After Credits

    act_fee = numcredits * RATE_ACTIVITY_FEE #Total Act. Fee Due After Credits 
    
    total = tuition_amt + inst_fee + cap_fee + act_fee #This is our total before adjustments
    
    total2 = total - scholarship_amt #This is our ttoal after adjustments 

def display_results():
    currency = '8,.2f' 
    sep_rate = '------------------------------------------'
    
    print(sep_rate)
    print('***** PIEDMONT VIRGINIA COMM COLLEGE *****')
    print('Tuition and Fees Report')
    print(sep_rate)
    print('Date:', datetime.datetime.now())
    print(sep_rate)
    print('Tuition:          $ ' + format(tuition_amt, currency))
    print('Capital Fee:      $ ' + format(cap_fee, currency))
    print('Institution Fee:  $ ' + format(inst_fee, currency))
    print('Activity Fee:     $ ' + format(act_fee, currency))
    print(sep_rate)
    print('Total:            $ ' + format(total, currency))
    print('Scholarship:      $ ' + format(scholarship_amt, currency))
    print(sep_rate)
    print('Balance Due:      $ ' + format(total2, currency))
    print(sep_rate)

"""Call main program to execute"""
main()
