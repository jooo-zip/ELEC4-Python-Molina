
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


student_grades = enter_grades()
result = calculate_average(student_grades)

print("Average:", result)

