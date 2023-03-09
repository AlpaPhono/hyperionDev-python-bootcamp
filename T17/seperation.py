#**************** COMPOLSORY TASK 2 *******************
#.Write a program that inputs a sentence and then
#.Displays each word of the sentence on a seperate line
#******************************************************

#---------------- Variables --------------------
string = "I am learning to code"
#------------------ Process --------------------
def seperation(s):
    ''' 
    This function splits the words in a string
    into a list
    then the print function is used
     to print each item into a new line
     '''

    lst = []
    lst = s.split(" ")

    for i in lst:
        print(i)

seperation(string)
