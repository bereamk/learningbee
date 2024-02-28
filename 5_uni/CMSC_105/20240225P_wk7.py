#===========================================================================
#  *                                 INFO
#
#   Python code
#   Name: Robinson, Berea
#   Course/Section: CMSC 105/6387
#   Date: 2024-02-25
#
#   Objective: 
#       This program collects the height of 5 people. Loop through the array
#       and ask for the height in feet and inches, convert the height into inches
#       and store in an array. Next each height in the array should be converted
#       to meters and stored in a second array. Display both arrays. 
#           - Challenge: display in column format using a loop
#       The number of short, average, and tall people should be counted and
#       the number of each group should be displayed. 
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
    hr_sep = '=' * 70

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
    print(header('TITLE'))
    print('TEXTEXT\n')
    print(textwrap.fill( # Wraps the text to fit the screen
        f"BIG TEXT"
        ))
    print('')
    print('------------ INSTRUCTION ------------\n'.center(70))
# ----------------------------- CALCULATIONS --------------------------------
def get_height_inches():
    # Create an empty list to store the heights
    heights = []

    # Loop through the array and ask for the height in feet and inches
    for i in range(5):
        print(f'\nPerson {i+1}')
        feet = int(input(f'  - Feet: ')) # Get the height in feet
        inches = int(input(f'  - Inches: '))
        height = feet * 12 + inches
        heights.append(height)
    return heights

def convert_to_meters(height_in_inches: list):
    # Create an empty list to store the heights in meters
    meters = []

    for height in height_in_inches:
        meters.append(height * 0.0254)
    return meters

def count_people(height_in_inches: list):
    # Initialize the counters
    num_short = 0
    num_average = 0
    num_tall = 0

    # Count the number of short, average, and tall people
    for height in height_in_inches:
        if height <= 60:
            num_short += 1
        elif height <= 72:
            num_average += 1
        else: 
            num_tall += 1
    return num_short, num_average, num_tall
# ---------------------------- DISPLAY RESULTS ------------------------------
def display_in_columns(total_inches: list, total_meters: list):
    print('-'*70)
    print('\nHeight in Inches\tHeight in Meters')
    for i in range(5):
        print(f'{total_inches[i]:.2f}\t\t\t{total_meters[i]:.2f}')
    print('-'*70)

def display_counts(short: int, average: int, tall: int):
    print(f'Number of short people: {short}')
    print(f'Number of average people: {average}')
    print(f'Number of tall people: {tall}')
#===========================================================================
#                                 Main
#===========================================================================
def main():
    # Welcome message showing title and text
    welcome_message()

    # Get the height in inches
    heights = get_height_inches()

    # Convert the height into inches and store in an array
    meters = convert_to_meters(heights)

    # Display both arrays
    display_in_columns(heights, meters)

    # Count the number of short, average, and tall people
    short, average, tall = count_people(heights)

    # Display the number of each group
    display_counts(short, average, tall)
#-------------------------------- EXECUTE ---------------------------------
main()