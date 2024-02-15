#===========================================================================
#  *                                 INFO
#
#   Python code
#   Name: Robinson, Berea
#   Date: 2024-01-30
#
#   Objective: 
#       This program works as a loan calculator that will ask for the interest
#       rate, loan amount, and time period the loan is for. 
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
            "This program will calculate the cost of the interest accrued over time, as well as the total amount of the future loan value."
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
def loanCalculation(interestRate1,loanAmount1,loanTime1,years1):
    # Calculate the amount of interest accrued
    interestTotal = loanAmount1 * interestRate1 * loanTime1

    # Calculate the amount of total months
    months = years1 * 12

    # Calculate the total amount of future value/amount accumulated
    loanTotal = ((interestRate1 * loanTime1) + 1) * loanAmount1

    # Calculate the interest paid per month
    interestperMonth = (interestTotal/months)

    # Calculate the loan payment per month
    loanperMonth = (loanTotal/months)

    # Calculate the total payment of loan/principle and interest
    monthlyTotal = interestperMonth + loanperMonth

    return interestTotal, loanTotal, interestperMonth, loanperMonth, monthlyTotal


#===========================================================================
#                                 Main
#===========================================================================
def main():
    print(welcome_message("Berea's Loan/Interest Calculation program v2.0"))
    print(
        f"\nPlease enter and provide the following information...\n"
        f"-----------------------------------------------------------------------"
    )  

    # Prompt user for loan interest rate
    interestRate = float(input("\n What is your loan's interest rate (in decimal) ? \t    "))

    # Prompt user for loan amount and get user response
    loanAmount = float(input("\n What is the total loan amount ? \t    ")) #numeric input value 1

    # Prompt user for time of the investment (in years)
    loanTime = float(input("\n How many years is the loan for ? \t    ")) #numeric input value 2  

    interestTotal, loanTotal, interestperMonth, loanperMonth, monthlyTotal = loanCalculation(interestRate,loanAmount,loanTime,loanTime)


    # Print the results
    print(
        f"\n--- Result ------------------------------------------------------------\n\n"
        f" The  total  amount  of  interest accrued over", int(loanTime), "years is:       $", f"{interestTotal:.2f}\n"
        f" The future value/amount accumulated  for  your  loan  is:    \t$", f"{loanTotal:.2f}\n\n"
        f" The total amount of interest per month is:   \t$", f"{interestperMonth:.2f}\n"
        f" The   total   principle   per   month  is:   \t$", f"{loanperMonth:.2f}\n"
        f" The    final     total     per      month:   \t$", f"{monthlyTotal:.2f}"
    )

#------------------------------- EXECUTE --------------------------------
main()