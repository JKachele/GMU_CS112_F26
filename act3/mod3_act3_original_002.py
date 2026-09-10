#***********************************************************************************
#   				Monolithic Programming & Linear Execution                      *
#                                                                                  *
#                    The Campus Concert Ticket Estimator				           *
#                                                                                  *
#***********************************************************************************


#***********************************************************************************
# 1. Required Import Statement                                                     *
#***********************************************************************************

import math

#***********************************************************************************
# 2. Input Section                                                                 *
#***********************************************************************************

raw_name = input("Enter your name: ")
raw_qty = input("Enter number of tickets desired: ")


#***********************************************************************************
# 3. Data Conversion & Type Exploration                                            *
# Convert the raw input string into an Integer (int)                               *
#***********************************************************************************

ticket_count = int(raw_qty)

#**********************************************************************************
# Modify the raw text using a built-in method to get an uppercase String (string) *
#**********************************************************************************

buyer_name = raw_name.upper()

#**********************************************************************************
# 4. Arithmetic Operations & Float Calculations                                   *
#**********************************************************************************

ticket_price = 15.00
service_fee = 2.75

#**********************************************************************************
# Multiply the integer count by the float price, then add the fee float           *
#**********************************************************************************

grand_total = (ticket_count * ticket_price) + service_fee

#**********************************************************************************
# 5. Boolean Logic without an IF Statement                                        *
# The comparison operator (<=) directly yields a Boolean value (bool)             *     
# This flags true if the student stays within the 4-ticket purchase threshold     *
#**********************************************************************************

order_status = ticket_count <= 4

#**********************************************************************************
# 6. Printing Results (Output)                                                    *
#**********************************************************************************

print("\n--- Ticket Order Summary ---")
print("Purchaser Name:", buyer_name)
print(f"Total Ticket Cost (inc. fees): ${grand_total:.2f}")
print("Is Order Within Limits?:", order_status)




