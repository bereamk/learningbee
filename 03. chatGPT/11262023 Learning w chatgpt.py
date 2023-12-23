### task 1 print a greeting
##print("Hello, World!")
##
###or
##
##greeting = "Hello, World!"
##print(greeting)
##
### task 2, simple arithmetic
##print(7+8)
##
###or
##
##number_1 = 7
##number_2 = 8
##
##
####This was my first attempt at the problem, but ChatGPT's solution is listed bellow
####
####def add_numbers(number_1, number_2):
####    total = number_1 + number_2
####    return total
##
#### ironically, my solution worked just as good...
##
##def add_numbers(number_1, number_2):
##    result = add_numbers(number_1, number_2)
##    print(result)
##
##
### Task 3 Using Variables
##a = 1
##b = 3
##
##print(a+b)
##
### Task 4 Concatenate Strings
##first_name = "berea"
##last_name = "robinson"
##
##print(first_name + " " + last_name)
##
### Task 5 If-statement
##if a > b:
##    print("a is greater than b")
##else:
##    print("b is greater than a")
##
### Task 6 Loop through Numbers
##for i in range(1,6):
##    print(i)
##
##
### Task 7 Append to a list
##numbers = [1, 2, 3]
##numbers.append(4)
##print(numbers)
##
##
################################
#### Creating a bit more of a complicated version of the knowledge
#### above.
##
### Task 1 Working with Lists in more detail:
### Task: Create a list of names. Write a loop that prints each
### name with a greeting, like "Hello, [name]!"
##
######THIS WAS WRONG, BUT THIS WAS MY INITIAL ATTEMPT:#####
##
####name = [alex, mike, john, sam, olivia]
####greeting = "Hello, "
####
####for i in range(alex, olivia):
####    print(greeting + name)
##
##names = ["alex", "mike", "john", "sam", "olivia"]  # List of names as strings
##greeting = "Hello, "
##
##for name in names:  # Loop over each name in the list
##    print(greeting + name)  # Print the greeting and the name
##
##
##
##########**###########**###########**###########**###########**###########**#
##########**###########**###########**###########**###########**###########**#
##########**###########**###########**###########**###########**###########**#

# Task 2 - Using Conditional Statements Inside Loops
#   Given a list of numbers, use a loop and if-conditions to print
#   "Even" for each even number and "Odd" for each odd number.

##numbers = [1, 4, 23, 98, 4, 5, 90, 9, 22, 34, 5, 1] # Define a list of numbers
##
##for number in numbers:
##    if number%2 == 0:   # For each number, it checks if the number is divisible by 2
##                        # with no remainder ('number % 2 == 0'). If this condition is
##                        # true, it prints "Even"; otherwise it prints "Odd".
##        print("Even")
##    else:
##        print("Odd")
        
## the [number] % 2 is "Even" because that means there's no remainder!!

##########**###########**###########**###########**###########**###########**#
##########**###########**###########**###########**###########**###########**#
##########**###########**###########**###########**###########**###########**#

# Task 3 - More Complex Functions
#   Write a function that takes a list of numbers as a parameter and returns
#   the sum of those numbers.

# My attempt:

##numbers = [1, 4, 23, 98, 4, 5, 90, 9, 22, 34, 5, 1] # Define a list of numbers
##
##l_1 = list(range(1,1))
##
##def total_sum():
##    for number in l_1:
##        print(total)
        

##### The solution:

# numbers = [1, 4, 23, 98, 4, 5, 90, 9, 22, 34, 5, 1] # Define a list of numbers

# def total_sum(numbers):  # Function takes 'numbers' list as a parameter
#     total = 0  # Initialize total sum to 0
#     for number in numbers:  # Loop over each number in the list
#         total += number  # Add each number to the total
#     return total  # Return the total sum

# # Example usage:
# numbers = [1, 4, 23, 98, 4, 5, 90, 9, 22, 34, 5, 1]  # List of numbers
# print(total_sum(numbers))  # Call the function and print the result


# def say_hello(name):
#     print(f"Hello, {name}!")

# say_hello("Alice")  # Directly prints "Hello, Alice!" when called

