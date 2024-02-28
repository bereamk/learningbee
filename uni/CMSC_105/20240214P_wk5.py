#===========================================================================
#  *                                 INFO
#
#   Python code
#   Name: Robinson, Berea
#   Course/Section: CMSC 105/6387
#   Type: Practice
#   Date: 2024-02-14
#
#   Objective: 
#       For each person, calculate the sum of the total lbs lost. Print at the end
#       who lost the most and the total paid.
#         - Per lb lost = 1.50
#         - 8 weeks
#         - 5 people
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

def welcome_message(people, price_per_lb):
    # Welcome message showing title and text
    print(header('Weight Loss Challenge'))
    print('Welcome to the weight loss challenge!\n')
    print(textwrap.fill( # Wraps the text to fit the screen
        f"Contestants are: {people}. Enter the amount of weight lost for each week for each individual. "
        f"The contestant with the most weight loss will win ${price_per_lb} per lb lost. "
        ))
    print(f'\nIf the person gained weight, enter the amount as a negative number.\n\n')
    print('------------ For each Week, enter the lbs lost ------------'.center(70))

# ----------------------------- CALCULATIONS --------------------------------

def get_weight_lost(people):
  weight_lost = [] # Create an empty list to store the total weight lost for each person
  getting_input = True # This variable will be used to control the while loop

  while getting_input:
    lbslost = 0 # This variable will store the amount of weight lost for each week
    
    # Loop through each person in the list
    for name in people:
        totalLBs = 0 # This variable will store the total amount of weight lost for each person

        print(f'\n\n>> {name.upper()} <<\n')

        valid_input = True # This variable will be used to control the while loop

        # Loop through each week
        for week in range(1, 9):
          while valid_input:  # This loop will keep running until a valid input is entered
            try: 
              lbslost = input(f"\tWeek {week}:\t") # Prompt the user for the amount of weight lost
              lbslost = float(lbslost) # Convert the input to a float
              totalLBs += lbslost # Add the amount of weight lost to the totalLBs variable
              break  # If the input is valid, break the while loop and move to the next week
            except ValueError: # If the input is not a number, display an error message
              print('/// Error 1 ///'.center(70))
              print('Please enter a number'.center(70))
        weight_lost.append(totalLBs) # Add the total amount of weight lost to the weight_lost list
        if totalLBs < 0: # If the total amount of weight lost is negative, display the total amount of weight gained
          print(f'\nTotal lbs gained: {abs(totalLBs)}\n')
        else: # If the total amount of weight lost is positive, display the total amount of weight lost
          print(f'\nTotal lbs lost: {totalLBs} lbs\n')
        valid_input = False # Set the valid_input variable to False to exit the while loop
    getting_input = False # Set the getting_input variable to False to exit the while loop

  return weight_lost # Return the weight_lost list

# ---------------------------- DISPLAY RESULTS ------------------------------

def display_results(weight, name, dollars):
  biggest_loser = max(weight) # Find the largest number in the weight list
  winner = name[weight.index(biggest_loser)] # Find the name of the person with the largest number in the weight list

  if biggest_loser < 0: # If the biggest_loser is negative, display a message saying that everyone gained weight
    print('')
    print('------------ WINNER ------------'.center(70))
    print('NONE')
    print(f"Everyone gained weight. No one wins.")
    print(f'--------------------------------'.center(70))
    return # Exit the function
  else: # If the biggest_loser is positive, display the winner and the amount of money they won
    print('')
    print('------------ WINNER ------------'.center(70))
    print(f"{winner.upper()} | {biggest_loser} lbs".center(70))
    print(f"Winning Amount: ${biggest_loser * dollars:.2f}".center(70))
    print(f'--------------------------------'.center(70))

#===========================================================================
#                                 Main
#===========================================================================

def main():
  # Declare variables
  people = ["Sam","Alex","Josh","Jenna","Tim"] # List of people
  price_per_lb = 1.50 # price per lb lost

  # Welcome message showing title and text
  welcome_message(people, price_per_lb)

  # Call the function to get the total weight lost for each person
  weight_lost = get_weight_lost(people)

  # Call the function to display the results
  display_results(weight_lost, people, price_per_lb)

#-------------------------------- EXECUTE ---------------------------------
main()