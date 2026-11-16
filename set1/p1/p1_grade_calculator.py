
# Name: Joseph Molina Jr.
# Section: IV-BSIT B
# Activity: P1 - Student Grade Calculator
# Date: 2026-11-16



def enter_grades():
    grades = []

    for number in range(1, 4):
        while True:
            try:
                grade = float(input(f"Enter grade {number}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Invalid grade! Enter a number from 0 to 100.")

            except ValueError:
                print("Invalid input! Please enter a number.")

    return grades



def calculate_average(grades):
    total = sum(grades)
    average = total / len(grades)
    return average



def get_highest_grade(grades):
    highest = max(grades)
    return highest


def get_lowest_grade(grades):
    lowest = min(grades)
    return lowest


def determine_status(grades):
    average = calculate_average(grades)

    if average >= 75:
        return "Passed"
    else:
        return "Failed"


# Main program
student_grades = []

print("Programmer: Joseph Molina Jr.")
print("Section: IV-BSIT B")

while True:

    print("\n===== STUDENT GRADE CALCULATOR =====")
    print("1. Enter Student Grades")
    print("2. View Grade Results")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        student_grades = enter_grades()
        print("Grades successfully entered!")

    elif choice == "2":
        if not student_grades:
            print("No grades entered yet. Please choose option 1 first.")

        else:
            average = calculate_average(student_grades)
            highest = get_highest_grade(student_grades)
            lowest = get_lowest_grade(student_grades)
            status = determine_status(student_grades)

            print("\n--- STUDENT GRADE RESULTS ---")
            print("Average:", average)
            print("Highest Grade:", highest)
            print("Lowest Grade:", lowest)
            print("Status:", status)

    elif choice == "3":
        print("Thank you for using the Grade Calculator!")
        break

    else:
        print("Invalid option! Please choose 1, 2, or 3.")



# Local and Global Variables Explanation:
# A local variable is created inside a function and can only be used within that function.
# In my program, total and average inside calculate_average() are local variables.
# A global variable is created outside functions, like student_grades in my main program.
# I pass student_grades to my functions so they can use the grades and return the calculated results.





