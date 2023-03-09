#========== Optional Task =============
# Program where user neters a number less than or equal to 100
# if they enter one about 100 ask them to try again
# if the number is valid check it is even and multiply it by 2 if it isnt multply it by 3
# print result
#======================================

#======= Variables ==========================
request = "Please enter a number under or equal to 100: "
limit = 100
error = "Wrong input, Try again!: "
num = 0
flag = True
result = 0
#===========================================

#=========== Processing ===============
while flag:
    num = int(input(request))
    if type(num) != type(1) or num > 100:       # Error check block
        print(error)
    else:
        # checking if it is odd of even
        if num % 2 == 0:
            result = num * 2
            print(f"The number {num} is even: the results in: {result} ")
            flag =  False
        
        else:
            result = num * 3
            print(f"The number {num} is odd: the results in: {result} ")
            flag = False

print("Thank You!:")

