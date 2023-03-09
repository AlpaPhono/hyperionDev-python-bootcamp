#******************** OPTIONAL TASK **********************
# Program that will give you the meaning of an  abbreviation 
#*********************************************************

abbreviation = {"YOLO":"You Only Live Once","ADSL":"Asymmetric Digital Subscriber Line","DSLR":"Digital Single-Lens Reflex","API":"Application Programming Interface"}

abbreviation.update({"IDE":"Integrated Development Environment"})
abbreviation.update({"SDK":"Software Development Kit"})
#------------------ Process --------------------------
# Requesting usr input for abbreviation
# checking if usr input matches dictionary key
# if so outputting value
#-----------------------------------------------------
usr_abbr = input("Please enter an abbreviation: ")
usr_abbr = usr_abbr.upper()

if usr_abbr in abbreviation:
    print(abbreviation[usr_abbr])
else:
    print("Abbreviation not found.")
