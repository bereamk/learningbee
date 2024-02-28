#===========================================================================
#  *                                 INFO
#
#   Python code
#   Name: Robinson, Berea
#   Course/Section: CMSC 105/6387
#   Date: 2024-02-18
#
#   Objective: 
#       The program determines whether a string is in the correct format for
#       a university email address. The correct format is: namehere@X.edu
#       The program will prompt the user to enter an email address, and output
#       whether the email address is valid, and if not, why it's not valid.
#       To be valid, the email must:
#       - Contain the @ symbol only once
#       - The length of the username before the @ symbol must be greater than 
#         four characters.
#       - It must end with the substring '.edu'
#       - There must be at least one letter between the @ and the .edu
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
    print(header('SCHOOL EMAIL VALIDATOR'))
    print('This program will tell you whether or not your email is a valid school email.\n')
    print(textwrap.fill( # Wraps the text to fit the screen
        f"Please enter your email address when prompted."
        ))
    print('')
    print('---------------------------------------------'.center(70))

# ----------------------------- CALCULATIONS --------------------------------

def get_email():
    # Example email: XXXX@X.edu
    substring = '.edu'
    getting_email = True

    while getting_email: # Loop until a valid email is entered
        email = input('\nPlease enter an email address: ') 
        if email == '' or ' ' in email:
            print(f'/// ERROR 1 ///'.center(70))
            print(f'You must enter an email address.'.center(70))
            continue
        elif '@' not in email:
            print(f'/// ERROR 2 ///'.center(70))
            print(f'Your email must contain the "@" symbol.'.center(70))
            continue
        elif email.count('@') > 1:
            print(f'/// ERROR 3 ///'.center(70))
            print(f'Your email must contain only one "@" symbol.'.center(70))
            continue
        elif email.find('@') < 4:
            print(f'/// ERROR 4 ///'.center(70))
            print(f'Your email must contain at least 4 characters before the "@" symbol.'.center(70))
            continue
        elif email[-4:] != substring:
            print('/// ERROR 5 ///'.center(70))
            print('Your email must end with ".edu".')
            continue
        elif email.find('@') + 1 == email.find('.edu'):
            print('/// ERROR 6 ///'.center(70))
            print('There must be at least one letter between the "@" and ".edu".')
            continue
        else:
            getting_email = False
            break
    return email

#===========================================================================
#                                 Main
#===========================================================================

def main():
    # Welcome message showing title and text
    welcome_message()
    user_email = get_email()
    print(f'\nYour email is: \t{user_email}')
    print(f'Congrats, your email is valid! :)')

#-------------------------------- EXECUTE ---------------------------------
main()