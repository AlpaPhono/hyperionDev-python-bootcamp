#================= Compulsory Task 4 =====================
#======== Declaring Variables =================
request = "Please Enter an integer: "
num = int(input(request)) # user input of int

#============== Processing ===============
print("") # to create a newline in consol output

#if num % 2 == 0 and num % 5 == 0:
if num % 10 == 0: # chose to use 10 because all number divisible by 2 and 5 are also divisible by 10
    print(f"user input: {num} is divisible by 5 and 2")
else:
    print(f"user input: {num} is not divisible by 5 and 2")

print("") # to create a newline in consol output

if num % 2 == 0 or num % 5 == 0:
    print(f"user input: {num} is divisible by 5 or 2")
else:
    print(f"user input: {num} is not divisible by 5 or 2")



