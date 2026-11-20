
# Name: Joseph Molina Jr.
# Section: IV-BSIT B
# Activity: P3 - Student Record Manager
# Date: 2026-11-16

# Function to add a student
def add_student(students, student_names):
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    if name.lower() in student_names:
        print("Student already exists!")
        return

    students.append(name)
    student_names.add(name.lower())

    print("Student added successfully!")



# Function to remove a student
def remove_student(students, student_names):
    name = input("Enter student name to remove: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    if name.lower() not in student_names:
        print("Student not found!")
        return

    for student in students:
        if student.lower() == name.lower():
            students.remove(student)
            student_names.remove(name.lower())
            print("Student removed successfully!")
            return


# Function to search for students using a partial name
def search_student(students):
    search_name = input("Enter name to search: ").strip().lower()

    if not search_name:
        print("Search cannot be empty.")
        return

    found = False

    for student in students:
        if search_name in student.lower():
            print("Student found:", student)
            found = True

    if not found:
        print("No matching student found.")


# Function to display all students alphabetically
def display_students(students):
    print("\n===== STUDENT RECORDS =====")

    if not students:
        print("No student records found.")
        print("Total Students: 0")
        return

    sorted_students = sorted(students, key=str.lower)

    for number, name in enumerate(sorted_students, start=1):
        print(f"{number}. {name}")

    print("Total Students:", len(students))



# Main program
students = []
student_names = set()

print("Programmer: Joseph Molina Jr.")
print("Section: IV-BSIT B")

while True:
    print("\n===== STUDENT RECORD MANAGER =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_student(students, student_names)

    elif choice == "2":
        remove_student(students, student_names)

    elif choice == "3":
        search_student(students)

    elif choice == "4":
        display_students(students)

    elif choice == "5":
        print("Thank you for using the Student Record Manager!")
        break

    else:
        print("Invalid option! Please choose 1, 2, 3, 4, or 5.")



# List and Set Explanation:
# A list stores multiple values in order and allows duplicate entries.
# In my program, I used the students list to store the original names of the students.
# A set stores unique values, so I used student_names to keep lowercase names and check for duplicates.
# I update both collections when adding or removing students to keep the records consistent.
