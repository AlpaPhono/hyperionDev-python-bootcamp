#============= Compulsory Task 2 ===============
#

import math

flag = True

# Error check loop to ensure user enters required values
while flag:
    shape = input("Enter the shape of the building: Square, Rectangular or Round") # Requesting input
    if shape.upper() == "SQUARE" or shape.upper() == "RECTANGULAR" or shape.upper() == "ROUND":
        flag = False
    else:
       print("error try again")

# Prompting for appropriate dimensions

# if square was the input
if shape.upper() == "SQUARE":
    length = float(input("what is the length of the square"))
    area = length **2 # area of swaure is lxl
    print(f"The foundation of your building will take up an area of {area}")

# if user entered rectangular as their input    
elif shape.upper() =="RECTANGULAR":
    length = float(input("what is the length"))
    width = float(input("What is the width"))
    area = length * width
    print(f"The foundation of your building will take up an area of {area}")
    
    # if round was the input
elif shape.upper() == "ROUND":
    radius = float(input("What is the radius of the foundation"))
    area = math.pi * radius**2
    print(f"The foundation of your building will take up an area of {area}")

