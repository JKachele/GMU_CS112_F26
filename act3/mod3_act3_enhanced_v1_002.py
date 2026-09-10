#***************************************************************************************
#   				      Modular Programming & Linear Execution                       *
#                                                                                      *
#                          The Campus Concert Ticket Estimator					       *
#                                                                                      *
#***************************************************************************************


#***************************************************************************************
# 1. Required Import Statement                                                         *
#***************************************************************************************

import math

#***************************************************************************************
# 2. Custom Function Definition                                                        *
#***************************************************************************************

def calculate_ticket_cost(student_name, ticket_qty):
    # String manipulation using built-in string method
    formatted_name = student_name.upper()
    
    # Arithmetic operations resulting in an Int and a Float
    ticket_price = 15.00
    service_fee = 2.75
    
    # Calculate base and total costs
    total_cost = (ticket_qty * ticket_price) + service_fee
    
    # Boolean logic without an IF statement
    # Directly stores the True/False outcome of the comparison
    is_valid_order = ticket_qty <= 4
    
    return formatted_name, total_cost, is_valid_order


#***************************************************************************************
# 3. Main Script Execution (Input/Output)                                              *
#***************************************************************************************

raw_name = input("Enter your name: ")
raw_qty = input("Enter number of tickets desired: ")

# Convert input string to integer
ticket_count = int(raw_qty)

#***************************************************************************************
# Call function and unpack the returned values                                         *
#***************************************************************************************

buyer_name, grand_total, order_status = calculate_ticket_cost(raw_name, ticket_count)


#***************************************************************************************
# 6. Printing Results (Output)                                                         *
#***************************************************************************************

print("\n--- Ticket Order Summary ---")
print("Purchaser Name:", buyer_name)
print(f"Total Ticket Cost (inc. fees): ${grand_total:.2f}")
print("Is Order Within Limits?:", order_status)




