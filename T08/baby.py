# ********************* COMPULSORY TASK 1 *********************
# test if user is 18 or older and allowed entry into a party
# *************************************************************

#============ Variables ==============
allowed = "Congrats you are old enough"
year = int(input("What year were you born in "))

if year <= 2004:
    print(allowed)