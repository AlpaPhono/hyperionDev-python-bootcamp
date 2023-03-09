#****************** Compulsory task 2 **************
# Program that calculates to cost of a holiday
#***************************************************

#******************* Functions **********************
#---------------- Hotel cost func -------------------
#
#----------------------------------------------------
def hotel_cost(nights):
    price = 50.00
    total_cost = price * nights
    return total_cost

#-------------------- Plane cost func ----------------
#
#-----------------------------------------------------
def place_cost(city):
    price = 0
    if city == "London":
        price = 100
        print(f"£{price}")
    if city == "Lisbon":
        price = 120
        print(f"£{price}")

    return price

#---------------------- Car rent func ----------------
#
#-----------------------------------------------------
def car_rental(days):
    price = 90.00
    total_cost = price * days
    return total_cost

#----------------- Holiday cost func ----------------
#
#---------------------------------------------------

def holiday_cost(nights,city,days):
    total_cost = hotel_cost(nights) + place_cost(city) + car_rental(days)
    return total_cost
#--------------- Variables ----------------
#
#-----------------------------------------
num_of_nights = int(input("How many nights will you be staying at the hotel? "))
city_choice = input("What city, London or Lisbon: ")
num_of_car_days = int(input("How many days will you rent the car for? "))

#------------- Function calls -----------
#
#----------------------------------------

hotel = hotel_cost(num_of_nights)
flight = place_cost(city_choice)
car = car_rental(num_of_car_days)
total = holiday_cost(num_of_nights,city_choice,num_of_car_days)

print(f"--------------Holiday Breakdown---------------\nCost of hotel:\t\t\t{hotel}\nCost of flights:\t\t{flight}\nCost of rental:\t\t\t{car}\nTotal Expenditure:\t\t{total}")


