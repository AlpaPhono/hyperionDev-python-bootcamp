#******************** Compulsory task 2 *******************
# write the numbers from numbers1.txt and numbers2.txt
# to a third file called all_numbers.txt
#**********************************************************


#------------------ Declairing Variables ------------------
# Declairing file objects and their lists to hold read data
#----------------------------------------------------------
num1_file = open("numbers1.txt","r+")
num2_file = open("numbers2.txt","r+")
num3_file = open("all_numbers.txt", "w+")

num1_list = num1_file.readlines()
num2_list = num2_file.readlines()
num3_list = []

#------------------- Process -------------------
# For block iterates through lists
#  and appends their values to the empty 3 list
#-----------------------------------------------
for num1 in num1_list:
    num3_list.append(num1.strip("\n"))
for num2 in num2_list:
    num3_list.append(num2.strip("\n"))


#------------------ Process 2 -----------------
# data in list is sorted and then written to file
#----------------------------------------------
#num3_list.sort()                                            #Using num3_list.sort() wasnt working because data is read as string!

num3_list = sorted(num3_list,key=int)
#print(num3_list)

for num3 in num3_list:
    num3_file.write(num3 + "\n")


num1_file.close()
num2_file.close()
num3_file.close()