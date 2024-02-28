#===========================================================================
#  *                                 INFO
#
#   Python code
#   Name: Robinson, Berea
#   Course/Section: CMSC 105/6387
#   Type: Discussion
#   Date: 2024-02-09
#
#   Objective: 
#       This program is designed to use while loops to calculate the total 
#       miles traveled for a road trip. It uses a sentinel value to end the 
#       loop and calculates and displays the sum of the user's input.
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
    print(header('Road Trip Tracker'))
    print('Welcome to the Road Trip Mileage Tracker!\n')
    print(textwrap.fill( # Wraps the text to fit the screen
        f"This simple program helps you to track the total miles covered during your road trip."
        f" Please enter the distance covered in miles at each stop. When you're finished, type "
        f"'end' to display the total miles covered."
        ))
    print('')
    print('------------ Enter a location (or "end" to quit) ------------\n'.center(70))

# --------------------------------- CALCULATIONS --------------------------------

def locations_and_miles():
    # Create two empty lists to store the locations and miles
    locations_list = []
    miles_list = []

    # Initialize the total miles and count
    total_miles = 0
    count = 0 # count of locations
    list_num = 0 # list number

    # Sentinel value to end the loop
    sentinal_value = 'end'

    getting_input_for_locations = True # Sets the loop condition
    getting_input_for_miles = True # Sets the loop condition

    # Loop to get the locations
    while getting_input_for_locations:
        list_num += 1 # Increment the list number
        
        try:
            location = input(f'\n{list_num}. Location: \t') # Get the location
            try: # Check if the location is a number
                float(location)
                print(f'/// Error 1 ///'.center(70))
                print(f'Please enter a valid location (not a number).\n'.center(70))
                list_num -= 1 
                continue
            except ValueError: # If the location is not a number
                #print('the value is good, location: ', location)
                pass
        except ValueError:  # print error message
            print(f'/// Error 2 ///'.center(70)) 
            continue # Go back to the start of the loop

        # Check if the location is an empty string
        if location.lower() == '':
            print(f'/// Error 3 ///'.center(70))
            print(f'Please enter a valid location.\n'.center(70))
            list_num -= 1
            continue # Go back to the start of the loop
        
        # Check if the user wants to end the loop as their first input
        if location.lower() == sentinal_value and list_num == 1:
            try:
                print(f'/// Error 4 ///'.center(70))
                print(f'You have not entered a location. Are you sure you want to quit?'.center(70))
                quit = input(f'[y/n]'.center(70))
                if quit.lower() == 'n':
                    continue
                elif quit.lower() == 'y':
                    break
                else:
                    print('')
                    print(f'/// Error 7 ///'.center(70))
                    print(f'Please enter a valid response.\n'.center(70))
                    continue # Go back to the start of the loop
            except:  
                pass # Go back to the start of the loop
        elif location.lower() == sentinal_value:
            break # Exit the loop

        # Add the location to the list
        locations_list.append(location) 
        count += 1 # Increment the count of locations

        # Loop to get the miles for the location
        while getting_input_for_miles:
            try:
                miles = float(input('   Miles: \t'))
                #print('the value is good, miles: ', miles)

            
                if miles <= 0:
                    print(f'/// Error 6 ///'.center(70))
                    print(f'Please enter a valid number of miles.\n'.center(70))

                # Add the miles to the total
                total_miles += miles

                # Add the miles to the list
                miles_list.append(miles)
                break # Exit the loop
            except ValueError:
                print(f'/// Error 5 ///'.center(70))
                print(f'Please enter a valid number of miles.\n'.center(70))
                continue

    # Determine the farthest location and miles
    if miles_list:  # Check if the list is not empty
        farthest_index = miles_list.index(max(miles_list)) # Get the index of the farthest location
        farthest_location = locations_list[farthest_index] # Get the farthest location
        farthest_miles = miles_list[farthest_index] # Get the farthest miles
    else: # If the list is empty
        farthest_location = None 
        farthest_miles = None

    return locations_list, total_miles, count, farthest_location, miles_list, farthest_miles

# --------------------------------- DISPLAY RESULTS --------------------------------

def display_results(L_locations, mileage_total, L_miles, num_locations):
    # Display the results
    print(subheader('Summary'))

    # Check if any locations were entered
    if num_locations == 0: # If no locations were entered
        print('No locations entered.') 
    elif num_locations == 1: # Grammer check
        print(f'You have traveled through {num_locations} location.')
    else: # Grammer check
        print(f'You have traveled through {num_locations} locations.')

    print(f'Total miles traveled:\t {mileage_total}\n')
        
    # Loop through the lists and display the locations and miles the user entered
    for location, miles in zip(L_locations, L_miles): 
        print(f'{location}: {miles} miles')
        
def check_farthest(f_location, f_miles):
    # Check if any locations were entered
    if f_location is None:
        print('No locations entered.')
    else:
        # Display the farthest location
        print(f'\nThe farthest location is {f_location} at {f_miles} miles.')

#===========================================================================
#                                 Main
#===========================================================================

def main():
    # Welcome message showing title and text
    welcome_message()
    
    # Get the locations and miles
    locations_list, total_miles, count, farthest_location, miles_list, farthest_miles = locations_and_miles()

    # Display the results
    display_results(locations_list, total_miles, miles_list, count)

    # Check the farthest location and display the results
    check_farthest(farthest_location, farthest_miles)

#------------------------------- EXECUTE --------------------------------
main()