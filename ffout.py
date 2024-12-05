# Name: Zachary Huffman
# Prog Purpose: This program creates a payroll report
import datetime

############## LISTS of data ############
emp = [
    "Smith, James ", "Johnson, Patricia", "Williams, John ","Brown, Michael ", "Jones, Elizabeth ",
    "Garcia, Brian ","Miller, Deborah ", "Davis, Timothy ","Rodriguez, Ronald","Martinez, Karen ","Hernandez, Lisa ","Lopez, Nancy ","Gonzales, Betty ","Wilson, Sandra ",
    "Anderson, Margie ","Thomas, Daniel ","Taylor, Steven ","Moore, Andrew ","Jackson, Donna ","Martin, Yolanda ","Lee, Carolina ", "Perez, Kevin ","Thompson, Brian ","White, Deborah ",
]
job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
       "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M"]
hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
         28, 31, 37, 32, 36, 22, 28, 29, 21, 31]
num_emps = len(emp)

# ########## NEW LISTS for calculated amounts ##########
gross_pay = []
fed_tax = []
state_tax = []
soc_sec = []
medicare = []
ret401k = []
net_pay = []

total_gross = 0
total_net = 0

# ########### TUPLES of constants ###########
# C    S     J    M
PAY_RATE = (16.50, 15.75, 15.75, 19.50)

# Fed, State, SS, Med, Ret
DED_RATE = (.12, .03, .062, .0145, .04)

# ########### Define program functions ###########
def main():
    perform_calculations()
    create_output_file()

def perform_calculations():
    global total_gross, total_net
    
    for i in range(num_emps):
        # Calculate gross pay
        if job[i] == "C":
            pay = hours[i] * PAY_RATE[0]
        elif job[i] == "S":
            pay = hours[i] * PAY_RATE[1]
        elif job[i] == "J":
            pay = hours[i] * PAY_RATE[2]
        else:
            pay = hours[i] * PAY_RATE[3]
        
        # Calculate deductions
        fed = pay * DED_RATE[0]
        state = pay * DED_RATE[1]
        ss = pay * DED_RATE[2]
        med = pay * DED_RATE[3]
        ret = pay * DED_RATE[4]
        
        net = pay - (fed + state + ss + med + ret)
        
        # Add to totals
        total_gross += pay
        total_net += net
        
        # Append amounts to lists
        gross_pay.append(pay)
        fed_tax.append(fed)
        state_tax.append(state)
        soc_sec.append(ss)
        medicare.append(med)
        ret401k.append(ret)
        net_pay.append(net)

def create_output_file():
    currency = '8,.2f'
    line = '\n------------------------------------------------------------\n'
    tab = "\t"

    # ########### output file ###########
    out_file = "payroll.txt"
    f = open(out_file, "a")

    f.write(line)
    f.write('\n*********** FRESH FOODS MARKET ***********')
    f.write('\n----------- WEEKLY PAYROLL REPORT -----------')
    f.write('\n' + tab + str(datetime.datetime.now()))
    f.write(line)

    titles1 = "Emp Name" + tab + "Code" + tab + "Gross" + tab
    titles2 = "Fed Inc Tax" + tab + "State Inc Tax" + tab + "Soc Sec" + tab + "Medicare" + tab + "Net"
    f.write(titles1 + titles2)
    f.write(line)

    # Write employee data to the file
    for i in range(num_emps):
        data1 = (
            '\n' + emp[i] + tab + job[i] + tab + format(gross_pay[i], currency) + tab +
            format(fed_tax[i], currency) + tab + format(state_tax[i], currency) + tab +
            format(soc_sec[i], currency) + tab + format(medicare[i], currency) + tab +
            format(net_pay[i], currency)
        )
        f.write(data1)

    f.write(line)
    f.write("\n****************** TOTAL GROSS: $" + format(total_gross, currency))
    f.write("\n****************** TOTAL NET  : $" + format(total_net, currency))
    f.write(line)
    f.close()

    print("Open " + out_file + " to view your report")

# ########## Call the main program ##########
main()
