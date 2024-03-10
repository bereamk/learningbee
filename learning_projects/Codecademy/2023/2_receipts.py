# Platform: Codecademy 
# Course: Learn Python 3
# Author: Berea Robinson
# Date: 2023-11-27
# Objective: Receipts for Lovely Loveseats
# Description: The aim is to store all the names and prices of a furniture store's catalog in
# variables. Process the total price and item list of customers, printing them out to the 
# output terminal.


# Items within the store

lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
lovely_loveseat_price = 254.00 # item one

stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50 # item two

luxurious_lamp_description = "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
luxurious_lamp_price = 52.15 # item three

sales_tax = .088 # sales tax 8.8%

###############
#FIRST CUSTOMER

customer_one_total = 0 # current total of the customer

customer_one_itemization = ""

###############
#THE PURCHASES

customer_one_total += lovely_loveseat_price
customer_one_itemization += "- " + lovely_loveseat_description + "\n"
customer_one_total += luxurious_lamp_price
customer_one_itemization += "- " + luxurious_lamp_description + "\n"

###############
#THE SALES TAX

customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

###############
#THE RECIEPT

print("Customer One Items:")
print(customer_one_itemization)
print("")
print("Customer One Total:")
print(f"{customer_one_total:.2f}")