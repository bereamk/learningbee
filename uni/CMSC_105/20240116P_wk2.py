# Python code
# Name: Robinson, Berea
# Course/Section: CMSC 105/6387
# Type: Practice
# Date: 2024-01-16

# Objective: 

# --- Program --------------------------------------------------------
def main():
    # Initialize variables 
    tax_rate = 0.15

    # Display welcome message
    print("\n Welcome!\n This program will calculate the total cost of the item you wish to purchase,\n as well as the sales tax included in the total.")

    # Prompt user for the price of item
    item_one = eval(input("\n What  is  the  cost  of  the item? : \t"))

    # Prompt user for how many items they wish to purchase
    item_quantity = int(input("\n How many items are you purchasing? : \t"))

    # Calculate total_cost of items
    total_cost = item_one * item_quantity

    # Calculate sales_tax of items (total_cost * tax_rate)
    sales_tax = total_cost * tax_rate

    # Calculate final_cost of items (sales_tax + total_cost)
    final_cost = sales_tax + total_cost

    print("------------------------------------------------------------------------------")

    # Display the result (total_cost, final_cost)
    print("\n The  total  cost of your purchase is  : \t$", total_cost)
    print(" The final cost including sales tax is : \t$", f"{final_cost:.2f}")


# --- Execute --------------------------------------------------------
main()
    

