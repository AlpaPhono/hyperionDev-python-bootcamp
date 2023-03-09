#***************** COMPULSORY TASK 1 ***************
#
#***************************************************

def numbersList ():
    '''Stores user input in variable, returns the variables in a list'''
    num1 = inputCheck()
    num2 = inputCheck()
    numbers = [num1,num2]
    return numbers 

def inputCheck():
    '''Confirms valid user input, Returns the value'''
    while True:

        num = input("Please enter a number: ")

        if num.isnumeric():
            num = int(num)
            break
        else:
            print("You have entered an invalid number. Please enter a whole number: ")

    return num


def OperatorSelection():
    '''Compares user input to list of strings; Returns input when '''
    symbols = ["+","-","x","/"]
    while True:
        operator = input("Please select from the following options what calculation you would like to do with these two numbers '+,-,x,/': ")
        if operator not in symbols:
            print("Wrong input, try again: ")
        else:
            break
    
    return operator
    
def addition(numbers):
    "Takes list of numbers; returns the sum of the first two index positions"
    total = numbers[0] + numbers[1]
    return total 

def subtraction(numbers):
    "Takes list of numbers; returns the subtraction of the first two index positions"
    if numbers[1] > numbers[0]:
        print("This subtraction will lead to a negative value. This isn't supported Try again.")
        numbersList()
    else:
        total = numbers[0] -  numbers[1]

    return total 

def multiplication(numbers):
    "Takes list of numbers; returns the multiplication of the first two index positions"

    total = numbers[0] * numbers[1]
    return total

def division(numbers):
    if numbers[1] == 0:
        print("Second number can not be 0: ")
        return

    return numbers[0] / numbers[1]
    



def main():
  count = 0
  file = open("calculations.txt","w")
  while count < 3:
    
    numbers = numbersList() 
    operator = OperatorSelection()
    

    if operator == "+":
        add = addition(numbers)
        addition_total = f"{numbers[0]} + {numbers[1]} = {add}\n"
        print(addition_total)
        file.write(addition_total)
        count += 1

    if operator == "-":
        subtract = subtraction(numbers)
        subtraction_total = f"{numbers[0]} - {numbers[1]} = {subtract}\n"
        file.write(subtraction_total)
        print(subtraction_total)
        count += 1

    if operator == "x":
        multiply = multiplication(numbers)
        multiplication_total = f"{numbers[0]} x {numbers[1]} = {multiply}\n"
        file.write(multiplication_total)
        print(multiplication_total)
        count += 1

    if operator ==  "/":
        divide = division(numbers)
        divide_total = f"{numbers[0]} / {numbers[1]} = {divide}"
        file.write
    while True:
        usr_exit = input("Would you like to continue? Y/N: ")
        if usr_exit.upper() == "N":
            exit()
        elif usr_exit.upper() == "Y":
            break
            continue
            
        else:
            print("Wrong input, Try again")

  file.close()

    
def menu():
    while True:
        usr = str(input("Please select between the following options: \nEnter 'A' To do calxculations:\nEnter 'B' to view previous calculations:\n"))
        usr = usr.upper()
        if usr == "A" or usr == "B":
            break

        else:
            print("Wrong input, Try again: ")


    if usr.upper() == "A":
        main()
    if usr.upper() == "B":
        readFile()
       


def readFile():
    file = None
    usr_file = input("Enter file name: ")
    try:
        file = open(usr_file,"r")
        lines = file.readlines()
        for line in lines:
            print(line)
           
            
    except FileNotFoundError as error:
        print("The file you are trying to open does not exist")
    finally:
        if file is not None:
            file.close()


if __name__ == "__main__":
    menu()
    
    