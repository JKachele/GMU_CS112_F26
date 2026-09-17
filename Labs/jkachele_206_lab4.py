'''
-------------------------------------------------------------------------------
Name: Justin Kachele
Partner's Name: Elizabeth Ford 
Assignment: Lab 4
Due by end of your lab class
-------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by the professor and class syllabus,
including any AI or code auto-complete tools.
-------------------------------------------------------------------------------
'''

# Part 1 -- Understanding Branching 

def branches_function():
    x = -1
    result = False
    if (x < 0) and (x != 0):
        result = True
    return result

# print(branches_function())

'''
Run the function above. What does it always return? Why?

Answer: 
    It always returns false because the variable 'x' is 1 which is not less than 0

Change the function so that it will always return True. Explain what you changed
and why it will now always return True.

Answer: 
    I changed the variable 'x' to -1 which is both less tha zero and not equal to zero

'''

# Part 2 -- Writing Code with Branching

def categorize(price, units_sold):
    category = ""
    if (price < 10.0) and (units_sold < 10):
        category = "Low-priced"
    elif (price >= 10.0) and (price <= 20.0) and (units_sold < 20):
        category = "Mid-priced"
    elif (price > 20.0) and (units_sold < 30):
        category = "High-priced"
    elif (price > 20.0) and (units_sold >= 30):
        category = "Premium"
    else:
        category = "Other"
    return category

# print(categorize(5.8, 5))
# print(categorize(10.0, 10))
# print(categorize(20.01, 25))
# print(categorize(24.13, 30))
# print(categorize(9.99, 10))

