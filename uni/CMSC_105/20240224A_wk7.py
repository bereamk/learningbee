#===========================================================================
#  *                                 INFO
#
#   Python code
#   Name: Robinson, Berea
#   Course/Section: CMSC 105/6387
#   Date: 2024-02-24
#
#   Objective: 
#       This program collects all the data of a road trop and calculates each
#       person's share of the cost. Currency is in USD.
#       Prompts the following:
#           - The number of people on the trip
#           - The number of days on the trip
#           - For each day of the trip:
#               - Cost of food
#               - Cost of gas
#        Calculates and displays each of the following:
#           - The total cost of each category
#           - The total cost of the trip
#           - The cost per person
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
    print(header('USA Road Trip Cost Calculator'))
    print('Welcome to the USA Road Trip Cost Calculator!\n')
    print(
        f'When prompted, please enter:\n'
        f'\t- The number of people on the trip\n'
        f'\t- The number of days on the trip\n'
        f'\t- The cost of food and gas for each day\n'
    )
    print(textwrap.fill(
        f'The program will then calculate the total cost of each category, the '
        f'total cost of the trip, and the cost per person.\n'
    ))
    print(f'\nAll currency is in USD ($)')
    print('')
    print('------------ Input ------------\n'.center(70))

# ----------------------------- CALCULATIONS --------------------------------
    
def get_trip_info():
    # Get the number of people and days on the trip
    num_people = int(input('Number of people on the trip: \t'))
    num_days = int(input('Number of days on  the  trip: \t'))

    # Initialize the arrays
    food_cost = []
    gas_cost = []
    
    print('')
    print('------------ Costs ------------'.center(70))
    print()

    for i in range(num_days):
        # Get the cost of food for each day
        food_cost.append(float(input(f'Food for day {i+1}: \t$')))
        # Get the cost of gas for each day
        gas_cost.append(float(input(f'Gas for  day {i+1}: \t$')))
        print('')

    return num_people, num_days, food_cost, gas_cost
                            
def calculate_cost(people, food, gas):
    # Calculate the total cost of each category
    total_food_cost = sum(food)
    total_gas_cost = sum(gas)
    # Calculate the total cost of the trip
    total_cost = total_food_cost + total_gas_cost
    # Calculate the cost per person
    cost_per_person = total_cost / people

    return cost_per_person, total_cost, total_food_cost, total_gas_cost

# ---------------------------- DISPLAY RESULTS ------------------------------

def display_results(per_person, total, f_cost, g_cost, num_days):
    # Display the results
    print(subheader('Results'))
    print(f'The total length of the trip was {num_days} days\n')
    print(f'\tTotal Costs\n'.upper())
    print(f' Food: \t\t${f_cost:.2f}')
    print(f' Gas: \t\t${g_cost:.2f}\n')
    print(f' Trip: \t\t${total:.2f}')
    print(f' Per Person: \t${per_person:.2f}')

#===========================================================================
#                                 Main
#===========================================================================

def main():
    # Welcome message showing title and text
    welcome_message()

    # Get trip info
    num_people, num_days, food_cost, gas_cost = get_trip_info()

    # Calculate the cost
    per_person, total, f_cost, g_cost = calculate_cost(num_people, food_cost, gas_cost)

    # Display the results
    display_results(per_person, total, f_cost, g_cost, num_days)

#-------------------------------- EXECUTE ---------------------------------
main()