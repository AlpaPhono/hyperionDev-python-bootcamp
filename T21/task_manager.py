#************** CAPSTONE II ****************
#=====importing libraries===========
'''This is the section where you will import libraries'''
import datetime

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
#------------------------------
# Reading from user.txt file and storing information in variables
#------------------------------
usr_file = open("user.txt","r")
lines = usr_file.readlines()
users = {}
flag = True

for pos, line in enumerate(lines):
    split_line = line.split(",")

    for index, word in enumerate(split_line):
        split_line[index] = word.strip()
        split_line[index] = word.strip("\n")
    users.update({split_line[index -1]: split_line[index]})

usn_request = "Please enter your username: "
password_request = "Please enter your password: "

#----------------------------
# While loop 
# Matching usr input with text data that is stored in variables
# Closing file
#----------------------------

while flag:
    usn_choice = input(usn_request)
    password_choice = input(password_request)
    auth_pass = users.get(usn_choice)
    auth_pass = auth_pass.strip()                           # Had issues with passwords not authenticating due to format.
    if password_choice != auth_pass: 
        print("Error Try again: ")
    else:
        flag = not flag
        print("\n\n")

usr_file.close()

while True:
    # presenting the menu to the user based on username and 
    # making sure that the user input is converted to lower case.
    if usn_choice != "admin":
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()
    else:
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    s - Statistics
    va - View all tasks
    vm - view my task
    e - Exit
    : ''').lower()



    if menu == 'r':
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''

       #-------- Confirming usr is admin ----------
       #    While loop is controlled by the 
       #    admin flag in the if else block
       #-------------------------------------------
        if usn_choice != "admin":
            admin_flag = False
            print("Only admin user has this permission!")
        else:
            admin_flag = True
        #-------------- password check ------------
        # while block confirms usr pswd and adds to 
        # a list
        #------------------------------------------     
            while admin_flag == True:
                new_usr = input("Enter a new usr: ")
                new_pswd = input("Enter new password: ")
                confirm_pswd = input("Confirm new password: ")
                if confirm_pswd == new_pswd:
                    new_login = [new_usr, new_pswd] 
                break
                print("Error!\npasswords do not match, start again. ")
            #------------- Writing to file ---------------
            # Use list created in previous while loop
            # populate text file
            #---------------------------------------------

            usr_file = open("user.txt","a+")
            
            usr_file.write(f"\n{new_login[0]}")
            usr_file.write(f", {new_login[1]}")
            
            print("\nuser has been added: \n")
            usr_file.close()
            


    elif menu == 'a':
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

        whos_tsk = input("What usr are you assigning the task to?: ")
        task_name = input("Please name the task: ")
        task_desc = input("Please provide a task description: ")
        task_due = input("The format of dd/month/yyyy please enter the due date of the task: \n")
        task_set = datetime.date.today()
        tsk_complete = ["Yes","No"]
        
        task_file = open("tasks.txt","a+")
        task_file.write(f"\n{whos_tsk}, {task_name}, {task_desc}, {task_set}, {task_due}, {tsk_complete[1]}")
        task_file.close()

    elif menu == 'va':
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''

        task_file = open("tasks.txt","r")
        data = task_file.readlines()
        
        #-------------- Outputting + formatting file data -----------
        # For block that counts the position of each line 
        # splits the line into its sections at comma position
        # String manipulation to format output of data
        #------------------------------------------------------------
        for position, line in enumerate(data,start=1):
            section = line.split(",")
            whos_tsk = section[0]
            task_name = section[1]
            task_desc = section[2]
            task_set = section[3]
            task_due = section[4]
            tsk_complete = section[5]

            output = f"------------{position}-------------\n"
            output += f"Task:\t\t\t{task_name}\n"
            output += f"Assigned to::  \t\t{whos_tsk}\n"
            output += f"Date assigned:\t\t{task_set}\n"
            output += f"Due date:\t\t{task_due}\n"
            output += f"Task Complete?\t\t{tsk_complete}\n"
            output += f"Task description:\n{task_desc}\n"
            print(output)

        task_file.close()



        

    elif menu == 'vm':
        
        '''In this block you will put the code that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''
        
        task_file = open("tasks.txt","r+")
        data = task_file.readlines()
        
        #-------------- Outputting + formatting file data -----------
        # For block that counts the position of each line 
        # splits the line into its sections at comma position
        # String manipulation to format output of data
        #------------------------------------------------------------
        for position, line in enumerate(data,start=1):
            section = line.split(",")
            whos_tsk = section[0]
            task_name = section[1]
            task_desc = section[2]
            task_set = section[3]
            task_due = section[4]
            tsk_complete = section[5]
            
            if whos_tsk == usn_choice:
                output = f"------------{position}-------------\n"
                output += f"Task:\t\t\t{task_name}\n"
                output += f"Assigned to::  \t\t{whos_tsk}\n"
                output += f"Date assigned:\t\t{task_set}\n"
                output += f"Due date:\t\t{task_due}\n"
                output += f"Task Complete?\t\t{tsk_complete}\n"
                output += f"Task description:\n{task_desc}\n"
                print(output)

                


        task_file.close()
    
    elif menu == "s":
        if usn_choice != "admin":
            exit()
        else:
            total_tasks = 0
            total_usrs = 0
            
            task_file = open("tasks.txt","r")
            task_data = task_file.readlines()
            total_tasks = len(task_data)
            task_file.close()

            usr_file = open("user.txt","r")
            usr_data = usr_file.readlines()
            total_usrs = len(usr_data)
            
            print(f'''Program Statistics:
            
                Number of Users:    {total_usrs}
                Number of Tasks:    {total_tasks} 
            
            ''')



    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")