#====== Compulsory Task 3 =========
#1 User enters a number
#2 User type -1 to stop program requesting a number
#3 Print out average of numbers entered.
# =================================

#======== DECLAIRING VARIABLES ===========
numbers = []
number = 0
request = "Enter a number: "
average = None
add = 0
flag = True


#======= Process =============
#loop requests user to enter numbers
while flag == True:
    if number == -1:
        flag = False

    else:
        number = int(input(request))            # Remember to cast input into an int
        numbers.append(number)

numbers.pop(-1)               # remove last item in list

for num in numbers:
    add +=num

total_average = add / len(numbers)   # Calculate average and store in a variable

print(f"Average total of numbers entered is: {total_average}")

