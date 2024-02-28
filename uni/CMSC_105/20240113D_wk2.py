# Python code
# Name: Robinson, Berea
# Course/Section: CMSC 105/6387
# Type: Discussion  
# Date: 2024-01-13

# Objective: This program will calculate the interest accrued from a loan over
# a period of time with a 8.6% interest rate, as well as calculate the total
# amount of the future value of the loan/amount accumulated over the time period inputed.       

# --- Program --------------------------------------------------------
def main():
    # Initialize variables
    interestRate = .056 #constant

    # Section title
    print("\n--- Week 2 Discussion -----------------------------------------------------")

    # Display Welcome message
    print("\nWelcome to Berea's Loan/Interest Calculation program")
    print("\nThis program will calculate the cost of the interest accrued over time, \n as well as the total amount of the future loan value.")
    print("\nPlease note that the current annual interest rate is", interestRate, ".")
    print("\n\nPlease enter and provide the following information...")
    print("\n---------------------------------------------------------------------------")

    # Prompt user for loan amount and get user response
    loanAmount = eval(input("\n What is the total loan amount ? \t    ")) #numeric input value 1

    # Prompt user for time of the investment (in years)
    loanTime = eval(input("\n How many years is the loan for ? \t    ")) #numeric input value 2

    # Calculate the amount of interest accrued
    interestTotal = loanAmount * interestRate * loanTime

    #C alculate the total amount of future value/amount accumulated
    loanTotal = ((interestRate * loanTime) + 1) * loanAmount

    # Display the output
    print("\n--- Result ----------------------------------------------------------------")
    print("\n The total amount of interest accrued over", loanTime, "years is:   \t$", f"{interestTotal:.2f}")
    print(" The future value/amount accumulated  for  your  loan  is:   \t$", f"{loanTotal:.2f}")

# --- Execute --------------------------------------------------------
main()
    

