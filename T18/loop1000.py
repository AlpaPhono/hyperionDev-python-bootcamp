#.************************* Compulsory Task 2 *********************
#. Write 2 lines of code in your file to print out all numbers from
#. 1 to 1000
#.*****************************************************************
print("Step1:")

for i in range(1001):
    print(i)

#.-------------------- Step 2 ------------------
#. add logic to the loop to only print out
#. the numbers from 1 to 1000 that are 
#. divisible by 2
#.----------------------------------------------
print("step2: ")
for i in range(1001):
    if i % 2 == 0:
        print(i)
