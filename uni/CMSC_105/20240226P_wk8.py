#===========================================================================
#  *                                 INFO
#
#   Python code
#   Name: Robinson, Berea
#   Course/Section: CMSC 105/6387
#   Date: 2024-02-28
#
#   Objective: 
#       This program determines the densities of a collection of cylindrical 
#       containers. User supplies the height, diameter, and weight of each
#       container. The program calculates the density of each container and
#       categorizes the containers into low, average, and high density.
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

def welcome_message():
    # Welcome message showing title and text
    print(header('DENSITY OF CYLINDRICAL CONTAINERS CALCULATOR'))
    print(textwrap.fill( # Wraps the text to fit the screen
        f'Welcome to the Density of Cylindrical Containers Calculator. This '
        f'program will determine the densities of a collection of cylindrical '
        f'containers. You will be prompted to supply the height, diameter, and '
        f'weight of each container. The program will calculate the density of '
        f'each container and categorize the containers into low, average, and '
        f'high density.'
        ))
    # Explain the results
    print('\nDensity Categories: ')
    print('  - Low: less than 0.5 lbs/ft^3')
    print('  - Average: between 0.5 and 1.5 lbs/ft^3')
    print('  - High: greater than 1.5 lbs/ft^3')
    print('')
    print('------------ USER INPUT ------------'.center(70))

# ----------------------------- CALCULATIONS --------------------------------
    
# Function to calculate the density of the containers
def get_height_diameter(containers: list):
    density_list = []   
    # Prompt user for the height and diameter of the containers in feet and pounds
    for i in range(len(containers)):
        print(f'\nContainer {i+1}: {containers[i]}')
        height = float(input(f'  - Height (ft): '))
        diameter = float(input(f'  - Diameter (ft): '))
        weight = float(input(f'  - Weight (lbs): '))

        # Call the function to calculate the density
        density = calculate_density(height, diameter, weight)
        density_list.append(f'{density:.3}') # Append the density to the list
        print(f'  - Density: {density:.2f} cubic feet (lbs/ft^3)')
        print('')
    print('The densities of the containers are: ')
    print(density_list)

    # Reverse the array of densities
    reversed_list = []
    for each_density in reversed(density_list):
        reversed_list.append(each_density)
    return reversed_list

def calculate_density(container_height, container_diameter, container_weight):
    # Calculate the volume of the container
    volume = container_diameter * 3.1415 * container_height

    # Calculate the density of the container
    container_density = container_weight / volume
    return container_density

def density_category(density_list_reversed: list):
    # Declare variables
    low_density = 0
    average_density = 0
    high_density = 0

    # Loop through the array and determine the category of the density
    for listed in range(len(density_list_reversed)):
        if float(density_list_reversed[listed]) < 0.5:
            low_density += 1
        elif float(density_list_reversed[listed]) >= 0.5 and float(density_list_reversed[listed]) <= 1.5:
            average_density += 1
        else:
            high_density += 1
    return low_density, average_density, high_density

# ---------------------------- DISPLAY RESULTS ------------------------------

def display_counts(low: int, average: int, high: int):
    # Display the number of containers in each category
    print('\nNumber of containers with: ')
    print(f'  - Low density: \t{low}')
    print(f'  - Average density: \t{average}')
    print(f'  - High density: \t{high}')

#===========================================================================
#                                 Main
#===========================================================================

def main():
    # Welcome message showing title and text
    welcome_message()

    # Declare variables      
    content_list = ['Water', 'Oil', 'Milk', 'Honey', 'Syrup']

    # Prompt user for the height and diameter of the containers in feet and pounds
    reversed_density_list = get_height_diameter(content_list)

    # Determine the category of the density
    low, average, high = density_category(reversed_density_list)

    # Display the number of containers in each category
    display_counts(low, average, high)

#-------------------------------- EXECUTE ---------------------------------
main()