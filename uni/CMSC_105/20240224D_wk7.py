#===========================================================================
#  *                                 INFO
#
#   Python code
#   Name: Robinson, Berea
#   Course/Section: CMSC 105/6387
#   Date: 2024-02-24
#
#   Objective: 
#       This program popuates an array variable (with 5 elements) within a 
#       for loop. The program will then modify each element of the array by
#       using a second loop. The program will then display the modified array
#       in a third loop.
#           - One array
#           - Three loops
#
#===========================================================================

import datetime 
import textwrap

#------------------------------- WELCOME INFO ------------------------------

# Welcome Information
def header(title: str):
    # Get the current date
    today = datetime.date.today()
    name = 'Berea Robinson'

    # Formating variables
    width = 70
    hr_sep = '=' * width

    # Return the formatted message
    return(
        f'\nDate: \t{today}\n'    # Display the current date
        f'Name: \t{name}\n'
        f'{hr_sep}\n'   # Display a line of '='
    )

def subheader(title: str):
    # Formating variables
    width = 70
    hr_sep = '-' * width

    # Return the formatted message
    return(
        f'\n{hr_sep}\n'   # Display a line of '-'
        f'{title.upper(): ^70}\n'   # Center the title
        f'{hr_sep}\n'  # Display a line of '-'
    )

def welcome_message():
    # Welcome message showing title and text
    print(header(''))
    print(textwrap.fill( # Wraps the text to fit the screen
        f'Please input the student names when prompted. The program will then '
        f'modify the names to be in all uppercase letters, and display the '
        f'modified names.'
        ))
    print('')
    print('------------ INPUT ------------\n'.center(70))

# ----------------------------- CALCULATIONS --------------------------------

def students():
    # Initialize the array
    students_list = []
    for i in range(5):
        students_list.append(input(f'Enter student {i+1}: '))
    return students_list

def modify_students(students1: list):
    # Modify the array
    for i in range(len(students1)):
        students1[i] = students1[i].upper()
    return students1

# ---------------------------- DISPLAY RESULTS ------------------------------

def display_students(students2: list):
    # Display the modified array
    print('\nThe modified student names are: ')
    for name in students2:
        print(name)

#===========================================================================
#                                 Main
#===========================================================================

def main():
    # Welcome message showing title and text
    welcome_message()

    # Initialize the array
    list = students()

    # Modify the array
    modified_names = modify_students(list)

    # Display the modified array
    display_students(modified_names)

#-------------------------------- EXECUTE ---------------------------------
main()