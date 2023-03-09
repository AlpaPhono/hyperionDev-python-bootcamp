# Create an adult Class with the following Attributes and method 
# - name, age, eye_colour and hair colour
# - Method called can_drive() that prints the name of the person and that they are old enough to drive

class Adult():

    def __init__(self,name,age,eye_colour,hair_colour):
        self.name = name
        self.age = age
        self. eye_colour = eye_colour
        self.hair_colour = hair_colour

    def can_drive(self):
        print(f"{self.name} is old enough to drive")

# Create a subclass of the adult class named "Child" that has the same 
# attributes but overrides the can_drive method to print the persons name 
# and that they are too young to drive

class Child(Adult):
    
    
    def can_drive(self):
        print(f"{self.name} is too young to drive")


# Take user inputs that ask for the name, age, hair, colour, eye colour of a person
catagory = ["name","age","hair colour","eye colour"]
person = []
for i in catagory:
    usr_input = input(f"Please enter a value for {i}: ")
    person.append(usr_input)

# create some logic that determines if the person is 18 or older and create an
# instance of the Adult class if this is true 
# Otherwise create an instance of the Child class 
# Once the object has been created, call the can_drive() method 
# to print out whether the person is old enough to drive or not
person[1] = int(person[1])
if person[1] > 18:
    adult = Adult(person[0],person[1],person[3],person[2])
    adult.can_drive()
else:
    child = Child(person[0],person[1],person[3],person[2])
    child.can_drive()