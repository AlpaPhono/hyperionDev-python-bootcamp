#*************** Optional Task***************************#

import math

def make_list(item,items):
    
    item = int(input("please enter the length of one side of a triangle" )) # Ask user for lengths of a triangle
    items.append(item) # added them to a list because I thought it would be useful... I was wrong

    return item

def tri_area(s1,s2,s3):
    s = (s1+s2+s3)/2 
    area = math.sqrt((s*((s - s1)*(s-s2)*(s-s3))))
    print(area)

'''
Above the function calculcartes and prints the area of a triangle based off of the users numbers.

I probably could find a way to combine the two functions into one
'''

#=============== Declaring variables =================
side1 = None
side2 = None
side3 = None

sides = []

#=========== Processing ======================
side1 = make_list(side1,sides)
side2 = make_list(side3,sides)
side3 = make_list(side3,sides)

tri_area(side1,side2,side3)













################### UPDATE 15/12/22 ################################
# THE CALCULATIONS ARE FINE I WAS USING A BAD SET OF NUMBERS 1,2,3


# I initally converted the inputs into ints, But i was getting the answer of 0
# So I decided to convert the inputs into floats
#
# What is a math domain error: 
#   raised when you use a number that is not supported by a mathematical opertion, commonly with sqrt() and log()
#   using negative or zero number where we should not be. (careerKarma.com)
#

# ++++++++++++++++++ References +++++++++++++++++++++++
# James Gallagher. 23 Feb 2021. careerKarama.com. Python ValueError: math domain error Solution [online] Accessed: 14/12/2022. Available from: https://careerkarma.com/blog/python-valueerror-math-domain-error/#:~:text=The%20Python%20ValueError%3A%20math%20domain,and%20the%20log()%20method.

