
#==== Compulsory Task 2 ================
# Ask a user for names of three products
#

#=====  Functions =================

def is_it_twoDp(price,prod):
    flag = True
    while flag == True:
        two_dp = False

        while two_dp == False:
            try:
                price = input(f"how much is {prod} ")
                split_price = str(price).split(".")
                check_length = len(split_price[1])
                two_dp = True
            except:
                print("Please Enter price with 2 decimal places ")

        if check_length != 2:
            print("Please write price to two decimal places: ")
        else:
            flag = False
            
    
    return float(price)

#==== Declaring Variables ==============
request = "Enter a product name: "
prod1 = input(request)
prod2 = input(request)
prod3 = input(request)
products = [prod1,prod2,prod3]

# Ask for the price of each product, Each product must have two decimal values
#
#==== Declaring Variables ===============


price1 = None
price2 = None
price3 = None
#==== Casting Values into floats =======
# They need to be to 2 decimal place

price1 = is_it_twoDp(price1,prod1)
price2 = is_it_twoDp(price2,prod2)
price3 = is_it_twoDp(price3,prod3)

#================== Processing =====================
#
# Calculate the total of all three products.

total = price1 + price2 + price3
print(f"The Total is: {total}")

# Calculate the average price of the three products.
prices = [price1,price2,price3]
average = total /len(prices)

print(f"The average price of the three products is: {average}")

# print out The requested sentence

print(f"The Total of {prod1}, {prod2}, {prod3} is £{total} and the average price of the items is £{average}")

#*********************************************** References *************************************************************
# stackoverflow.com Python: only two decimal places after user entered number [forum] Accessed: 13/12/22 Available from: 
# https://stackoverflow.com/questions/23463705/python-only-two-decimal-places-after-user-entered-number




'''
def is_it_twoDp(price,prod):
    flag = True
    while flag == True:
        price = input(f"how much is {prod}")
        split_price = str(price).split(".")
        check_length = len(split_price[1])
        if check_length != 2:
            print("Please write price to two decimal places: ")
        else:
            flag = False
    
    return float(price)

    This was the original function used but if user input a number without a decimal it would cause an error when using the split(.)
    What I have to use is the try: except: thing  so that if an error throws up I can re route it.
'''