#================================= COMPULSORY TASK 3 =============================
# Design a program that determines the award a person competing in triathlon will recieve



#========== user input Times in minutes in three events ==================
#============ Declaring Variables ================
swimming = float(input("Please enter your swimming time in minutes: "))
cycling = float(input("Please enter your Cycling time in minutes: "))
running = float(input("Please enter your runnning time in minutes: "))
qualifying_time = 100

#================== Calculating total times based on user input ===========================
total_time = swimming + cycling + running
print(f"Total time to complete the triathlon is: {total_time} minutes ") # printing the the total time.

#====== Determining Award in relation to qualifying time ===================

if total_time <= 100:
    print("Provincial Colours")
elif total_time > 100 and total_time <= 105:
    print("Provincial Half Colours")
elif total_time > 105 and total_time <= 110:
    print("Provincial Scroll")
elif total_time > 110:
    print("No award")
