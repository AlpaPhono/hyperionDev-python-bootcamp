#****************** Task 1*************
# Ask user for three different integers 

#
def num_Request():
    msg = "This is not an integer, Try again! " 
    request = "Please enter an integer "
    flag = False
    while flag == False:
        num = input(request)

        if num.isdigit():
            flag = True

        else:
            print(msg)

    num = int(num)
    return num

# error handling func to make sure user inputs a number and not a string

def not_the_same(first,second):
    flag = True
    msg = "enter a different number: "
    while flag == True:
        if second == first:
            print(msg)
            second = num_Request()
        elif second != first:
            flag = False
            num_list.append(second)
# function to restrict the user from inputting two of the same values into a list.
# I thought about creating a set but.... In hind sight i should have just used a set


                       
#======== Body of code ==========

#======== Declairing variables ==============
num_list = []

num1 = num_Request()

num_list.append(num1)

num2 = num_Request()
not_the_same(num1,num2)

num3 = num_Request()
not_the_same(num2,num3)
not_the_same(num1,num3)


#===== Print out the sum =====
print(num1 + num2 + num3)
print(type(num1))

#==== Print out the First number minus the second Number =====
print(f"The first number minus the second one is:\n{num_list[0] - num_list[1]}")

#==== The third number multiplied by the first number =====

print(f"The third number multiplied by the first number is:\n{num_list[2] * num_list[0]}")

#===== Sum of all three numbers divided by the third number =====

sum_of_3 = num1 + num2 + num3
print(f"The sum of all three numbers divided by the third number is:\n{sum_of_3/num3}")

#================= References ==========================
# favetutor.com. 5 oct 2022. How to check if the String is Integer in Python [online] Accessed 13/12/22 Available from: https://favtutor.com/blogs/check-string-is-integer-python#:~:text=The%20isdigit()%20method%20is,and%20False%20if%20it%27s%20not.

