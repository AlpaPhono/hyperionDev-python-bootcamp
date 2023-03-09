#************** Compulsory Task 1 ************
# Write a program that asks a user for a number and prints out even numbers from one up to or equal to the number
#*********************************************

#========== DECLARING VARIABLES =============
num = 0
request = "Please enter a number:  "
limit = True
current_num = 1 

#========== Process Block ==================

num = int(input(request))

# The block checks if current number variable is even prints the result if true and increments its value
# When current number is equivelant to user input while loop will end.
while limit:

    if current_num % 2 == 0:
        print(current_num)
    current_num+=1
    if current_num > num:      # condition to switch flag value
        limit = False
     

