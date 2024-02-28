#===========================================================================
#  *                                 INFO
#
#   Python code
#   Name: Robinson, Berea
#   Course/Section: CMSC 105/6387
#   Type: Assignment
#   Date: 2024-02-10
#
#   Objective: 
#       This program computes the weighted average of a student's grades and
#       determines which student has the highest average.
#
#? Note: This program is a second verion of the first program. The first program
#?       failed to meet certain requirements. This itteration is a second attempt.
#
#===========================================================================

import datetime 
import textwrap

#------------------------------- WELCOME INFO ------------------------------

# Welcome Information
def header(title: str):
    # Get the current date
    today = datetime.date.today()

    # Formating variables
    width = 70
    hr_sep = '=' * width

    # Return the formatted message
    return(
        f'\nDate: \t{today}\n'    # Display the current date
        f'{hr_sep}\n'   # Display a line of '='
        f'{title.upper(): ^70}\n'   # Center the title
        f'{hr_sep}\n'  # Display a line of '='
    )

def subheader(title: str, text: str):
    # Formating variables
    width = 70
    hr_sep = '-' * width

    # Return the formatted message
    return(
        f'\n{hr_sep}\n'   # Display a line of '-'
        f'{title.upper(): ^70}\n'   # Center the title
        f'{text.center(70)}\n' # Center the text
        f'{hr_sep}\n'  # Display a line of '-'
    )

def welcome_message():
    # Welcome message showing title and text
    print(header('Grade Calculator'))
    print('Welcome to the Grade Calculator!\n')
    print(textwrap.fill( # Wraps the text to fit the screen
        f"This simple program helps you to calculate the weighted average of a"
        f" student's grades. Please enter the student's grades ranging from [0 - 100]"
        f" for the Discussion, Quiz, and Programming Assignment. The program will"
        f" then calculate the weighted average grade and determine which student has the highest average."
        ))
    print('')
    print('------------ Enter Grades ------------\n'.center(70))

# --------------------------------- CALCULATIONS --------------------------------

def get_student_grades(student):
    letter_grade = ''
    # Prompt the user for the student's Discussion grade
    discussion_grade = input(f'\nDiscussion: \t')
    
    while discussion_grade == '' or ' ' in discussion_grade or not discussion_grade.isdigit() or int(discussion_grade) < 0 or int(discussion_grade) > 100:
        print('/// Error 1 ///'.center(70))
        print('Invalid input. Please enter a valid grade.'.center(70))
        print('[0 - 100]'.center(70))
        discussion_grade = input(f'Discussion: \t')

    # Prompts the user for the student's Quiz grade
    quiz_grade = input(f'Quiz: \t\t')

    while quiz_grade == '' or ' ' in quiz_grade or not quiz_grade.isdigit() or int(quiz_grade) < 0 or int(quiz_grade) > 100:
        print('/// Error 2 ///'.center(70))
        print('Invalid input. Please enter a valid grade.'.center(70))
        print('[0 - 100]'.center(70))
        quiz_grade = input(f'Quiz: \t')

    # Prompts the user for the student's Programming Assignment grade
    assignment_grade = input(f'Assignment: \t')

    while assignment_grade == '' or ' ' in assignment_grade or not assignment_grade.isdigit() or int(assignment_grade) < 0 or int(assignment_grade) > 100:
        print('/// Error 3 ///'.center(70))
        print('Invalid input. Please enter a valid grade.'.center(70))
        print('[0 - 100]'.center(70))
        assignment_grade = input(f'Assignment: \t')

    # Calculate the weighted average grade
    # Discussion grate weight is 0.15, Quiz grade weight is 0.35, and Assignment grade weight is 0.5
    wtAvgGrade = float(discussion_grade) * 0.15 + float(quiz_grade) * 0.35 + float(assignment_grade) * 0.5

    letter_grade = get_letter_grade(wtAvgGrade)

    # Return the weighted average grade
    return wtAvgGrade, letter_grade

def get_letter_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'

#===========================================================================
#                                 Main
#===========================================================================

def main():
    # Welcome message showing title and text
    welcome_message()

    # List of four students
    students = ['Alexander', 'Brianna', 'Chris', 'Dannie']
    student_averages = []
    student_grades = []

    # Call the function to loop through the students and get their grades and calculate the weighted average
    for student in students:
        print(f'{student}\'s Grades')

        # Get the weighted average grade for each student
        wtAvgGrade, letter_grade = get_student_grades(student)

        # Display the weighted average grade
        print(f'\nThe weighted average grade for {student} is {wtAvgGrade:.2f} or {letter_grade}')

        # Append the weighted average grade to the list
        student_averages.append(wtAvgGrade)
        student_grades.append(letter_grade)

        current_highest = max(student_averages)
        highest_student = students[student_averages.index(current_highest)]
        h_grade = student_grades[student_averages.index(current_highest)]

        # Check if the student has the highest grade
        if wtAvgGrade == current_highest:
            highest = f'Highest: {highest_student} | Grade: {current_highest:.2f} | Letter Grade: {h_grade}'
            print(subheader(f'Current Highest Grade?: YES ({current_highest:.2f})', highest))
        else:
            print(subheader(f'Current Highest Grade?: NO', highest))

   # The student with the highest grade
    highest_grade = max(student_averages)
    highest_student = students[student_averages.index(highest_grade)]
    hh_grade = student_grades[student_averages.index(highest_grade)]
    print(f'The student with the highest grade is {highest_student} with a grade of {highest_grade:.2f} ({hh_grade})') 

#-------------------------------- EXECUTE ---------------------------------
main()