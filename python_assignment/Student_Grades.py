student_grades ={"Sourav": 95, "Rohit": 88, "Priya": 65, "Anjali": 55, "Biswajit": 75}

user_needs_new = input("Do you want to add a new student grade? (yes/no): ")

if user_needs_new.lower() == "yes":
    student_name = input("Enter the new student's name: ")
    if student_name not in student_grades:
        try:
            new_grade = int(input("Enter the new student's grade: "))
            student_grades[student_name] = new_grade
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Student already exists.")

user_needs_edit = input("Do you want to edit an existing student's grade? (yes/no): ")
if user_needs_edit.lower() == "yes":
    student_name = input("Enter the existing student's name: ")
    if student_name in student_grades:
        try:
            grade_update = int(input("Enter the existing student's updated grade: "))
            student_grades[student_name] = grade_update
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Student does not exist.")

print("Student Grades: ", student_grades)


