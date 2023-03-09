#.*************** COMPULSORY TASK ************
# Create a program that reads in a string
# Makes each alternate character a uppercasecase character
# and each other alternate character a lowercase character
#*********************************************


#------------------- Variables ---------------
string = "Hello World"

#------------------ Process ------------------
'''
Function that takes a sentence and capitalises and lowercases each alternative character
It then returns the new sentence.
'''
def capitalise(s):
    newString = ""                              # string to hold new character values
    cap = True                                  # Bool variable to control when certain processes occur
    for char in s:                              # For loop to iterate throught string.

        # if captial flag is true turn current char upper
        # else make it lower 
        if cap:                                 
            newString += char.upper()           
        else:
            newString += char.lower()

            # If current char is not a space character 
            # swap the cap flag to its opposite value.
        if char.isalnum() == True:
            cap = not cap
    return newString


print(capitalise(string))

#===================== PART 2 ======================
#.Make each alternative word lower and upper case
#.Use split and join junctions
#==================================================


#--------------------- Variables -------------------
string2 = "I am learning to code"

#--------------------- Process ---------------------
def cap2(s):
    #------- Function Variables -------------
    
    cap_lst = []            # list for mutated values to be stored in
    lst = []                # list for string to be split into
    lst = s.split(" ")      # splitting words into list
    flag = True             # bool control variable
    empty_string = ""       # Empty string for join function      
    #----------------------------------------

    #------------ Function Process ---------
    
    for i in lst:
        if flag:
            cap_lst.append(i.upper(),)
            cap_lst.append(" ")
        else:
            cap_lst.append(i.lower())
            cap_lst.append(" ")

        flag = not flag
    
    empty_string = empty_string.join(cap_lst)
    print(empty_string)

    return empty_string

cap2(string2)
cap2(string)


    