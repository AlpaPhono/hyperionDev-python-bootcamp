#=========== Compulsory Task 2 ===============
#
#=============================================

usr_year = int(input("What year do you want to start with?: "))
usr_no_years = int(input("How many years do you want to check?: "))



for year in range(usr_year,(usr_year + usr_no_years)):
    if year % 4 != 0:
        print(f"{year} isn't a leap year")
    else:
        print(f"{year} is a leap year")
