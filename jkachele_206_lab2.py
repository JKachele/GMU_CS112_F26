'''
-------------------------------------------------------------------------------
Name: Justin Kachele
Partner's Name: Elizabeth Ford 
Assignment: Lab 2
Date: Sep 03, 2026
Due by end of your lab class
-------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by the professor and class syllabus,
including any AI or code auto-complete tools.
-------------------------------------------------------------------------------
'''

'''
###################################################
Your OWN test cases:
1) Barbie: 5 Ken: 4 Hours: 10
   Results: 90

2) Barbie: 6 Ken: 3 Hours: 4
   Results: 36

3) Barbie: 3 Ken: 9 Hours: 17
   Results: 204

4) Barbie: 11 Ken: 8 Hours: 6
   Results: 114

5) Barbie: 50 Ken: 88 Hours: 36
   Results: 4968
'''


'''
##############################
Write out the algorithm (your plan) for the task:
    Save the 3 inputs as variables: barbie, ken, and hours
    final output is (barbie + ken) * hours

'''


#Type your code below:
barbie = int(input("Enter hanging speed of Barbie (lights per minute): "))
ken    = int(input("Enter hanging speed of Ken (lights per minute): "))
hours  = int(input("Enter total time in minutes: "))

num_lights = (barbie + ken) * hours

print("The total number of lights hung are:", num_lights)





 

