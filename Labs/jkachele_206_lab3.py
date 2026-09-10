'''
-------------------------------------------------------------------------------
Name: Justin Kachele
Partner's Name: Elizabeth Ford 
Assignment: Lab 3
Due by end of your lab class
-------------------------------------------------------------------------------
Honor Code Statement: I received no assistance on this assignment that
violates the ethical guidelines set forth by the professor and class syllabus,
including any AI or code auto-complete tools.
-------------------------------------------------------------------------------
'''

#Partner A -- write area_of_base function here
def area_of_base(side_len):
    area = side_len * side_len
    return round(area, 4)

#Partner B -- write area_of_side function here
def area_of_side(base_len, height):
    area = 0.5 * base_len * height
    return round(area, 4)

#Write pyramid_surface_area function to calculate surface area of pyramid here
def pyramid_surface_area(base_len, slant_height):
    base_area = area_of_base(base_len)
    side_area = area_of_side(base_len, slant_height)
    surface_area = base_area + (4 * side_area)
    return round(surface_area, 4)

#Write pyramid_volume function to calculate the volume of the pyramid (and any other functions you make) here
def pyramid_volume(base_len, height):
    base_area = area_of_base(base_len)
    volume = (1 / 3) * base_area * height
    return round(volume, 4)
