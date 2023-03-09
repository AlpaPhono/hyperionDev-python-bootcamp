#************************* COMPULSORY TASK ************************
# Program to calculate the costs of sending a parcel.
#******************************************************************

#================ VARIABLES =======================================

price = float(input("How much is the package: "))
distance = float(input("Total distance of delivery in kms: "))
air = True
full_insurance = True
Gift = True
priority = True
cost = None
total_cost = 0

#==================== Process =====================
delivery_type = input("air or freight")
if delivery_type.upper() == "AIR":
    air = True
    cost = 0.36 * distance
else:
    air = False
    cost = 0.25 * distance
total_cost += cost

insurance = input("Full insurance. YES or NO: ")
if insurance.upper() == "YES":
    full_insurance = True
    cost = 50.00
else:
    full_insurance = False
    cost = 25.00
total_cost += cost

is_gift = input("Gift: YES or NO: ")
if is_gift.upper() == "YES":
    Gift = True
    cost = 15.00
else:
    Gift = False
    cost = 0
total_cost += cost


is_priority = input("priority delivery: YES or NO: ")
if is_priority.upper() == "NO":
    priority = False # I think this is a more efficient way to do my if statemnts that reduces the amount of code I write in comparison to previous if blocks in this file.
    
    if priority == False:
        cost = 20.00
    else:
        cost = 100.00
total_cost += cost

print(f"The total cost for delivery will be: {total_cost}")




