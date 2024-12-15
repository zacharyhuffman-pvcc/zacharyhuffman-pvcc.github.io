# Name: Zac Huffman
# Prog Purpose: This program computes PVCC college tuition & fees based on the number of credits
# The output is sent to an .html file

import datetime

############## Define global variables ##############
# Rates and fees
RATE_TUITION_IN = 164.40          # In-state tuition / per credit
RATE_TUITION_OUT = 353.00         # Out-of-state tuition / per credit
RATE_CAPITAL_FEE = 26.00          # Capital fee for out-of-state students 
RATE_INSTITUTION_FEE = 1.75       # Institution fee / per credit 
RATE_ACTIVITY_FEE = 2.90          # Activity fee / per credit 

# Global variables
inout = 1                         # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarship_amt = 0.0

tuition_amt = 0.0
inst_fee = 0.0
cap_fee = 0.0
act_fee = 0.0
total = 0.0
total_due = 0.0

# Create output file
outfile = 'pvccweb.html'

############## Define program functions ##############
def main():
    open_outfile()
    more_calculations = True
    
    while more_calculations:
        get_user_data()
        perform_calculations()
        create_output_file()
        
        ask_again = input('\nWould you like to calculate tuition & fees for another student (Y or N)?: ')
        if ask_again.upper() == 'N':
            more_calculations = False
            print(f'\n** Open this file in a browser window to see your results: {outfile}')
            f.write('</body></html>')
            f.close()

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html><head><title>PVCC Tuition & Fees</title>\n')
    f.write('<style>td{text-align: center} body {background-color: #d3d3d3; font-family: Arial; color: #000; ' 
            'background-image: url("wp-pvcc.jpg"); background-size: cover; background-repeat: no-repeat;}'
            'table {background-color: #add8e6; border-collapse: collapse; color: #ff4500; text-align: center;} '
            'th, td {border: 1px solid #000; padding: 8px;} '
            'th {background-color: #ffa07a; color: #000;}</style></head>\n')
    f.write('<body>\n')

def get_user_data():
    global inout, numcredits, scholarship_amt
    print('\n***** PIEDMONT VIRGINIA COMMUNITY COLLEGE Tuition & Fees *****')
    inout = int(input('Enter 1 for IN-STATE, 2 for OUT-OF-STATE: '))
    numcredits = int(input('Number of credits registered for: '))
    scholarship_input = input('Scholarship amount received: ')
    scholarship_amt = float(scholarship_input.replace(',', ''))

def perform_calculations():
    global tuition_amt, inst_fee, cap_fee, act_fee, total, total_due
    
    if inout == 1:
        tuition_amt = numcredits * RATE_TUITION_IN
    else:
        tuition_amt = numcredits * RATE_TUITION_OUT
        cap_fee = numcredits * RATE_CAPITAL_FEE

    inst_fee = numcredits * RATE_INSTITUTION_FEE
    act_fee = numcredits * RATE_ACTIVITY_FEE
    
    total = tuition_amt + inst_fee + cap_fee + act_fee
    total_due = total - scholarship_amt

def create_output_file():
    currency = ',.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'
    colsp = '<tr><td colspan="2">'

    f.write('\n<table border="3" style="margin: auto;">\n')            
    f.write(colsp + '\n')
    f.write('<h2>PIEDMONT VIRGINIA COMMUNITY COLLEGE</h2></td></tr>')
    f.write(colsp + '\n')
    f.write('Tuition & Fees Report\n')
    
    f.write(tr + 'Tuition' + endtd + format(tuition_amt, currency) + endtr)
    f.write(tr + 'Capital Fee' + endtd + format(cap_fee, currency) + endtr)
    f.write(tr + 'Institution Fee' + endtd + format(inst_fee, currency) + endtr)
    f.write(tr + 'Activity Fee' + endtd + format(act_fee, currency) + endtr)

    f.write(tr + 'Total' + endtd + format(total, currency) + endtr)
    f.write(tr + 'Scholarship' + endtd + format(scholarship_amt, currency) + endtr)
    f.write(tr + 'Balance Due' + endtd + format(total_due, currency) + endtr)
    
    f.write(colsp + f'Date/Time: {day_time}' + '</td></tr>')
    f.write('</table><br />')

############## Call main program to execute ##############
main()
