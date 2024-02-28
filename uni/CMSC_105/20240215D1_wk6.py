#===========================================================================
#  *                                 INFO
#
#   Python code
#   Name: Robinson, Berea
#   Course/Section: CMSC 105/6387
#   Date: 2024-02-14
#
#   Objective: 
#       Program accepts a string as input. It then analyzes some of the
#       characters in the string and displays the results.
#           - The number of characters in the string
#           - The number of words in the string
#           - The number of vowels in the string
#           - Slice the string to display the first and last words
#           - Converts string to lowercase
#           - Determines if my initials are in the string (in any case combination). 
#               - Initials are 'BR'
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
    print(header('Sentence Analyzer'))
    print('Welcome to the string (or sentence) analyzer!\n')
    print(textwrap.fill( # Wraps the text to fit the screen
        f"This program will analyze a string that you enter. It will display "
        f"the number of characters, words, and vowels in the string. It will "
        f"also display the string in lowercase, the first and last words in the "
        f"string, and determine if my initials are in the string. My initials are 'BR'.",
        ))
    print('')

# ----------------------------- CALCULATIONS --------------------------------

# Get the string to analyze
def get_string(): 
    print('Enter String:')
    ans = input('\t\t')
    return ans

# Analyze the string
def count_characters(string):
    # Count the number of characters in the string
    count = len(string)
    return count

def count_words(string):
    # Count the number of words in the string
    words = string.split()
    count = len(words)
    return count

def count_vowels(string):
    # Count the number of vowels in the string
    vowels = 'aeiou'
    count = 0
    for char in string: # Loop through each character in the string
        if char in vowels:
            count += 1 # If the character is a vowel, add 1 to the count
    return count

def convert_to_lowercase(string):
    # Convert the string to lowercase
    lower = string.lower()
    return lower

def split_string(string):
    # Slice the string to display the first and last words
    words = string.split() # Split the string into a list of words
    first = words[0] # Get the first word
    last = words[-1] # Get the last word
    ends = (first, last)
    return ends

def determine_initials(string):
    # Determine if my initials are in the string
    initials = 'BR'
    if initials.lower() in string.lower(): # Check if the initials are in the string
        present = True # If the initials are in the string, return True
    elif initials.lower() not in string.lower():
        present = False
    return present


    

# ---------------------------- DISPLAY RESULTS ------------------------------



#===========================================================================
#                                 Main
#===========================================================================

def main():
    default_string = True # This variable will be used to control the if loop
    question = True # This variable will be used to control the while loop

    # Welcome message showing title and text
    welcome_message()

    while question:
        favorite = input('What is your favorite letter? ').lower()
        if favorite.isalpha() and len(favorite) == 1:
            break
        else:
            print('')
            print('/// Error 1 ///'.center(70))
            print('Invalid input. Please enter a single letter.\n'.center(70))
            continue
    question = False


    displayed_text = get_string()
    if default_string:
        text = f'The string you entered is: \n'.center(70)
        print('')
        print(f'--------------------------------------------------\n'.center(70))
        print(text.upper())
        print(f'{displayed_text}'.center(70)) # Center the text
        print('')
        print(f'--------------------------------------------------\n'.center(70))

    char_num = count_characters(displayed_text)
    word_num = count_words(displayed_text)
    vowel_num = count_vowels(displayed_text)
    lower_text = convert_to_lowercase(displayed_text)
    end_pieces = split_string(displayed_text)
    initials = determine_initials(displayed_text)
    
    print(f'1. The number of characters in the string is: \t{char_num}')
    print(f'2. The number of words in the string is: \t{word_num}')
    print(f'3. The number of vowels in the string is: \t{vowel_num}')
    print(f'4. The string in lowercase is:')
    print(f'{lower_text}'.center(70))
    print(f'5. The first and last word in the string is: {end_pieces}')
    print(f'6. Are my initials [BR] in the string?: {initials}')
    print(f"7. The letter '{favorite}' appears {displayed_text.count(favorite)} time(s) in the string.")
    


#-------------------------------- EXECUTE ---------------------------------
main()