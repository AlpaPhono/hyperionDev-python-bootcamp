from tabulate import tabulate
if __name__ == "__main__":
    pass
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country 
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    def get_cost(self):
        
        '''
        Add the code to return the cost of the shoe in this method.
        '''
        return self.cost

    def get_quantity(self):
        '''
        Add the code to return the quantity of the shoes.
        '''
        return self.quantity

    def __str__(self):
        return f"Country: {self.country}\nCode: {self.code}\nProduct: {self.product}\nCost: {self.cost}\nQuantity: {self.quantity}"
        '''
        Add a code to returns a string representation of a class.
        '''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
print()
#==========Functions outside the class==============
def read_shoes_data():
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
    try:

        with open("inventory.txt","r") as file:    
            for start, line in enumerate(file):
                temp = line.strip()
                temp = temp.split(",")
                shoe = Shoe(temp[0],temp[1],temp[2],temp[3],temp[4])
                shoe_list.append(shoe)
    except FileNotFoundError:
        print(
            "File does not exist,"
            "\n Create file and try again"
        )
        exit()
    shoe_list.pop(0)

def capture_shoes():
    new_shoe = Shoe(country=input("Please enter country",code=input("Please enter code"),product="Please enter name of product",cost=input("Cost of the product"),quantity=input("please enter the quantity")))
    shoe_list.append(new_shoe)
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
def make_list():
    '''Read from file; store each line into a list variable'''
    info_list = []
    with open("inventory.txt","r") as file:
        for line in file:
            temp = line.strip()
            temp = temp.split(",")
            info_list.append(temp)

    info_list.pop(0)
    return info_list


def view_all():
    '''Creates a table from data in text file; prints table onto console'''
    header = ["Country","Code","Product","Cost","Quantity"]
    info_list = make_list()
    print(tabulate(info_list,headers = header,tablefmt = "fancy_grid"))


    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

def stock_write(num,shoe):
    """Re-writes inventory.txt file with updated stock numbers"""
    info_list = make_list()
    new_list = []
    for line in info_list:
        if line[1] == shoe.code:
            old_num = int(line[4])
            new_num = num + old_num
            line[4] = str(new_num)
        new_list.append(line)
    
    with open("inventory.txt","w") as file:
        header = ["Country","Code","Product","Cost","Quantity"]
        for word in header:
            file.write(word)
            file.write(",")
        file.write("\n")
        for line in new_list:
            for word in line:
                file.write(word)
                file.write(",")

            file.write("\n")
        

def re_stock():
    '''finds object in a list with the lowest "quantity variable"; user input writes a new value for it. '''
    lowest_quantity = min(shoe_list, key = lambda shoe: int(shoe.quantity))
    usr_choice = input(
        f"{lowest_quantity.product} has the lowest stock of: {lowest_quantity.quantity}"
    "\nWould you like to restock this product: Y/N: ")

    if usr_choice.upper() == "Y":
        num = int(input("How much more stock would you like to add?: "))
        old_number = int(lowest_quantity.quantity )
        new_number = old_number + num
        lowest_quantity.quantity = str(new_number)


        stock_write(num,lowest_quantity)
    
   
         
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

def search_shoe():
    usr_code = input("Please enter the code of the shoe you wish to find: ")
    for shoe in shoe_list:
        if shoe.code == usr_code.upper():
            return shoe
        

    
    
    pass
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    for shoe in shoe_list:
        value = int(shoe.cost) * int(shoe.quantity)
        print(f"The stock value of {shoe.product} is: {value}")
    
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    highest_quantity = max(shoe_list, key = lambda shoe: int(shoe.quantity))
    print(f"{highest_quantity.product} is for sale. ")


#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''


#==================References====================
#digital ocean str-repr functions 
#    https://www.digitalocean.com/community/tutorials/python-str-repr-functions