# Created function because of repeated code
def outcome(x,y):
    result = f"first number: {x}\nsecond number: {y}"
    return result

# getting values and assinging them to variables 
num1 = input("enter a number ")
num2 = input("enter another number ")

# printing out values before the swap
print(outcome(num1,num2))

# swapping the numbers around 
holder = None
holder = num1 
num1 = num2
num2 = holder 


# printing values after the swap
print("\n",outcome(num1,num2))