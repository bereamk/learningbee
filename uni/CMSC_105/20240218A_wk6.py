#===========================================================================
#  *                                 INFO
#
#   Python code
#   Name: Robinson, Berea
#   Course/Section: CMSC 105/6387
#   Date: 
#
#   Objective: 
#       This program determines whether or not the user inputed password is
#       valid/secure. The password must meet the following requirements:
#           - At least 6 minimum and 15 maximum characters
#           - It must not include any spaces
#           - It must contain at least one digit (integers 0-9)
#           - It must contain at least one alphabetic character (a-z, A-Z)
#       The program must contain three functions:
#           - A function that checks the length of the password
#           - A function that cheks the required number of characters/digits
#           - A function that verifies it does not contain space(s)
#
#===========================================================================

import datetime 

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
    print(header('SECURE PASSWORD CHECKER'))
    print(f'Welcome to the secure password checker.\n'
          f'This program will check the strength of your password.\n')
    print(f"It must meet the following requirements:\n"
        f"    - At least 6 minimum and 15 maximum characters\n"
        f"    - It must not include any spaces\n"
        f"    - It must contain at least one digit (integers 0-9)\n"
        f"    - It must contain at least one alphabetic character (a-z, A-Z)"
        )
    print('')
    print('-----------------------------------------------'.center(70))

# ----------------------------- CALCULATIONS --------------------------------

# Get the password from the user
def get_password():
    while True:
        password = input('\nPlease enter a password: \t')
        print('')
        if check_length(password): # Check the length of the password
            continue # If the length is not valid, continue the loop
        elif check_spaces(password): # Check for spaces in the password
            continue # If spaces are found, continue the loop
        else: # If the password meets the length and space requirements
            input_digit, input_alpha = check_characters(password) # Check for digits and alphabetic characters
            if not input_digit or not input_alpha: # If the password does not contain a digit or alphabetic character
                continue # Continue the loop
            else: # If the password meets all the requirements
                break # Break the loop
    return password

# Check the length of the password
def check_length(password1):
    if 6 <= len(password1) <= 15: # If the length of the password is between 6 and 15 characters
        return False
    else: # If the length of the password is not between 6 and 15 characters
        print('/// ERROR 1 ///'.center(70)) # Display the error message
        print('Password must be between 6 and 15 characters.'.center(70))
        return True
    
# Check for spaces in the password
def check_spaces(password2):
    if ' ' in password2: # If a space is found in the password
        print('/// ERROR 2 ///'.center(70)) # Display the error message
        print('Password must not contain any spaces.'.center(70))
        return True

# Check for digits and alphabetic characters
def check_characters(password3): 
    # Initialize the variables
    digit = False 
    alpha = False

    for char in password3: # Loop through each character in the password
        if char.isdigit(): # If the character is a digit
            digit = True
        if char.isalpha(): # If the character is an alphabetic character
            alpha = True

    if not digit: # If the password does not contain a digit
        print('/// ERROR 3 ///'.center(70)) # Display the error message
        print('Password must contain at least one digit.'.center(70))
    if not alpha: # If the password does not contain an alphabetic character
        print('/// ERROR 4 ///'.center(70)) # Display the error message
        print('Password must contain at least one alphabetic character.'.center(70))

    return digit, alpha # Return the digit and alpha variables

#===========================================================================
#                                 Main
#===========================================================================

def main():
    # Welcome message showing title and text
    welcome_message()

    # Get the password from the user
    input_password = get_password()

    # Display the result
    print(subheader('Password is Valid'))

#-------------------------------- EXECUTE ---------------------------------
main()