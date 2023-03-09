#======== Compulsory Task 1 =============
# display times tables for any number using for loop
# from start (1) to end (12)
# based from user input
#=======================================

#=========== Declairing Variables ================
usr_num = 0
calc = None
request = "Enter a number: "
#================================================

#=========== PROCESSING =======================
# Printing times tables
usr_num = int(input(request))
for num in range(13):
    calc = usr_num * num
    print(f"{usr_num} x {num} = {calc}")