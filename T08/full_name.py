#******************* COMPULSORY TASK 2 ************************
#Validates the user niputs at least two names 
#**************************************************************

#============== VARIABLES ====================
no_name = "You haven't entered anything. Please enter your full name"
too_short = "You have entered less than 4 characters. Please make sure you have entered your name and surname"
too_long = "You have entered more than 25 characters. Please make sure that you have only entered your full name"
perfect = "Thank you for entering your name"
name = input("What is your full name: ")
full_name = name.split(" ")

#=============== Processing =================
if len(name) == 0:
    print(no_name)
if len(name) < 4:
    print(too_short)
if len(name) > 25:
    print(too_long)

if len(full_name)>= 2:
    print(perfect)
    print(full_name)

else:
    print("You didn't enter a full name")
