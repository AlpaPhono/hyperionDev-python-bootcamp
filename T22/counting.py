#****************** Compulsory Task 3 *****************
# Count the number of times a character occurs in a string
#******************************************************

#----------------- Variable declaration -----------
# Dictionary to be updated 
# Alphabet to iterate through
#--------------------------------------------------
sample_string = "google.com"
char_occurrence = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"

#------------------ Process ----------------------
# Nested for loop that matches letters of the alphabet
# with letters in the sample string
# every time there is a match a counter is incremented 
# values get placed in char_occurrence and then printed at the end
#-------------------------------------------------
for letter in alphabet:
    count = 0
    if letter in sample_string:
        for char in sample_string:
            if char == letter:
                count +=1

            char_occurrence.update({letter: count})

print(char_occurrence)    
