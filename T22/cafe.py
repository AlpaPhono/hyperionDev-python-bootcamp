#*********************** Compulsory task 1 **************
# Create list called menu that has 4 items from the cafe
#********************************************************

menu = ["tea", "coffee","bread","water"]

#---------------------------
# Create a dictionary called stock
# contains the stock value of each item in menu
#---------------------------
stock ={
    menu[0]: 3,
    menu[1]: 12,
    menu[2]: 2,
    menu[3]: 1
}

#-------------------------
# Create dictionary called price
# Contains prices of each item in menu
#-------------------------

price = {
    menu[0]: 4.00,
    menu[1]: 5.00,
    menu[2]: 2.00,
    menu[3]: 1.00
}

#--------------------
# Calculate the total stock worth in cafe
# loop through the appropriate dictionaries and lists
#-------------------

for index, item in enumerate(menu):
    stock_worth = price[item] * stock[item]
    print(f"The stock worth of {item} is:  {stock_worth}\n")