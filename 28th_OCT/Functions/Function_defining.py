def student_details():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    course = input("Enter course: ")
    age = int(input("Enter age: "))

    print("\n----- Student Details -----")
    print("Name:", name)
    print("Roll Number:", roll_no)
    print("Course:", course)
    print("Age:", age)

# Function call
student_details()