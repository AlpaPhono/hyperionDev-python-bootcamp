#************** COMPULSORY TASK 3 ********************
#                   STEP 1
# program that takes in user's input
# stores incorrectly entered strings in a list 
# When john is entered the loop terminates
#****************************************************

#----------------------- Variables -----------------
wrong_input = []
usr_input = ""

#------------------ Process ------------------------
'''
A loop that requests input and stores incorrect ones into a list variable
'''
while usr_input.lower() != "john":          
    usr_input = input("Enter John as a string.\nIf you dont enter John this will not stop: ")

    if usr_input == "John":
        print("Finally it's over!")
    else:
        wrong_input.append(usr_input)


#---------------------------------------------------
# Loop that prints out each item of the list
#---------------------------------------------------
print()             # for space in console
for item in wrong_input:        
    print(item)
   



