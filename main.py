from reference import kclosest

"""
function removes the input location from the string of locations to
avoid the same location from being read as closest location, and 
returns the coordinates of said location in a tuple
"""
def remove_loc(loc, locations):
    for i in range(len(locations)):
        if loc == locations[i][0]:
            place=tuple([locations[i][1],locations[i][2]])
            locations.remove(locations[i])
            break
    return place

def buildtour(start,locations):
    #initializing list to store location names starting with the start input
    tour = [start]
    #remove_loc function sets up the coordinates of the start location
    coods = remove_loc(start, locations)
    
    """
    while loop appends next nearest location then removes it from 
    the list until list locations no longer has elements
    """
    while len(locations)>0:
        location = kclosest(coods,1,locations)[0]
        coods = remove_loc(location, locations)
        tour.append(location)
    
    return tour
    