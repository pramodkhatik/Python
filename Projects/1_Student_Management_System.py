Students_Details = {}
print("Welcome to SMS(Student Management System)")
while True:
    print("1. Add Student Details")
    print("2. Search Student Details")
    print("3. Remove Student Details")
    print("4. Exit")

    choice = int(input("Enter your choice"))
    if choice == 1:
        stud_count = int(input("How many students details you want to add?"))
        count = 1
        while count <= stud_count:
            roll_no = int(input("Enter roll number:"))
            if roll_no not in Students_Details:
                Students_Details[roll_no] = {}
                Students_Details[roll_no]["Name"] = str(input("Enter name of student:"))
                Students_Details[roll_no]["Marks"] = int(input("Enter marks:"))
                count += 1
            else:
                print("Roll number already exist, please enter unique roll number..!")
        print(Students_Details)
    elif choice == 2:
        roll_no = int(input("Please enter Roll Number of student:"))
        if roll_no in Students_Details:
            print(roll_no, ":", Students_Details[roll_no])
        else:
            print("Roll number", roll_no, "does't exist.")
    elif choice == 3:
        roll_no = int(input("Please enter Roll Number of student:"))
        if roll_no in Students_Details:
            del Students_Details[roll_no]
            print("Details of roll number", roll_no, "removed.")
            print("Current Student directory:", Students_Details)
        else:
            print("Roll number", roll_no, "doesn't exist.")
    elif choice == 4:
        break
    else:
        print("Please enter valid option...")
print("Thank you for using Student Management System...")
