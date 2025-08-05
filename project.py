students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    student_class = input("Enter Class: ")
    
    # Check for duplicate roll number
    for student in students:
        if student['roll'] == roll:
            print("Student with this roll number already exists!")
            return

    student = {
        'roll': roll,
        'name': name,
        'age': age,
        'class': student_class
    }
    students.append(student)
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No student records found.\n")
        return
    print("\nList of Students:")
    for student in students:
        print(f"Roll: {student['roll']}, Name: {student['name']}, Age: {student['age']}, Class: {student['class']}")
    print()

def search_student():
    roll = input("Enter Roll Number to Search: ")
    for student in students:
        if student['roll'] == roll:
            print(f"Found: Roll: {student['roll']}, Name: {student['name']}, Age: {student['age']}, Class: {student['class']}\n")
            return
    print("Student not found!\n")

def update_student():
    roll = input("Enter Roll Number to Update: ")
    for student in students:
        if student['roll'] == roll:
            student['name'] = input("Enter New Name: ")
            student['age'] = input("Enter New Age: ")
            student['class'] = input("Enter New Class: ")
            print("Student updated successfully!\n")
            return
    print("Student not found!\n")

def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    for student in students:
        if student['roll'] == roll:
            students.remove(student)
            print("Student deleted successfully!\n")
            return
    print("Student not found!\n")

def menu():
    while True:
        print("==== Student Management System ====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

# Run the menu
menu()
