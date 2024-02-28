#===========================================================================
#  *                                 INFO
#
#   Python code
#   Name: Robinson, Berea
#   Course/Section: CMSC 105/6387
#   Type: Assignment
#   Date: 2024-01-26

#   Objective: 
#       This program is designed to estimate the cost of house cleaning services.
#       It prompts the user to enter the number of rooms in their house and select
#       a type of cleaning service (e.g., floors, windows, bathrooms). The program
#       calculates the total cost based on the house size (categorized as small,
#       medium, large, or extra large) and the selected cleaning service. Prices vary
#       for different types of cleaning. 
#
#===========================================================================
import datetime
import textwrap
#===========================================================================
#                          TITLES / WELCOME MESSAGE
#===========================================================================

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
    sm_hr_sep = "-"

    return(
        "\nDate: \t{today}"
        "\n{hr}\n"
        "{title: ^70}\n"
        "{hr}\n"
        "{text}\n"
        .format(
            hr = hr_sep * width,
            sm_hr = sm_hr_sep * width,
            today = today,
            **message
        )
    )

#===========================================================================
#                                 Main
#===========================================================================

def main():
    # Constants for house sizes
    smallHouse = 1 
    medHouse = 3 
    largeHouse = 5
    xlHouse = 10

    # Constants for cleaning servies
    floors = float(25.99)
    windows = float(10.50)
    bathrooms = float(30.99)

    # Welcome message showing title, text, and cleaning options
    print(titledisplay("Berea's Cleaning Service"))
    print(textwrap.fill(
        "Based on the number of rooms your home has and the cleaning type selected, we will create an estimate of the total cost."
    ),
        f"\n\nWe offer three options for cleaning :\n\n"
        f"\t [F] Floors\n" 
        f"\t [W] Windows\n"
        f"\t [B] Bathrooms\n"
    )

    # Determine the base rate multiplier based on the house size
    # This multiplier reflects the scale of cleaning effort required for different house sizes
    # Example: For a medium house, the base rate multiplier is 3
    rooms = int(input("How many rooms need cleaning? \t"))
    if (rooms < smallHouse):
        print("Invalid. Please put a number greater than 0.")
    elif (rooms < medHouse):
        baseRate = 2 # Base rate for small houses
    elif (rooms < largeHouse):
        baseRate = 3 # Base rate for medium houses
    elif (rooms < xlHouse):
        baseRate = 5 # Base rate for large houses
    elif (rooms >= xlHouse):
        baseRate = 20 # Base rate for extra large houses
    # There is no "else" statment, because it wouldn't have a significant impact on the code

    # Calculate the total cost based on the selected cleaning type and the base rate
    # The total cost is the product of the base rate and the price of the chosen cleaning service
    cleaning = input("What type of cleaning for the rooms [F, W, B]? ").upper() # .upper() forces the string typed to be uppercase to avoid errors in input
    if cleaning == "F":
        total = baseRate * floors
    elif cleaning == "W":
        total = baseRate * windows
    elif cleaning == "B":
        total = baseRate * bathrooms
    else:
        print("Error 101: Please enter a valid cleaning type.") # If a letter other than F, W, or B is used, this error will display

    # Output the total cost
    print(f"\nThe total cost estimate for your home is: ${total:.2f}") 
    
    


#------------------------------- EXECUTE --------------------------------
main()