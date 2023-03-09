#************** Compulsory Task 1 **************
# Function that prints all the days of the week
#***********************************************

def days_of_week():
    days = ["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    for day in days:
        print(day)

days_of_week()

#----------------- Replace function -------------
# Function that replaces every second word with hello
#-----------------------------------------------

def replace(input):
    sentence = str(input).split()
    empty_string = ""
    for index, word in enumerate(sentence, start = 1):
        if index % 2:
            sentence[index] = "Hello"
    
    for word in sentence:
        empty_string += word + " " 

    return empty_string

random_string = "I am gonna be King Of The Pirates!"

print(replace(random_string))
