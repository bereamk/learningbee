# Python code
# Name: Robinson, Berea
# Course/Section: CMSC 105/6387
# Type: Assignment
# Date: 2024-01-16

# Objective: This program will compute the daily pay for an Uber driver. 

# --- Program --------------------------------------------------------
def main():
    # Initialize variables
    hourlyRate = 16.50 #constant value
    commissionRate = .05 #constant value
    
    # Display welcome message
    print(f"\n\nWelcome UBER DRIVER !\n"
          f"\nThis program will help you calculate your daily wage, commission pay,\n"
          f"and your total pay for the day.\n"
          f"\n When ready, please provide the following information...\n"
          f"\n---------------------------------------------------------------------------")

    # Prompt the number of miles driven for the day
    totalMiles = eval( #eval is used in the event the user inputs a float
        input("\n How many miles have you driven?\t   ")
        ) 

    # Prompt the number of hours worked for the day
    hoursWorked = eval( #eval is used in the event the user inputs a float
        input("\n How many hours have you worked?\t   ")
        ) 

    # Prompt the amount of tips recieved for the day
    tipsEarned = eval( #eval is used in the event the user inputs a float
        input("\n How much did you earn in tips?\t\t $ ")
        )

    # Calcuclate the daily wage
    dailyWage = hoursWorked * hourlyRate

    # Calculate the commission pay
    commissionPay = totalMiles * commissionRate

    # Calculate the total pay for the day
    totalPay = dailyWage + commissionPay + tipsEarned

    # Display the output
    print(
        f"\n\n--- Your Daily Earnings ---------------------------------------------------\n\n"
        f" Daily        Wage:     \t$", f"{dailyWage:.2f}\n" # outputs daily wage
        f" Commission    Pay:       \t$", f"{commissionPay:.2f}\n" # outputs commission pay
        f" Total Tips Earned:       \t$", f"{tipsEarned:.2f}\n\n" # outputs total tips earned
        f" Total Pay for the Day: \t$", f"{totalPay:.2f}\n\n\n" # outputs total pay
          )

# --- Execute --------------------------------------------------------
main()
    
