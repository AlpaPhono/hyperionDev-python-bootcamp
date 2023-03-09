#======= Compusolry Task 3 =============
#
#=======================================

#******************************************************************
#1 Create a while loop that will dsiplay a count down from 20 to 0
#*******************************************************************
print("Create a while loop that will dsiplay a count down from 20 to 0")

#=========== Variables ===============
count = 0
limit = 20

#=========== Process ================
# while count is less than 21 to ensure that limit reaches 0
while count < 21:
    print(limit)
    limit -= 1
    count+= 1
#=====================================

print("")   # to create a new line 


#******************************************************************
#2 create a loop that will display even numbers between 1 and 20
#******************************************************************

print("Create a loop that will displahy even numbers between 1 and 20:\n ")
for number in range(1,20):
    if number % 2 == 0:
        print(number)

#******************************************************************
#3 use loop to display pattern
#******************************************************************
print()     # used to create new line 


star ="*"
print("use loop to display pattern")
for num in range(5):

    print(star)
    star = star + "*"





