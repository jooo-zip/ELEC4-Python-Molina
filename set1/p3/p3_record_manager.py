
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


# Temporary test program
students = []
student_names = set()

add_student(students, student_names)
add_student(students, student_names)

print("\nBefore removing:", students)

remove_student(students, student_names)

print("After removing:", students)

add_student(students, student_names)

print("Final student records:", students)


search_student(students)
search_student(students)

display_students(students)
