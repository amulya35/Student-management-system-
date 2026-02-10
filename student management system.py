students = {}

def add_student():
    sid = input("Enter Student ID: ")
    if sid in students:
        print("Student ID already exists!")
        return
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    students[sid] = {
        "name": name,
        "age": age,
        "course": course
    }
    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return
    print("\n--- Student List ---")
    for sid, details in students.items():
        print(f"ID: {sid}, Name: {details['name']}, Age: {details['age']}, Course: {details['course']}")

def search_student():
    sid = input("Enter Student ID to search: ")
    if sid in students:
        s = students[sid]
        print(f"Name: {s['name']}")
        print(f"Age: {s['age']}")
        print(f"Course: {s['course']}")
    else:
        print("Student not found.")

def update_student():
    sid = input("Enter Student ID to update: ")
    if sid in students:
        name = input("Enter new Name: ")
        age = input("Enter new Age: ")
        course = input("Enter new Course: ")

        students[sid] = {
            "name": name,
            "age": age,
            "course": course
        }
        print("Student updated successfully!")
    else:
        print("Student not found.")

def delete_student():
    sid = input("Enter Student ID to delete: ")
    if sid in students:
        del students[sid]
        print("Student deleted successfully!")
    else:
        print("Student not found.")

def menu():
    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

menu() 
