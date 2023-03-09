import datetime

def no_duplicates(usn, usn_flag):
    '''
    
    '''
    usrfile = open("user.txt","r")
    data = usrfile.readlines()
    for line in data:
        words = line.split(",")
        if words[0] == usn:
            usn_flag = True
            print("This username is already in use. Try again: \n")
        else:
            
            usn_flag = False
    return usn_flag




def confirm_details(usn, flag):
    #-------------- password check ------------
    # while block confirms usr pswd and adds to 
    # a list
    #------------------------------------------
    
    while flag == True:
        usn_flag = True

        while usn_flag == True:
            new_usr = input("Enter a new usr: ")
            usn_flag = no_duplicates(new_usr,usn_flag)

        new_pswd = input("Enter new password: ")
        confirm_pswd = input("Confirm new password: ")
        if confirm_pswd == new_pswd:
            new_login = [new_usr, new_pswd] 
        break
        print("Error!\npasswords do not match, start again. ")

    return new_login


def reg_user(usn):
    #------------- Writing to file ---------------
    # Use list created in confirm details function
    # populate text file
    #---------------------------------------------
    if usn != "admin":
        admin_flag = False
        print("Only admin user has this permission!\n")
    else:
        admin_flag = True
        new_login = confirm_details(usn, admin_flag)
        usr_file = open("user.txt","a+")
            
        usr_file.write(f"\n{new_login[0]}")
        usr_file.write(f", {new_login[1]}")
        
        print("\nuser has been added: \n")
        usr_file.close()


def add_task():
    while True:
        whos_tsk = input("What usr are you assigning the task to?: ")
        users = userList()
        if whos_tsk in users:
            break
        if whos_tsk not in users:
            print("This user does not exist, try again: ")
        
    task_name = input("Please name the task: ")
    task_desc = input("Please provide a task description: ")
    task_due = input("The format of dd month yyyy please enter the due date of the task: \n")
    task_set = datetime.date.today()
    task_set.strftime("%d %b %Y")
    tsk_complete = ["Yes","No"]
    
    rtask_file = open("tasks.txt","a+")
    rtask_file.write(f"\n{whos_tsk}, {task_name}, {task_desc}, {task_set}, {task_due}, {tsk_complete[1]}")
    rtask_file.close()

def view_all():
    rtask_file = open("tasks.txt","r")
    data = rtask_file.readlines()

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

    rtask_file.close() 

def view_mine(usn_choice):
    rtask_file = open("tasks.txt","r+")
    data = rtask_file.readlines()
    
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
            output += f"Task Complete?\t\t{tsk_complete}"
            output += f"Task description:\n{task_desc}\n"
            print(output)
            flag = True
        else: 
            print("You have no task!")
            flag = False
            break

    edit_task(flag,data,rtask_file)

    rtask_file.close()
#------------------------------------------------------------------

def edit_task(flag,data,rtask_file):
    #---------------------------------------------
    # Edit task data block
    # Collect user input and use it to specify which
    # index position the task they want to edit is in
    # within the "data[]" variable above
    #---------------------------------------------
    while flag:
        edit_choice = int(input("Please select a task to edit by its number header or enter -1 to exit back to the main menu:  "))
        tsk_choice = edit_choice - 1
        if edit_choice > 0 and edit_choice <= len(data):

            while True:
                output = f"------------Select an Option -------------\n"
                output += f"1 - Mark as completed\n"
                output += f"2 - Edit Task \n"
                output += f"-----------------------------------------\n"
                print(output)

                option_choice = int(input(": "))

                task = data[tsk_choice].split(",")

                if option_choice == 1:
                    #-------- Replacing data ------
                    # splits list into a another list "task"
                    # Makes a change in "task" and joins it to a new list "new_data"
                    # Replace changed data with original user selected task
                    #------------------------------
                    
                    task[-1] = "Yes\n"
                    new_data = ",".join(task)
                    data[tsk_choice] = new_data
                    #------- Writing to file ------
                    # write the changes from previous block into file
                    #------------------------------
                    wtask_file = open("tasks.txt","w")
                    for line in data:
                        wtask_file.write(line)
                    wtask_file.close()
                    

                elif option_choice == 2 and task[5] == " No":                                
                    #-------------- EDIT and write to file --------------
                    # editing and writing username and due date of 
                    # user selected task
                    #----------------------------------------------------
                    output = f"------------Select an Option -------------\n"
                    output +=f"cu - to change the user the task is assigned to\n"
                    output +=f"cd - to change the due date of the task\n"
                    output += "-------------------------------------------\n"
                    
                    choice = input(output)
                    if choice.lower() == "cu":
                       
                        task = data[tsk_choice]
                        task[0] = input("Which user are you assigning this task: ")
                        new_data = ".".join(task)
                        data[tsk_choice] = new_data
                        
                        wtask_file.open("tasks.txt","w")
                        for line in data:
                            wtask_file.write(line)
                        wtask_file.close()
                    
                    if choice.lower() == "cd":
                        task = data[tsk_choice]
                        task[4] = input("The format of dd/month/yyyy please enter the due date of the task: \n")
                        new_data = ",".join(task)
                        data[tsk_choice] = new_data
                        
                        wtask_file = open("tasks.txt","w")
                        for line in data:
                            rtask_file.write(line)
                    
                        wtask_file.close()
                        
                        
                else:
                    print("wrong input. Try again!: ")    

                
        elif edit_choice == -1:
            break

        else:
            print("You have selected and invalid number. Try again!: ")

    
def readFile(filename):
    # Function to read tasks into a list 
    # Returns this information for other functions to use
    rtasks = open(filename,"r")
    data = rtasks.readlines()
    rtasks.close()

    return data

def numTasks(name=None):
    data = readFile("tasks.txt")
    # Function that takes a list returned bt read tasks
    # calculates the length of the list to determine number of tasks
    if name == None:

        return len(data)
    else:
        count = 0
        for line in data:
            task = line.split(",")
            if name == task[0]:
                count += 1
        
        return count

def numCompleted(name = None):
    data = readFile("tasks.txt")
    numCompleted = 0
    if name == None:
        for task in data:
            split_task = task.split(",")
            if split_task[5] == " Yes" or split_task[5] == "Yes\n":
                numCompleted += 1
    else:
        for task in data:
            split_task = task.split(",")
            if split_task[0] == name and (split_task[5] == " Yes" or split_task[5] == " Yes\n"):
                numCompleted += 1
        
    return numCompleted

def numUncompleted(name = None):
    data = readFile("tasks.txt")
    count = 0
    if name == None:
        for task in data:
            split_task = task.split(",")
            if split_task[5] == " No" or split_task[5] == " No\n":
                count += 1
    else:
        for task in data:
            split_task = task.split(",")
            if split_task[0] == name and (split_task[5] == " No" or split_task[5] == " No\n"):
                count += 1

    return count

#-----------------------------
# Checks if 

def numOverdue(name = None):
    data = readFile("tasks.txt")
    if name == None:
        for task in data:
            split_task = task.split(",")
            due_date = split_task[4].strip(" ")
            count = 0
            if split_task[5] == " No" or split_task[5] == " No\n":
                today = datetime.datetime.today() 
                date_object = datetime.datetime.strptime(due_date, "%d %b %Y")
                if date_object < today:
                    count += 1
    else:
         for task in data:
            split_task = task.split(",")
            due_date = split_task[4].strip(" ")
            count = 0
            if split_task[0] == name and (split_task[5] == " No" or split_task[5] == " No\n"):
                today = datetime.datetime.today() 
                date_object = datetime.datetime.strptime(due_date, "%d %b %Y")
                if date_object < today:
                    count += 1

    return count
'''
REFERENCE
stackoverflow, 10/2/2010, Parse date string and change format, [Forum], available: https://stackoverflow.com/questions/2265357/parse-date-string-and-change-format accessed 01/02/2023

'''

#-----------------------------------------
# Function to put all user names in a list 
#-----------------------------------------
def userList():
    data = readFile("user.txt")
    user_list = []
    for user in data:
        split_user = user.split(",")
        user_list.append(split_user[0])
    
    return user_list

#--------------------------
# Writes stats of each user to text file
#--------------------------

def eachUser():
    user_list = userList()
    file = open("user_overview.txt","w")
    for user in user_list:
        file.write(f"""                 ---------{user}---------
        Number of tasks assigned:       {numTasks(user)}
        Percentage of tasks assigned:   {(numTasks(user)/numTasks())*100}
        Percentage of tasks Completed:  {percentage(numCompleted(user),numTasks(user))}
        Percentage of tasks incomplete: {percentage(numUncompleted(user),numTasks(user))}
        Percentage Overdue:             {percentage(numOverdue(user),numTasks(user))}
         """)
    file.close() 

#-----------------------
# Function calculates percentages
# Makes sure to avoid errors by avoiding zero division
#-----------------------
def percentage(a, b):
    if b != 0:
        result = (a / b) * 100
    else:
        result = "0.0%"
    
    return result
    

def numUsers():
    data = readFile("user.txt")
    # Function that takes a list returned bt read tasks
    # calculates the length of the list to determine number of tasks
    return len(data)


#---------------------------
#  Creates files with stats
#--------------------------                
def generate_report():
    file = open("task_overview.txt","w")
    
    
    
    file.write(f""" Task Overview Report:
    Number of tasks tracked:            {numTasks()}
    Total number of completed tasks:    {numCompleted()}
    Total number of uncompleted tasks   {numUncompleted()}
    Total number of overdue tasks:      {numOverdue()}
    Percentage incomplete:              {percentage(numUncompleted(),numTasks())}%
    Percentage of tasks overdue:        {percentage(numOverdue(),numTasks())}%""")
    file.close()

    file = open("user_overview.txt","w")

    file.write(f""" User Overview Report:
    Number of users:        {numUsers()}
    Total number of tasks:  {numTasks()}
     """)

    eachUser()


#------------------------------
# Function that prints data from files onto console
#-------------------------------
def printStats():
                                
    task_data = readFile("task_overview.txt")
    user_data = readFile("user_overview.txt")
    for line in task_data:
        print(line)

    print()

    for line in user_data:
        print(line)
