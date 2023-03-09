#.************* COMPULSORY TASK ************
#. Write a program that reads data from the
#. text file called DOB.txt and prints it out
#. in two different sections in the format
#. displayed
#*******************************************
'''
contents = ""

with open("DOB.txt","r+") as f:
    for line in f:
        contents = contents + line
        print(contents)
'''

import re
#--------------- Process 1 -----------------
# Using regular expressions to extract the second_attempt_names from the text
#----------------------------------------
print("\nThis is the solution using regular expressions\nI did this by accident:\n\n")
f = open('DOB.txt','r')
text = f.read()

#------------------- Explaining this block -------
# name_matches searches the text
# for any occurances that fit the pattern
#  
name_pattern = r'^\w+\s\w+'
name_matches = re.findall(name_pattern, text, re.MULTILINE)             #re.MULTILINE forces the ^ symbol to match at the beginning of each line of text

print("Name")
for name in name_matches:
    print(name)

print()


#--------------- Process 2 -----------------
# Using regular expressions to extract the birthdates from the text
#----------------------------------------

date_pattern = r'(?:0[1-9]|[12][0-9]|3[01])\s(?:\D*)\s(?:\d*)'            # To stop it creating tuples use (?:)
      
date_matches = re.findall(date_pattern, text)                  
print(date_matches)

print("Birthdate")
for date in date_matches:
    print(date)

f.close()


#*********************** After a one to one *******************
# I learnt I didnt have to use regular expressions
# Here is the result without it 
#**************************************************************
print("\nThis is the attempt after doing the one to one with Christiaan")

with open("DOB.txt","r") as dob_file:
    data = dob_file.readlines()

    print("\nName:")
    for line in data:
        line_list = line.split()
        print(f"{line_list[0]} {line_list[1]}")
        #second_attempt_names.append(line_list[0])
        #second_attempt_names.append(line_list[1])

    print("\nBirthdate")
    for line in data:
        line_list = line.split()
        print(f"{line_list[2]} {line_list[3]}")



#************* REFERENCES ***************
# regexmagic, (n.d) [website]- https://www.regular-expressions.info/dates.html accessed (10/01/2023)
# bhairvav.s (7/3/13) [EMAIL]- [Tutor] Fwd: findall() returns tuples or string? https://mail.python.org/pipermail/tutor/2013-March/094172.html accessed (10/01/2023)
# jastrzebsji.N (n.d) [BLOG]- RefEx - Extractig the first N words, accessed (10/01/2023) https://www.theinformationlab.co.uk/2020/01/03/regex-extracting-the-first-n-words/
# Christiaan Joubert hyperion dev tutor