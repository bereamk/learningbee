#===========================================================================
#  *                                 INFO
#
#   Python code
#   Name: Robinson, Berea
#   Course/Section: CMSC 105/6387
#   Type: Discussion
#   Date: 2024-01-30

#   Objective: 
#       This program is a call back to the loan calculator I did during week 2
#       But more concise and calculations within its own functions.
#
#===========================================================================

import datetime
import textwrap

#--------------------------------- FUNCTIONS --------------------------------
# Welcome Information function
def welcome_message(title: str):
    today = datetime.date.today()

    message = dict(
        title = f"{title.upper()}",
        text = textwrap.fill(
            f"This program will calculate the cost of the interest accrued over "
            f"time, as well as the total amount of the future loan value."
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

# Function that calculates loan
def loanCalculation(loanAmount1,loanTime1,years1):
    # Interest rate is constant, so it's a local variable again
    interestRate1 = .086

    # Calculate the amount of interest accrued
    interestTotal = loanAmount1 * interestRate1 * loanTime1

    months = years1 * 12

    # Calculate the total amount of future value/amount accumulated
    loanTotal = ((interestRate1 * loanTime1) + 1) * loanAmount1

    interestperMonth = (interestTotal/months)
    loanperMonth = (loanTotal/months)

    monthlyTotal = interestperMonth + loanperMonth

    return interestTotal, loanTotal, interestperMonth, loanperMonth, monthlyTotal


#===========================================================================
#                                 Main
#===========================================================================
def main():
    # Local Variables
    interestRate = .086 #! If you want to change the interestRate, you must also change it in the loanCalculation function
    percentage = interestRate * 100

    print(welcome_message("Berea's Loan/Interest Calculation program v2.0"))
    print(
        f"\nPlease note that the current annual interest rate is", percentage, "%.\n\n"
        f"Please enter and provide the following information...\n"
        f"-----------------------------------------------------------------------"
    )  

    # Prompt user for loan amount and get user response
    loanAmount = float(input("\n What is the total loan amount ? \t    ")) #numeric input value 1

    # Prompt user for time of the investment (in years)
    loanTime = float(input("\n How many years is the loan for ? \t    ")) #numeric input value 2  

    interestTotal, loanTotal, interestperMonth, loanperMonth, monthlyTotal = loanCalculation(loanAmount,loanTime,loanTime)


    # Print the results
    print(
        f"\n--- Result ------------------------------------------------------------\n\n"
        f" The total amount of interest accrued over", int(loanTime), "years is:   \t$", f"{interestTotal:.2f}\n"
        f" The total amount of interest per month is:   \t$", f"{interestperMonth:.2f}\n\n"
        f" The future value/amount accumulated  for  your  loan  is:   \t$", f"{loanTotal:.2f}\n"
        f" The total amount req to be paid per month is:   \t$", f"{loanperMonth:.2f}"
        f" The final total per month:   \t$", f"{monthlyTotal:.2f}"
    )

#------------------------------- EXECUTE --------------------------------
main()