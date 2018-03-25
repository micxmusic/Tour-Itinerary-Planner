"""
function takes in a place name and finds k number of locations closest
to that place from the list of locations
"""
def kclosest(place, k, locations):
    
    sorted_locations =[]
    output = []
    
    #calculates distance of each location and adds to new list a tuple 
    #containing location name and corresponding distance
    
    for i in range(len(locations)):
        distance = (((place[0]-locations[i][1])**2+
                    (place[1]-locations[i][2])**2)**0.5)
        sorted_locations.append(tuple([locations[i][0],distance]))
    
    #sorts list by distance which is stored as second element in tuple
    sorted_locations.sort(key=lambda tup: tup[1])
    
    #appends specified number of locations to output list
    for j in range(k):
        output.append(sorted_locations[j][0])
    
    #returns list of specified number of closest locations
    return output
