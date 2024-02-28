# Python code
# Name: Robinson, Berea
# Course/Section: CMSC 105/6387
# Type: Discussion
# Date: 2024-01-17

# Objective: This is a simple calculator that's capable of taking inputs
# that are numbers and +,/,*,-. Based on user input, the calculator will
# do the necesary calculation.

# --- Program -------------------------------------------------------
def main():
    # Welcome message
    print(
        f"\n\n--- CALCULATOR --------------------------------------------------\n\n"
        f" Welcome to the Calculator program!\n"
        f" This calculator will help you to do basic computations.\n"
        f" But first things first...\n\n"
        )
    
    # User inputs name
    name = input("What is your name? : \t")
    
    # Instructions
    operator = input(f"\n\n{name}, would you like to subtract (-), add (+), multiply (*)\nor divide (/)? Type 'exit' to quit : \t")
    
    # If user wants to quit
    if operator == 'exit':
        quit()

    # Number inputs from user
    num1 = eval(input("\n\tEnter first number : "))
    num2 = eval(input("\n\tEnter second number: "))
    
    # Arithmetic operations with error message
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero"
    else:
        result = "Invalid operator"

    # Display result
    print(
        f"\nResulting answer:", result
        )

#--- Execute --------------------------------------------------------
main()
