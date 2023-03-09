#********************* OPTIONAL TASK 1 ***********************
# Test whether a number is odd or even

#===================== VARIABLES ==================
even = "This number is even"
odd = "This number is odd"
num = int(input("Please enter a number: "))

#============== Processing ========================
if num % 2 == 0: # this means it has no remainder when divided by 2 making it an even number
    print(even)
    print(num)
else:
    print(odd)
    print(num)

