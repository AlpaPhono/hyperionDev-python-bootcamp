#====== Compulsory Task 2 =========
#1 User enter the names of pupils in a class
#2 User type stop to indicate the names have been entered
#3 Print out total number of names entered.
# =================================

#======== DECLAIRING VARIABLES ===========
names = []
name = ""
request = "Enter a name: "
total_names = None


#======= Process =============
#loop requests user to enter names
while name.upper() != "STOP":
    name = input(request)
    names.append(name)


names.pop(-1)               # remove last item in list
total_names = len(names)    # store number of names in variable

print(f"Total number of names entered is: {total_names}")

