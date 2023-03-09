# User inputs a number and it is casted into an int 

num = int(input("Please enter a number: "))

#========= Process Block ================
#use user input to control the amount of times number is printed.
if num > 10:
    for times in range(num):
        print(num)
elif num <= 10:
    print("Sorry to small")

    