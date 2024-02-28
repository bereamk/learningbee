#===========================================================================
#  *                                 INFO
#
#   Python code
#   Name: Robinson, Berea
#   Course/Section: CMSC 105/6387
#   Type: Practice
#   Date: 2024-01-31

#   Objective: 
#       Prompt the user for the price of one item. Also prompt the user for 
#       how many items they wishs to purchase. Calculate total cost of the items. 
#       Display the total cost. Add the sales tax to the total cost, where sales 
#       tax is total cost times tax rate. You define the tax rate. Display both the 
#       total cost and final cost. Design your program so that you have the 
#       following functions:
#       - 1 or 2 functions that prompt and validate the user input(s) and returns a 
#           valid input value.
#       - 1 function to Calculate the total cost, the sales tax and final cost.
#       - 1 function to Display both the total and final cost.
#       - Make sure you define a main program and all your functions with arguments 
#           and returns. No Globals.
#
#===========================================================================

import datetime
import textwrap

def main():
    # Variables
    taxRate = .19

    # Welcome Information
    print(welcome_message("SHOP OF HORRIBLE"))

    # User Input
    price, num = prompts()

    # Calculations & Output
    totalCost = cost(price,num)
    endAmount(totalCost, taxRate)

#===========================================================================
#                               FUNCTIONS
#===========================================================================

# ------ Welcome Information -----------------------------------------------
def welcome_message(title: str):
    today = datetime.date.today()

    message = dict(
        title = f"{title.upper()}",
        text = textwrap.fill(
            "Welcome to this horrible shop.\n\n"
            )
    )

    # Formating variables
    width = 70
    hr_sep = "="
    sm_hr_sep = "-"

    return(
        "\nDate: \t{today}"
        "\n{hr}\n"
        "{title: ^70}\n"
        "{hr}\n\n"
        "{text}"
        .format(
            hr = hr_sep * width,
            sm_hr = sm_hr_sep * width,
            today = today,
            **message
        )
    )

# ------ User Input --------------------------------------------------------
def prompts():
    price = float(input("\nWhat is the price of the item?: \t$"))

    # Validate
    if (price <= 0):
        print("Invalid number, please try again.")
        price = float(input("\nWhat is the price of the item?: \t$"))
    else:
        print("\tYou have entered that the price of the item is $", f"{price:.2f}")

    # Validate
    num = int(input("\nQuantity?: \t"))
    if (num <= 0):
        print("Invalid number, please try again.")
        num = int(input("\nQuantity?: \t"))
    else:
        print("\tYou have entered that the quantity of the item is ", num)

    return price, num

# ------ Calculations ------------------------------------------------------
# Calculates Total Cost
def cost(price,num):
    # Calculate
    totalCost = price * num
    return totalCost

# Function that displays total and final cost
def endAmount(totalCost1, taxRate1):
    saleTax = totalCost1 * taxRate1
    finalCost = saleTax + totalCost1
    print("\nYour total cost including sales tax is:\t $", f"{finalCost:.2f}")
    print("Your total cost w/o sales tax is:\t $", f"{totalCost1:.2f}")

#===========================================================================
#                                 Execute
#===========================================================================
main()