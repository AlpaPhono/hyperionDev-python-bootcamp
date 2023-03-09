#================== Compulsory Task 1 ===================
#
#=========== Declairing Variables =======================
num1 = 5
num2 = 2
num3 = 24

#==================== Processing =========================
# Comparing num1 with num2
print("Displaying the larger value")
if num1 >= num2:
    print(num1)
elif num2 >= num1:
    print(num2)
print("")

# Determining if num1 is even
if num1 % 2 == 0:
    print(f"num1 is even")
else:
    print("num1 is odd")

# Sort numbers from largest to the smallest
print("") # to give space to console output
print("listing in decending order: ")
if num1 > num2 and num2 > num3:
    print(num1, num2, num3)
elif num1 > num3 and num3 > num2:
    print(num1,num3,num2)
elif num2 > num1 and num1 > num3:
    print(num2,num1,num3)
elif num2 > num3 and num3 > num1:
    print(num2,num3,num1)
elif num3 > num1 and num1 > num2:
    print(num3,num1,num2)
elif num3 > num1 and num1 > num2:
    print(num3, num1, num2)