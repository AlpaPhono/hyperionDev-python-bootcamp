#********** OPTIONAL TASK *************
# Write a program that will count
# The number of char words and lines in a file
# also count the number of vowels
#**************************************

file = open("input.txt", "r")
words = 0
#---------- Number of lines------------
# First block of code strips the text of all new line characters
# Then converts the string into a list
#--------------------------------------
text = file.read()
text.strip("\n")
lines = text.split("\n")

#------------ Process -----------------
# The for loop removes all empty lines from the list
#-------------------------------------
'''
for line in lines:
    current_line = line.split()
    if line == "":
        lines.pop(lines.index(line))
        
    words += len(current_line)

Why does the if statement in this code affect the number of words added when its only 
supposed to pop the valus that hold nothing?
'''
for line in lines:
    current_line = line.split()
    words += len(current_line)
    for word in current_line:
        char +







total_number_of_lines = len(lines)
print(f"Total number of lines is:\t{total_number_of_lines}")
print(f"Total number of words are:\t{words}")


#---------- Number of Words -----------
for line in lines:
    pass

file.close()