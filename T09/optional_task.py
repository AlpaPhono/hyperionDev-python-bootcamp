#************************** OPTIONAL TASK ***********************
# Monthly wage for two different types of employees
#****************************************************************

#************************ VARIABLES *****************************
position = input("Salesperson or Manager")
commission = 0
salary = 0
total_monthly = 0

#************************ PROCESSING ****************************
if position.upper() == "SALESPERSON":
    gross = int(input("what is your gross sales"))
    commission = gross * 1.08
    salary = 2000.00
    total_monthly = salary + commission
else:
    hours = int(input("How many hours did you work this month: "))
    total_monthly = 40.00 * hours

print(f"The total monthly for {position} is {total_monthly} ")


