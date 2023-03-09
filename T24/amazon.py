#------------------ Compulsory Task 3 ---------------
# Code to read content from input.txt
#----------------------------------------------------

#-------------------- Functions ---------------------
#----------------------------------------------------
#                       Min function
#----------------------------------------------------
def min_func(numbers):
    output = min(numbers)
    return output

#----------------------------------------------------
#                   Max Function
#----------------------------------------------------
def max_func(numbers):
    output = max(numbers)
    return output

#-----------------------------------------------------
#                   avg function
#-----------------------------------------------------
def avg_func(numbers):
    output = 0
    for num in numbers:
        output += num
    output / len(numbers)
    return output


#------------------- Read file ----------------------
# Read data from file
# nested for block reads numbers and turns into a list variable
#       and converts the items into int
#----------------------------------------------------
infile = open("input.txt","r")
data = infile.readlines()
for index, line in enumerate(data):
    new_line = line.split(":")
    new_line.pop(0)
    #print(new_line)
    numbers_string = new_line[0]
    numbers_string = numbers_string.strip("\n")
    numbers_list = numbers_string.split(",")
    for pos, i in enumerate(numbers_list):
        numbers_list[pos] = int(i)


infile.close()


outfile = open("output.txt","w+")
outfile.write(f"The min of {numbers_list} is {min_func(numbers_list)}\n")
outfile.write(f"The max of {numbers_list} is {max_func(numbers_list)}\n")
outfile.write(f"The avg of {numbers_list} is {avg_func(numbers_list)}\n")

outfile.close()