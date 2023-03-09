#==================== COMPULSORY TASK 2 =================
# Calculate BMI

# =============== VARIABLES ======================
weight = float(input("Please enter your weight in kg: "))
height = float(input("please enter your height in m: "))
bmi = weight / (height**2)

#=================== PROCESSING ===================
if bmi >= 30:
    print(bmi)
    print("obese")
elif bmi >= 25:
    print(bmi)
    print("Overweight")
elif bmi >= 18.5:
    print("normal")
elif bmi < 18.5:
    print("underweight")