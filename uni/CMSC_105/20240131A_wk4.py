#===========================================================================
#  *                                 INFO
#
#   Python code
#   Name: Robinson, Berea
#   Course/Section: CMSC 105/6387
#  Type: Assignment
#   Date: 2024-02-06

#   Objective: 
#       This program is designed to estimate the cost of house cleaning services.
#       It prompts the user to enter the number of rooms in their house and select
#       a type of cleaning service (e.g., floors, windows, bathrooms). The program
#       calculates the total cost based on the house size (categorized as small,
#       medium, large, or extra large) and the selected cleaning service. Prices vary
#       for different types of cleaning. 
#
#       Update: I've moved the calculations to their own function.
#
#===========================================================================
import datetime
import textwrap

#--------------------------------- FUNCTIONS --------------------------------

# Welcome Information
def titledisplay(title: str):
    today = datetime.date.today()

    message = dict(
        title = f"{title.upper()}",
        text = f"Welcome to our cleaning service!"
    )

    # Formating variables
    width = 70
    hr_sep = "="

    return(
        "\nDate: \t{today}"
        "\n{hr}\n"
        "{title: ^70}\n"
        "{hr}\n"
        "{text}\n"
        .format(
            hr = hr_sep * width,
            today = today,
            **message
        )
    )

# Function accepts the number of rooms and the type of cleaning service. Returns the total cost of the house cleaning.
def calculateCost(rooms1: int, cleaning1: str):
    # Constants for house sizes
    smallHouse = 1 
    medHouse = 3 
    largeHouse = 5
    xlHouse = 10

    # Constants for cleaning servies
    floors = float(25.99)
    windows = float(10.50)
    bathrooms = float(30.99)

    total = 0 # Sets the total to ensure it's always defined
    
    # Determine the base rate multiplier based on the house size
    # This multiplier reflects the scale of cleaning effort required for different house sizes
    # Example: For a medium house, the base rate multiplier is 3
    if rooms1 < smallHouse:
        print("Invalid. Please enter a number greater than 0.")
        return 0 # Return 0 to indicate an error in input
    elif rooms1 < medHouse:
        baseRate = 2  # Small houses
    elif rooms1 < largeHouse:
        baseRate = 3  # Medium houses
    elif rooms1 < xlHouse:
        baseRate = 5  # Large houses
    else:
        baseRate = 20  # Extra large houses

    # Calculate the total cost based on the selected cleaning type and the base rate
    # The total cost is the product of the base rate and the price of the chosen cleaning service
    if cleaning1 == "F":
        total = baseRate * floors
    elif cleaning1 == "W":
        total = baseRate * windows
    elif cleaning1 == "B":
        total = baseRate * bathrooms
    else:
        print("Error 101: Please enter a valid cleaning type [F, W, B].") # If a letter other than F, W, or B is used, this error will display
        return 0  # Return 0 to indicate an error in input

    # The total cost is returned to the main function
    return total


#===========================================================================
#                                 Main
#===========================================================================

def main():
    # Welcome message showing title, text, and cleaning options
    print(titledisplay("Berea's Cleaning Service v2.0"))
    print(textwrap.fill(
        f"Based on the number of rooms your home has and the cleaning type selected,"
        f" we will create an estimate of the total cost."
    ),
        f"\n\nWe offer three options for cleaning :\n\n"
        f"\t [F] Floors\n" 
        f"\t [W] Windows\n"
        f"\t [B] Bathrooms\n"
    )

    rooms_input = input("How many rooms need cleaning? \t")
    if not rooms_input.isdigit() or int(rooms_input) < 1:
        print("Please enter a valid, positive number of rooms.")
        return  # Exits the program if the input is not a positive integer

    rooms = int(rooms_input)  # Convert input to integer after validation

    cleaning = input("What type of cleaning for the rooms [F, W, B]? ").upper()
    if cleaning not in ['F', 'W', 'B']:
        print("Please enter a valid cleaning type [F, W, B].")
        return  # Exits the program if the cleaning type is invalid

    totalCost = calculateCost(rooms, cleaning)
    if totalCost > 0:
        print(f"\nThe total cost of cleaning is: ${totalCost:.2f}")
    else:
        print("An error occurred, please try again with valid inputs.")


#------------------------------- EXECUTE --------------------------------
main()