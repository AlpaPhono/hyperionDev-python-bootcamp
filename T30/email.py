#******************************
# An Email Simulation
#******************************

# Create a class definition for an email with four variables
#
class Email():
    # Class Variables 
    has_been_read = True
    email_contents = ""
    is_spam = True
    from_address = ""


    def __init__(self,from_address,email_contents):
        self.has_been_read = False
        self.is_spam = False
        self.from_address = from_address
        self.email_contents = email_contents

 
    def mark_as_read(self):
        """changes has_been_read variable to True"""
        self.has_been_read = True

    def mark_as_spam(self):
        """Changes is_spam to True"""
        self.is_spam = True

def add_email(from_address, email_contents):
    '''Creates email object and appends to inbox list.
    
    Keyword arguments:
        from_address -- the senders address
        email_contents -- content of the email
        '''
    email = Email(from_address,email_contents)
    inbox.append(email)

def get_count():
    '''Returns length of inbox list'''
    return len(inbox)

def get_email(i):
    email = inbox[i]
    contents = email.email_contents
    email.mark_as_read()
    return contents
    
def get_unread_emails():
    unread = []
    for email in inbox:
        if email.has_been_read == False:
            unread.append(email)
    
    return unread


def get_spam_emails():
    spam = []
    for email in inbox:
        if email.is_spam == True:
            spam.append(email)
    
    return spam


def delete(i):
    inbox.pop(i)

def email_select(option):
    """Allows user to specify which email they want to read from inbox;

    Keywords:
        option (str): a string to edit consol output based on user input.
    
        Returns:
        A list with user selected email choice and email position"""
    num_emails = get_count()
    print(f"Enter the numerical position of the email you want to {option}.\n")
    pos = int(input(f"There are {num_emails} Emails in your inbox.\nWhich would you like to {option}?\n"))
    email_choice = inbox[pos]

    return [email_choice, pos]

def send_email():
    '''Creates email object from user input, Adds to outbox list'''
    address = input("Enter your email address")
    message = input("Enter message")
    send_mail = Email(address,message)
    email = Email(address, message)
    #email.contents = message
    outbox.append(email)
    print("Email sent!")
        
        



inbox = []
outbox = []



user_choice = ""

add_email("welcome@info.com","This is your first email!")

while user_choice != "quit":
    user_choice = input("What would you like to do - read/mark spam/send/delete/quit?")
    if user_choice == "read":
        email_choice = email_select(user_choice)
        email = email_choice[0]
        inbox_pos = email_choice[1]
        
        sender = email.from_address
        contents = get_email(inbox_pos)
        print(f"Email from: {sender}\nmessage:\n{contents}")
        
    
    elif user_choice == "mark spam":
        email_choice = email_select(user_choice)
        email_choice[0].mark_as_spam()
        
        
    elif user_choice == "send":
        send_email()
    elif user_choice == "delete":
        print("\nThe emails are ordered in index notation email 1 = 0, email 2 = 1 ect.")
        email_choice = email_select(user_choice)
        delete(email_choice[1]) 
    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")