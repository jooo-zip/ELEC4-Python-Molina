
# Name: Joseph Molina Jr.
# Section: IV-BSIT B
# Activity: P2 - Custom Module student_utils
# Date: 2026-11-16

# Import our custom module
import student_utils

# Import a specific function from our custom module
from student_utils import determine_status

# Import datetime to show when the report was generated
import datetime


print("===== STUDENT GRADE REPORT =====")
print("Programmer: Joseph Molina Jr.")
print("Section: IV-BSIT B")

# Create an empty list for the grades
grades = []

# Ask the user to enter three grades
for number in range(1, 4):
    grade = float(input(f"Enter grade {number}: "))
    grades.append(grade)


# Use functions from student_utils.py
average = student_utils.calculate_average(grades)
highest = student_utils.get_highest_grade(grades)
lowest = student_utils.get_lowest_grade(grades)

# Demonstrate the second import style
status = determine_status(grades)

# Get the current date and time
report_date = datetime.datetime.now().strftime("%Y-%m-%d %I:%M %p")


# Display the grade report
print("\n===== GRADE REPORT RESULTS =====")
print("Average:", average)
print("Highest Grade:", highest)
print("Lowest Grade:", lowest)
print("Status:", status)
print("Report Generated:", report_date)
