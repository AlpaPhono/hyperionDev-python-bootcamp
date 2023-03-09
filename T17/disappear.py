#*************** COMPULSORY TASK 3 *****************
# Program that strips a set of characters from a string
#***************************************************

#--------------- VARIABELS -------------------------
request = "Please enter a string: "
strip_request = "What characters would you like to make disappear: "
usr_string = input(request)             # string to be stripped
usr_strip = input(strip_request)        # chars to strip

#------------- Functions ---------------------------
def strip(string,strip):
    #new_string = ""
    for i in strip:
        string = string.replace(i,"")

    print(string)
#-------------- Process ----------------------------
strip(usr_string,usr_strip)


#****************** FAILED ATTEMPTS *****************
# Had to get 1to1 support with Chris Smitt
#****************************************************
'''
# I tried this as well

def strip(string,strip):
    new_string = ""
    for i in strip:
        for word in string:
            replace_word = ""
            if i in word:
                replace_word = word.replace(i,"")
                new_string = string.replace(word,replace_word)

    print(new_string)
'''

'''
def strip(string,strip):
    new_string = ""
    for i in strip:
        new_string = string.replace(i,"")

    print(new_string)

    WHY DIDNT THIS WORK?
    - because changes in the original string 
        weren't being saved into any variable 
'''