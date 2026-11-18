
# Name: Joseph Molina Jr.
# Section: IV-BSIT B
# Activity: P4 - Safe Menu Program
# Date: 2026-11-18


# Function to divide two numbers safely
def divide_numbers():
    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        result = first_number / second_number

    except ValueError:
        print("Invalid input! Please enter numbers only.")

    except ZeroDivisionError:
        print("Error! Cannot divide by zero.")

    else:
        print("Division Result:", result)

    finally:
        print("Division operation finished.")


# Function to open and read a text file safely
def open_text_file():
    file_name = input("Enter file name: ").strip()

    if not file_name:
        print("File name cannot be empty.")
        return

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()

    except FileNotFoundError:
        print("File not found! Please check the file name.")

    except PermissionError:
        print("Permission denied! Cannot read this file.")

    except OSError as error:
        print("Error opening file:", error)

    except UnicodeError:
        print("Error! The file cannot be read as UTF-8 text.")

    else:
        print("\n===== FILE CONTENTS =====")
        print(content if content else "(File is empty.)")

    finally:
        print("File operation finished.")


# Main program
print("Programmer: Joseph Molina Jr.")
print("Section: IV-BSIT B")

while True:
    print("\n===== SAFE MENU PROGRAM =====")
    print("1. Divide Two Numbers")
    print("2. Open a File")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        divide_numbers()

    elif choice == "2":
        open_text_file()

    elif choice == "3":
        print("Thank you for using the Safe Menu Program!")
        break

    else:
        print("Invalid option! Please choose 1, 2, or 3.")
