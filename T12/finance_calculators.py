#================================ Compulsory Task 1 =====================================
# A program that allows the user to access two different financial calculators: an investment and home lone repayment calculator
#========================================================================================
import math


def option_error(usr_input,msg,option1,option2):
    error_flag = True
    while error_flag:
        usr_input = input(msg)
        if usr_input.upper() == option1.upper() or usr_input.upper() == option2.upper():
            error_flag = False
        else:
            print("\ninput not recognised, Please try again: ")

    return usr_input

''' Function to error check user input based on given options
'''



#=============== Variables ==============
request = "Choose either 'investment' or 'bond' from the menu below to proceed:\n\ninvestment\t- to calculate the amount interest you'll earn on your investment\nbond\t\t- to calculate the amount you'll have to pay on a home lone:\n"
user_choice = ""
deposit = 0
interest_rate = 0
years = 0
interest = ""
total_amount = 0
house_value = 0
months = 0
repayment = 0
#============== Processing ==============

user_choice = option_error(user_choice,request,"INVESTMENT","BOND")     # Using errorcheck function to initialise 


# If user input is investment the following block will execute
# Requests amount to deposit, interest rate and length in years
if user_choice.upper() == "INVESTMENT":
    deposit = float(input("How much would you like to deposit: "))
    interest_rate = float(input("What is the interest rate: "))
    years = int(input("Number of years to invest: "))
    interest = option_error(interest,"Simple or Compound interest?: ","SIMPLE","COMPOUND")

    
    # different outcome if user entered simple or compound interest
    if interest.upper() == "SIMPLE":
        total_amount = deposit*((1 + interest_rate)* years)
        print(f"Total amount saved will be: {total_amount}") 

    elif interest.upper() == "COMPOUND":
        total_amount = deposit * math.pow((1 + interest_rate), years)
        print(f"Total amount saved will be: {total_amount}") 

# Calculations for monthly repayments for the bond
# The instructions don't differentiate between if user inputs annual interest rate or monthly interest rate
elif user_choice.upper() == "BOND":
    house_value = float(input("What is the current value of the property: "))
    interest_rate = float(input("What is the interest rate: "))
    months = int(input("Number of months to repay bond: "))
    repayment = (interest_rate * house_value) / 1 - math.pow((1 + interest_rate),(-1 * months))     # in this calculation I assumed the user inputs the monthly interest rate
    print(f"Total monthley repayment will be: {repayment}") 






