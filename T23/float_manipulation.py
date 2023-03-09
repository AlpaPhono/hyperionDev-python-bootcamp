#--------------- Compulsory task 1 ----------------
# Program asking the user to input 10 floats
#--------------------------------------------------
#------------- Imports -----------
import math , statistics

#------------- Variables ---------
float_list = []
number = 0
#---- Asking for 10 variables ---- 
print("This program will request you to enter a float value 10 times.\nThis can be a combination of whole numbers and decimals:\n ")
while len(float_list) < 10:
    
    
    for index, i in enumerate(range(10)):
        number = float(input(f"Please enter a float variable:"))
        float_list.append(number)

#-- Finding Total of all numbers --
total_numbers = 0
for num in float_list:

    total_numbers += num

print(f"Total of all the numbers is: {total_numbers}")

#-------- Maximum index --------
max_index = float_list.index(max(float_list))
print(f"The index of the biggest number in the list is: {max_index}")

# -------- Minimum Index -------
min_index = float_list.index(min(float_list))
print(f"The index of the smallest number in the list is: {min_index}")

#--- Average of numbers to 2dp --- 
average_of_numbers = total_numbers / len(float_list)
print(f"The average of all numbers is: {round(average_of_numbers,2)}")

#---- Find Median ----------
print(f"The median of the list is: {statistics.median(float_list)}")




