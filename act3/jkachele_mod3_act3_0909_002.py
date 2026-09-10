#**************************************************************************************
#   				      Modular Programming & Linear Execution                      *
#                                                                                     *
#                        The Campus Café Order Calculator Problem					  *
#                                                                                     *
#**************************************************************************************


#**************************************************************************************
# 1. Required Import Statement                                                        *
#**************************************************************************************

import math

#**************************************************************************************
# 2. Function 1: Input Handling                                                       *
#**************************************************************************************

def get_user_input():
    
    #Prompts the user for details 
    raw_name = input("Enter your name: ")
    raw_qty = input("Enter number of tickets desired: ")
    
    # Type conversion from string to integer (int)
    ticket_count = int(raw_qty)

    return raw_name, ticket_count



#**************************************************************************************
# 2. Custom Functions Definitions                                                     *
#**************************************************************************************

def calculate_ticket_cost(stu_name, ticket_qty):
    
    # Arithmetic operations resulting in a Float (float)
    ticket_price = 15.00
    service_fee = 2.75
    grand_total = (ticket_qty * ticket_price) + service_fee
    
    #String Manipulation 
    student_name = stu_name.upper()
    
    # Comparison operator evaluates directly to a Boolean value (bool)
    # Evaluates to True if ticket limit (4) is respected
    order_status = ticket_qty <= 4
    
    return student_name, grand_total, order_status

#*************************************************************************************
# 4. Output the results                                                             *
#*************************************************************************************    
    
def display_order_summary(buyer_name, grand_total, order_status):
    
    #Outputs the processed data
    print("\n--- Ticket Order Summary ---")
    print("Purchaser Name:", buyer_name)
    print(f"Total Ticket Cost (inc. fees): ${grand_total:.2f}")
    print("Is Order Within Limits?:", order_status)



#**************************************************************************************
# 3. Main Script Execution (Input/Output)                                             *
#**************************************************************************************

#Get the raw data 
input_name, input_qty = get_user_input() # call the function

#Process the raw data 
processed_name, total_bill, limits_check = calculate_ticket_cost(input_name, input_qty) #call the function 

#Output the results
display_order_summary(processed_name, total_bill, limits_check) #call the function 




