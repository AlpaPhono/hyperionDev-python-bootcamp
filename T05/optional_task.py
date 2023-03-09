# input users favorite restaurant 
fave_rest = input("what is your favourite restaurant? ")

# request favorite number
int_fave = int(input("What is your favourite number? "))

# two seperate print statements
print(fave_rest)
print(int_fave)

int(fave_rest)
#ValueError: Invalid literal for int() with base 10: 'kfc'
#This happens when you pass a string representation of a float or anything that is not an integer into the int() function (net-informations)
#This integers are typically base 10
#Base 10 is method of assigning a place value to numbers

# References
#net-informations.com. (n.a).[website] accessed:09/12/2022 Available from: http://net-informations.com/python/err/int.htm