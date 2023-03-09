#*************** Compulsory Task 1 **************
#
#************************************************

#.---------------- Variables --------------------
# student_id is initalised to none as it will be used later
#
#.------------------------------------------------
no_students = int(input("How man students are registering: "))
student_id = None
request_id = "What is your id number: "

#.---------------- Process -----------------------
# With block to open/create a file.
# Nested For loop to write student id into the file
#.------------------------------------------------
with open("reeg_form.txt","a+") as f:
    for student in range(no_students):
        student_id = int(input(request_id))
        f.write(str(student_id)+"\n")

