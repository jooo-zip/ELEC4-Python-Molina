
# Name: Joseph Molina Jr.
# Section: IV-BSIT B
# Activity: P2 - Custom Module student_utils
# Date: 2026-11-16

# Function to calculate the average grade
def calculate_average(grades):
    total = sum(grades)
    average = total / len(grades)
    return average


# Function to determine if the student passed or failed
def determine_status(grades):
    average = calculate_average(grades)

    if average >= 75:
        return "Passed"
    else:
        return "Failed"


# Function to get the highest grade
def get_highest_grade(grades):
    highest = max(grades)
    return highest


# Function to get the lowest grade
def get_lowest_grade(grades):
    lowest = min(grades)
    return lowest
