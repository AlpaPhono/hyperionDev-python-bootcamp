# *************************** OPTIONAL TASK 2 ************************************
# help decide what to wear based on temperature and period of the week.
# ********************************************************************************

#================== VARIABLES ======================
greater_than_20 = True
weekend = True
sunny = True
temp = input("is the temperature greater than 20: ")
week = input("is it the weekend: ")
sun = input("is it sunny outside: ")
positive = "YES"
negative = "NO"
shirt = None
bottoms = None
Top = None

#=================== PROCESSING ========================
if temp.upper() == positive:
    greater_than_20 = True
    shirt = "Short-sleeved shirt"
else:
    greater_than_20 = False
    shirt = "Long-sleeved shirt"

if week.upper() == positive:
    weekend = True
    bottoms = "Shorts"
else:
    weekend = False
    bottoms = "Jeans"

if sun.upper() == positive:
    sunny = True
    top = "Cap"
else:
    sunny = False
    top = "RainCoat"

print(f"You should wear a {shirt} with {bottoms} and a {top} Today. ")